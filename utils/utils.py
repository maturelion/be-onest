import requests
import json


def get_ticker_price(symbol="BTCUSDT"):
    ticker = requests.get(
        f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    )
    price = json.loads(ticker.text)['price']
    symbol = json.loads(ticker.text)['symbol']
    return {"price": price, "symbol": symbol}
