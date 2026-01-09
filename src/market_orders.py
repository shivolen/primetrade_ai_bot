import sys
import time
import hmac
import hashlib
import requests
import logging
import os
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://testnet.binancefuture.com"

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def sign(params):
    query = urlencode(params)
    signature = hmac.new(
        API_SECRET.encode(),
        query.encode(),
        hashlib.sha256
    ).hexdigest()
    return query + "&signature=" + signature

def main():
    try:
        symbol = sys.argv[1]
        side = sys.argv[2]
        quantity = sys.argv[3]

        if side not in ["BUY", "SELL"]:
            raise ValueError("Side must be BUY or SELL")

        timestamp = int(time.time() * 1000)

        params = {
            "symbol": symbol,
            "side": side,
            "type": "MARKET",
            "quantity": quantity,
            "timestamp": timestamp
        }

        signed_query = sign(params)

        headers = {
            "X-MBX-APIKEY": API_KEY
        }

        url = BASE_URL + "/fapi/v1/order"

        response = requests.post(url, headers=headers, params=signed_query)

        logging.info(f"REST market order response: {response.text}")

        print("RAW RESPONSE ↓")
        print(response.text)

    except Exception as e:
        logging.exception("Market order failed")
        print("ERROR:", e)

if __name__ == "__main__":
    main()
