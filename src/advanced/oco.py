import logging
import os
from binance import Client
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def get_client():
    client = Client(
        os.getenv("BINANCE_API_KEY"),
        os.getenv("BINANCE_API_SECRET")
    )
    client.FUTURES_URL = "https://testnet.binancefuture.com"
    return client
