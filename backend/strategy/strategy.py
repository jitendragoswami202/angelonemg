# strategy.py - Smart Money Strategy Implementation
import logging
from trade_executor import TradeExecutor
from websocket_client import WebSocketClient
import threading
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Strategy:
    def __init__(self):
        self.executor = TradeExecutor()
        self.ws_client = WebSocketClient()
        self.trade_threshold = 0.01  # Target profit of 1%
        self.max_loss = 0.02  # Maximum loss of 2%
        self.position = None
        self.last_price = None
        self.balance = 100000  # Initial trading balance

    def on_market_data(self, data):
        symbol = data.get('symbol')
        price = float(data.get('price'))

        if self.position is None:
            if self.last_price and (price - self.last_price) / self.last_price >= self.trade_threshold:
                self.open_position(symbol, price)
        else:
            if (self.position['type'] == 'BUY' and (price - self.position['entry_price']) / self.position['entry_price'] >= self.trade_threshold) or \
               (self.position['type'] == 'SELL' and (self.position['entry_price'] - price) / self.position['entry_price'] >= self.trade_threshold):
                self.close_position(symbol, price)

            if (self.position['type'] == 'BUY' and (self.position['entry_price'] - price) / self.position['entry_price'] >= self.max_loss) or \
               (self.position['type'] == 'SELL' and (price - self.position['entry_price']) / self.position['entry_price'] >= self.max_loss):
                self.close_position(symbol, price, stop_loss=True)

        self.last_price = price

    def open_position(self, symbol, price):
        self.position = {
            'symbol': symbol,
            'entry_price': price,
            'type': 'BUY',
            'quantity': 1
        }
        logging.info(f"Opening Position: {self.position}")
        self.executor.execute_trade(symbol, 1, 'BUY')

    def close_position(self, symbol, price, stop_loss=False):
        logging.info(f"Closing Position at {price} - {'Stop Loss Triggered' if stop_loss else 'Target Achieved'}")
        self.executor.execute_trade(symbol, 1, 'SELL')
        self.position = None

    def start(self):
        threading.Thread(target=self.ws_client.start).start()
        self.ws_client.ws.on_message = lambda ws, message: self.on_market_data(message)

if __name__ == "__main__":
    strategy = Strategy()
    strategy.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Strategy Stopped")
