from web3 import Web3
from typing import Optional
from hexbytes import HexBytes

from config import PRIVATE_KEY


binance_testnet_rpc_url = "https://data-seed-prebsc-1-s1.binance.org:8545/"
web3 = Web3(Web3.HTTPProvider(binance_testnet_rpc_url))
print(f"Is connected: {web3.is_connected()}")  # Is connected: True


def get_balance(wallet_address):
    checksum_address = web3.to_checksum_address(wallet_address)
    balance = web3.eth.get_balance(checksum_address)
    balance_bnb = web3.from_wei(balance, 'ether')
    return balance_bnb


def build_txn(web3: Web3, from_address, to_address, amount):
    gas_price = web3.eth.gas_price
    gas = 2_000_000

    nonce = web3.eth.get_transaction_count(from_address)

    txn = {
        'chainId': web3.eth.chain_id,
        'from': from_address,
        'to': to_address,
        'value': int(web3.to_wei(amount, 'ether')),
        'nonce': nonce,
        'gasPrice': gas_price,
        'gas': gas
    }

    return txn


my_address = '0x4634A49eF99bb6e548253386aA2e9802c1478cdc'
to_address = '0x8F21eCD6E0F6857C0CF78f3Ac72c3088dEC929dB'

transaction = build_txn(
    web3=web3,
    from_address=my_address,
    to_address=to_address,
    amount=0.03
)

signed_txn = web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)

txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

print(txn_hash.hex())
print(get_balance(my_address))