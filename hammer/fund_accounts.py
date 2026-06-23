#!/usr/bin/env python3
import argparse
import os
import sys
from decimal import Decimal

import requests
from web3 import Web3, HTTPProvider

# Allow running as ./fund_accounts.py from /app/hammer.
if __name__ == '__main__' and __package__ is None:
    from os import path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from hammer.accounts import load_accounts_file, normalize_private_key


DEFAULT_GAS_LIMIT = 21000
DEFAULT_TRANSFER_GAS_LIMIT = 40000
DEFAULT_TRANSFER_VALUE_WEI = 1


def default_accounts_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts.json")


def parse_int(value):
    return int(str(value), 0)


def ether_to_wei(value):
    return int(Decimal(str(value)) * Decimal(10 ** 18))


def rpc_call(rpc, method, params=None):
    payload = {"jsonrpc": "2.0", "method": method, "params": params or [], "id": 1}
    response = requests.post(rpc, json=payload, headers={"Content-type": "application/json"}, timeout=30)
    data = response.json()
    if "error" in data:
        raise RuntimeError("%s failed: %s" % (method, data["error"]))
    return data.get("result")


def get_chain_id(rpc):
    result = rpc_call(rpc, "eth_chainId", [])
    if result is None:
        return None
    return int(result, 16)


def select_accounts(accounts, start, count):
    if start < 0:
        raise SystemExit("--start must be >= 0")
    selected = accounts[start:]
    if count is not None:
        selected = selected[:count]
    return selected


def resolve_amount_wei(args):
    provided = [args.amount_wei is not None, args.amount_ether is not None, args.txs_per_account is not None]
    if sum(1 for item in provided if item) != 1:
        raise SystemExit("pass exactly one of --amount-wei, --amount-ether, or --txs-per-account")

    if args.amount_wei is not None:
        return parse_int(args.amount_wei)
    if args.amount_ether is not None:
        return ether_to_wei(args.amount_ether)

    gas_price = parse_int(args.transfer_gas_price_wei)
    transfer_gas_limit = parse_int(args.transfer_gas_limit)
    transfer_value = parse_int(args.transfer_value_wei)
    extra = parse_int(args.extra_wei)
    return int(args.txs_per_account) * (transfer_gas_limit * gas_price + transfer_value) + extra


def send_funding_transactions(w3, args, accounts, amount_wei):
    private_key = normalize_private_key(args.private_key)
    from_address = w3.toChecksumAddress(args.from_address)
    gas_price = parse_int(args.gas_price_wei) if args.gas_price_wei else w3.eth.gasPrice
    gas_limit = parse_int(args.gas_limit)
    nonce = w3.eth.getTransactionCount(from_address)

    chain_id = args.chain_id
    if chain_id == "auto":
        chain_id = get_chain_id(args.rpc)
    elif chain_id is not None:
        chain_id = parse_int(chain_id)

    total_wei = amount_wei * len(accounts)
    total_gas_wei = gas_price * gas_limit * len(accounts)
    balance = w3.eth.getBalance(from_address)

    print("Funding %d accounts" % len(accounts))
    print("Amount per account: %d wei" % amount_wei)
    print("Total transfer value: %d wei" % total_wei)
    print("Estimated gas: %d wei" % total_gas_wei)
    print("Sender balance: %d wei" % balance)
    if balance < total_wei + total_gas_wei:
        raise SystemExit("sender balance is too low")

    if args.dry_run:
        print("Dry run only; no transactions sent.")
        return

    hashes = []
    for offset, account in enumerate(accounts):
        to_address = w3.toChecksumAddress(account["address"])
        tx = {
            "from": from_address,
            "to": to_address,
            "nonce": nonce + offset,
            "value": amount_wei,
            "gas": gas_limit,
            "gasPrice": gas_price,
        }
        if chain_id is not None:
            tx["chainId"] = chain_id

        signed = w3.eth.account.signTransaction(tx, private_key)
        tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
        tx_hash_hex = w3.toHex(tx_hash)
        hashes.append(tx_hash_hex)
        print("%d %s -> %s" % (offset, to_address, tx_hash_hex))

    if args.wait:
        for tx_hash in hashes:
            receipt = w3.eth.waitForTransactionReceipt(tx_hash, timeout=args.timeout)
            print("mined %s block=%s gasUsed=%s" % (tx_hash, receipt.blockNumber, receipt.gasUsed))


def parse_args():
    parser = argparse.ArgumentParser(description="Fund generated chainhammer sender accounts.")
    parser.add_argument("--rpc", default=os.getenv("RPC"), help="Ethereum JSON-RPC URL; default: RPC env")
    parser.add_argument("--from-address", default=os.getenv("PRIVATE_KEY_ADDRESS"),
                        help="funding account address; default: PRIVATE_KEY_ADDRESS env")
    parser.add_argument("--private-key", default=os.getenv("PRIVATE_KEY"),
                        help="funding account private key; default: PRIVATE_KEY env")
    parser.add_argument("--accounts-file", default=os.getenv("ACCOUNTS_FILE", default_accounts_path()),
                        help="generated accounts JSON file")
    parser.add_argument("--start", type=int, default=0, help="first account index to fund")
    parser.add_argument("--count", type=int, default=None, help="number of accounts to fund")
    parser.add_argument("--amount-wei", default=None, help="fixed funding amount per account")
    parser.add_argument("--amount-ether", default=None, help="fixed funding amount in ether per account")
    parser.add_argument("--txs-per-account", type=int, default=None,
                        help="derive funding for this many benchmark txs per account")
    parser.add_argument("--transfer-gas-limit", default=os.getenv("TRANSFER_GAS_LIMIT", DEFAULT_TRANSFER_GAS_LIMIT),
                        help="gas limit used later by send_multi_transfer_chain.py")
    parser.add_argument("--transfer-gas-price-wei", default=os.getenv("TRANSFER_GAS_PRICE_WEI", "20000000000"),
                        help="gas price used later by send_multi_transfer_chain.py")
    parser.add_argument("--transfer-value-wei", default=os.getenv("TRANSFER_VALUE_WEI", DEFAULT_TRANSFER_VALUE_WEI),
                        help="value sent by each later benchmark tx")
    parser.add_argument("--extra-wei", default="0", help="extra wei to add per funded account")
    parser.add_argument("--gas-limit", default=DEFAULT_GAS_LIMIT, help="gas limit for each funding transfer")
    parser.add_argument("--gas-price-wei", default=None, help="gas price for funding transfers; default: node gasPrice")
    parser.add_argument("--chain-id", default=None,
                        help="optional chain id for signed funding transactions; pass auto to query eth_chainId")
    parser.add_argument("--wait", action="store_true", help="wait for funding transaction receipts")
    parser.add_argument("--timeout", type=int, default=120, help="receipt wait timeout")
    parser.add_argument("--dry-run", action="store_true", help="print totals without sending transactions")
    return parser.parse_args()


def main():
    args = parse_args()
    if not args.rpc:
        raise SystemExit("missing --rpc or RPC env")
    if not args.from_address:
        raise SystemExit("missing --from-address or PRIVATE_KEY_ADDRESS env")
    if not args.private_key:
        raise SystemExit("missing --private-key or PRIVATE_KEY env")

    accounts = load_accounts_file(args.accounts_file, require_private_key=False)
    accounts = select_accounts(accounts, args.start, args.count)
    if not accounts:
        raise SystemExit("no accounts selected")

    amount_wei = resolve_amount_wei(args)
    w3 = Web3(HTTPProvider(args.rpc, request_kwargs={'timeout': 120}))
    send_funding_transactions(w3, args, accounts, amount_wei)


if __name__ == "__main__":
    main()
