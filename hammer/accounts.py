#!/usr/bin/env python3
import json
import os


ACCOUNTS_FILE_ENV = "ACCOUNTS_FILE"


def normalize_private_key(private_key):
    if private_key is None:
        return None
    private_key = str(private_key)
    if private_key.startswith("0x"):
        private_key = private_key[2:]
    return private_key


def _account_from_pair(address, private_key=None, require_private_key=True):
    if not address:
        raise ValueError("account entry is missing address")
    if require_private_key and not private_key:
        raise ValueError("account entry for %s is missing private_key" % address)
    return {
        "address": str(address),
        "private_key": normalize_private_key(private_key),
    }


def load_accounts_file(filename, require_private_key=True):
    """
    Load generated accounts from JSON.

    Supported formats:
    - {"accounts": [{"address": "...", "private_key": "..."}, ...]}
    - [{"address": "...", "private_key": "..."}, ...]
    - ["0xaddress", "privatekey", "0xaddress2", "privatekey2", ...]
    """
    with open(filename, "r") as f:
        data = json.load(f)

    if isinstance(data, dict):
        data = data.get("accounts")

    if not isinstance(data, list):
        raise ValueError("accounts file must contain a list or an accounts list")

    if len(data) == 0:
        return []

    if all(isinstance(item, str) for item in data):
        if len(data) % 2 != 0:
            raise ValueError("flat account list must contain address/private-key pairs")
        accounts = []
        for i in range(0, len(data), 2):
            accounts.append(_account_from_pair(data[i], data[i + 1], require_private_key))
        return accounts

    accounts = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("account entries must be objects")
        private_key = item.get("private_key", item.get("privateKey"))
        accounts.append(_account_from_pair(item.get("address"), private_key, require_private_key))
    return accounts


def flatten_accounts(accounts, require_private_key=True):
    address_list = []
    for account in accounts:
        address_list.append(account["address"])
        private_key = account.get("private_key")
        if require_private_key and not private_key:
            raise ValueError("account entry for %s is missing private_key" % account["address"])
        address_list.append(normalize_private_key(private_key))
    return address_list


def load_address_list(default_address_list, env_var=ACCOUNTS_FILE_ENV):
    filename = os.getenv(env_var)
    if not filename:
        if not default_address_list:
            raise ValueError("%s is not set and no default ppk.py account list is available" % env_var)
        return list(default_address_list)

    accounts = load_accounts_file(filename, require_private_key=True)
    return flatten_accounts(accounts, require_private_key=True)
