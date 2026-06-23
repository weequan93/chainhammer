#!/usr/bin/env python3
import argparse
import json
import os
import sys

try:
    from eth_account import Account
except Exception:
    print("eth-account is unavailable. Run this inside the Docker image or install requirements first.")
    sys.exit(1)


def default_output_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts.json")


def private_key_to_hex(private_key):
    if isinstance(private_key, bytes):
        return private_key.hex()
    if hasattr(private_key, "hex"):
        private_key = private_key.hex()
    private_key = str(private_key)
    if private_key.startswith("0x"):
        private_key = private_key[2:]
    return private_key


def generate_accounts(count):
    accounts = []
    for index in range(count):
        account = Account.create(os.urandom(32))
        private_key = getattr(account, "privateKey", None)
        if private_key is None:
            private_key = getattr(account, "key", None)
        if private_key is None:
            private_key = getattr(account, "_private_key", None)
        accounts.append({
            "index": index,
            "address": account.address,
            "private_key": private_key_to_hex(private_key),
        })
    return accounts


def write_json(filename, accounts, force=False):
    if os.path.exists(filename) and not force:
        raise RuntimeError("%s already exists; pass --force to overwrite it" % filename)

    data = {"accounts": accounts}
    with open(filename, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("\n")


def write_ppk(filename, accounts, force=False):
    if os.path.exists(filename) and not force:
        raise RuntimeError("%s already exists; pass --force to overwrite it" % filename)

    with open(filename, "w") as f:
        f.write("ADDRESS_LIST = [\n")
        for account in accounts:
            f.write('    "{address}", "{private_key}",\n'.format(**account))
        f.write("]\n")


def parse_args():
    parser = argparse.ArgumentParser(description="Generate fresh Ethereum sender accounts for chainhammer.")
    parser.add_argument("count", type=int, help="number of accounts to generate")
    parser.add_argument("--output", default=default_output_path(),
                        help="JSON output path, default: hammer/accounts.json")
    parser.add_argument("--ppk-output", default=None,
                        help="optional Python ppk.py style output path")
    parser.add_argument("--force", action="store_true", help="overwrite existing output files")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.count <= 0:
        raise SystemExit("count must be greater than zero")

    accounts = generate_accounts(args.count)
    write_json(args.output, accounts, force=args.force)
    if args.ppk_output:
        write_ppk(args.ppk_output, accounts, force=args.force)

    print("Generated %d accounts" % len(accounts))
    print("JSON: %s" % args.output)
    print("First address: %s" % accounts[0]["address"])
    print("Use with Docker: -e ACCOUNTS_FILE=/app/hammer/accounts.json")
    print("These private keys are test keys. Do not fund them on a real-value chain.")


if __name__ == "__main__":
    main()
