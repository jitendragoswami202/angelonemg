# enhanced_market_making_strategy.py

import time
import numpy as np
from datetime import datetime
from websocket_manager import WebSocketManager  # Assuming you have websocket_manager.py set up
from trade_executor import TradeExecutor  # Assuming you have trade_executor.py set up
from utils import log_message  # Assuming you have a logging utility

class EnhancedMarketMaker:
    def __init__(self, executor, symbol, spread=0.01, max_drawdown=5, max_position_size=100, hedge=True):
        self.executor = executor
        self.symbol = symbol
        self.spread = spread  # Initial spread percentage
        self.max_drawdown = max_drawdown
        self.max_position_size = max_position_size
        self.hedge = hedge
        self.inventory = 0
        self.open_orders = {}
        self.trade_frequency = 5  # Target: 5 trades per second

    def calculate_dynamic_spread(self, volatility):
        # Increase spread during high volatility to reduce risk
        return self.spread * (1 + volatility)

    def manage_inventory(self):
        # Prevent excessive long or short positions
        if self.inventory > self.max_position_size:
            self.executor.place_order(self.symbol, 'sell', 'market', abs(self.inventory))
            self.inventory = 0
        elif self.inventory < -self.max_position_size:
            self.executor.place_order(self.symbol, 'buy', 'market', abs(self.inventory))
            self.inventory = 0

    def cancel_stale_orders(self):
        # Cancel orders that are too old
        now = datetime.now()
        stale_orders = [order_id for order_id, order in self.open_orders.items() if (now - order['timestamp']).seconds > 5]
        for order_id in stale_orders:
            self.executor.cancel_order(order_id)
            del self.open_orders[order_id]

    def place_market_making_orders(self, market_price, volatility):
        dynamic_spread = self.calculate_dynamic_spread(volatility)
        bid_price = market_price * (1 - dynamic_spread)
        ask_price = market_price * (1 + dynamic_spread)

        bid_order_id = self.executor.place_order(self.symbol, 'buy', 'limit', 1, price=bid_price)
        ask_order_id = self.executor.place_order(self.symbol, 'sell', 'limit', 1, price=ask_price)

        self.open_orders[bid_order_id] = {'type': 'buy', 'timestamp': datetime.now()}
        self.open_orders[ask_order_id] = {'type': 'sell', 'timestamp': datetime.now()}

    def run(self):
        while True:
            try:
                market_price, volatility = self.executor.get_market_data(self.symbol)
                self.place_market_making_orders(market_price, volatility)
                self.cancel_stale_orders()
                self.manage_inventory()
                time.sleep(1 / self.trade_frequency)
            except Exception as e:
                log_message(f"Error: {str(e)}")


if __name__ == "__main__":
    executor = TradeExecutor()  # Replace with your actual executor instance
    market_maker = EnhancedMarketMaker(executor, symbol="NIFTY")
    market_maker.run()
