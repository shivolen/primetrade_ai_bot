Binance Futures Trading Bot (USDT-M Testnet)

Overview
This project implements a CLI-based trading bot for Binance USDT-M Futures Testnet.
It supports core and advanced order types with validation and structured logging.

Supported Orders
- Market Orders
- Limit Orders
- Stop-Limit Orders (Advanced)

Technology
- Python
- Binance Futures REST API
- Testnet Environment

Setup
1. Create and activate a virtual environment
2. Install dependencies:
   pip install python-binance python-dotenv requests
3. Add API keys to a .env file:
   BINANCE_API_KEY=your_key
   BINANCE_API_SECRET=your_secret

Usage

Market Order:
python src/market_orders.py BTCUSDT BUY 0.003

Limit Order:
python src/limit_orders.py BTCUSDT SELL 0.003 90000

Stop-Limit Order:
python src/advanced/stop_limit.py BTCUSDT BUY 0.003 90000 88000

Logging
All API requests, responses, and errors are logged to bot.log.
