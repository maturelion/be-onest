# from blockcypher import generate_new_address
from dotenv import load_dotenv
import requests
import json
import blockcypher
from users.models import User

import environ
load_dotenv()
env = environ.Env(DEBUG=(bool, False))


class BlockcypherWallet:
    def __init__(self):
        self.mode = "test" if env("DEBUG") == True else "main"
        self.coin = "bcy" if env("DEBUG") == True else "btc"
        self.api_key = env("BLOCKCYPHER_TOKEN")
        self.wallet_endpoint = "https://api.blockcypher.com/v1/"

    def create_wallet(self, user_id):
        url = f"{self.wallet_endpoint}{self.coin}/{self.mode}/wallets?token={self.api_key}"
        req = requests.post(url, json.dumps({"name": f"{user_id}"}))
        res = json.loads(req.content)
        return res

    def generate_wallet_address(self, user_id):
        url = f"{self.wallet_endpoint}{self.coin}/{self.mode}/wallets/{user_id}/addresses/generate?token={self.api_key}"
        req = requests.post(url)
        res = json.loads(req.content)
        return res
    
    def generate_address(self):
        url = f"{self.wallet_endpoint}{self.coin}/{self.mode}/addrs?token={self.api_key}"
        req = requests.post(url)
        res = json.loads(req.content)
        return res

    def get_wallet_address(self, user_id):
        url = f"{self.wallet_endpoint}/{self.coin}/{self.mode}/wallets/{user_id}/addresses?token={self.api_key}"
        req = requests.post(url)
        res = json.loads(req.content)
        return res

    def get_all_wallet_address(self):
        url = f"{self.wallet_endpoint}/{self.coin}/{self.mode}/wallets?token={self.api_key}"
        req = requests.post(url)
        res = json.loads(req.content)
        return res

    def delete_wallet_address(self, user_id, address):
        url = f"{self.wallet_endpoint}/{self.coin}/{self.mode}/wallets/{user_id}/addresses?token={self.api_key}&address={address}"
        req = requests.delete(url)
        res = req.status_code
        return res

    def delete_wallet(self, user_id):
        url = f"{self.wallet_endpoint}/{self.coin}/{self.mode}/wallets/{user_id}?token={self.api_key}"
        req = requests.delete(url)
        res = req.status_code
        return res

    def simple_spend(self, from_privkey, to_address, to_satoshis):
        simple_spend = blockcypher.simple_spend(
            api_key=self.api_key,
            from_privkey=from_privkey,
            to_address=to_address,
            to_satoshis=to_satoshis,
            coin_symbol=self.coin,
        )
        return simple_spend

    # Blockcypher paid plan only
    def create_forwarding_address_with_details(self, destination_address):
        create_forwarding_address_with_details = (
            blockcypher.create_forwarding_address_with_details(
                destination_address=destination_address,
                api_key=self.api_key,
                coin_symbol=self.coin,
            )
        )
        return create_forwarding_address_with_details

    def get_wallet_addresses(self, wallet_name):
        get_wallet_addresses = blockcypher.get_wallet_addresses(
            wallet_name=wallet_name,
            api_key=self.api_key,
            coin_symbol=self.coin,
        )
        return get_wallet_addresses

    def get_wallet_balance(self, wallet_name):
        get_wallet_balance = blockcypher.get_wallet_balance(
            wallet_name=wallet_name,
            api_key=self.api_key,
            coin_symbol=self.coin,
        )
        return get_wallet_balance

    def get_address_overview(self, address):
        get_address_overview = blockcypher.get_address_overview(
            address=address,
            api_key=self.api_key,
            coin_symbol=self.coin,
        )
        return get_address_overview

    def get_confirmed_balance(self, address):
        get_confirmed_balance = blockcypher.get_confirmed_balance(
            address=address,
            api_key=self.api_key,
            coin_symbol=self.coin,
        )
        return get_confirmed_balance

    def get_unconfirmed_balance(self, address):
        get_unconfirmed_balance = blockcypher.get_unconfirmed_balance(
            address=address,
            api_key=self.api_key,
            coin_symbol=self.coin,
        )
        return get_unconfirmed_balance

    def send_faucet_tx(self, address_to_fund, satoshi=1_000_000):
        faucet_tx = blockcypher.send_faucet_coins(
            address_to_fund,
            satoshis=satoshi,
            coin_symbol=self.coin,
            api_key=self.api_key,
        )
        return faucet_tx["tx_ref"]

    def deposit_webhook(self, subscription_address):
        webhook_id = blockcypher.subscribe_to_address_webhook(
            callback_url=f"{env('BASE_URL')}/deposit-webhook/",
            confirmations=int(env("HOOK_CONFIRMATIONS")),
            subscription_address=subscription_address,
            event="tx-confirmation",
            coin_symbol=self.coin,
            api_key=self.api_key,
        )
        return webhook_id

    def list_webhooks(self):
        return blockcypher.list_webhooks(
            api_key=self.api_key,
            coin_symbol=self.coin,
        )

    def get_webhook_info(self, webhook_id):
        return blockcypher.get_webhook_info(
            webhook_id,
            coin_symbol=self.coin,
            api_key=self.api_key,
        )

    def unsubscribe_from_webhook(self, webhook_id):
        return blockcypher.unsubscribe_from_webhook(
            webhook_id,
            api_key=self.api_key,
            coin_symbol=self.coin,
        )
