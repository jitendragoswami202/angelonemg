import logging
from execution import api

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

import os
SYMBOL = os.getenv("SYMBOL", "BANKNIFTY")  
EXCHANGE = os.getenv("EXCHANGE", "NSE")
ORDER_TYPE = "LIMIT"
TRADE_PERCENTAGE = 0.8  

def get_bid_ask(symbol):
    bid, ask = api.get_market_data(symbol, EXCHANGE)
    return bid, ask

def check_exit_conditions(current_price, entry_price):
    stop_loss = entry_price * 0.995  
    target_profit = entry_price * 1.01  
    return current_price <= stop_loss or current_price >= target_profit
