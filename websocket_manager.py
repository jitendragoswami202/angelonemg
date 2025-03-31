# websocket_manager.py

import websocket
import json
import threading
import time
from utils import log_message

class WebSocketManager:
    def __init__(self, url, symbols):
        self.url = url
        self.symbols = symbols
        self.ws = None
        self.callbacks = {}
        self.is_running = False

    def on_message(self, ws, message):
        try:
            data = json.loads(message)
            if 'symbol' in data and data['symbol'] in self.callbacks:
                self.callbacks[data['symbol']](data)
        except Exception as e:
            log_message(f"Error processing message: {str(e)}")

    def on_error(self, ws, error):
        log_message(f"WebSocket Error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        log_message("WebSocket closed")

    def on_open(self, ws):
        log_message("WebSocket connection established")
        for symbol in self.symbols:
            self.subscribe(symbol)

    def subscribe(self, symbol):
        if self.ws:
            request = json.dumps({
                "action": "subscribe",
                "symbol": symbol
            })
            self.ws.send(request)

    def set_callback(self, symbol, callback):
        self.callbacks[symbol] = callback

    def connect(self):
        self.is_running = True
        self.ws = websocket.WebSocketApp(self.url,
                                         on_open=self.on_open,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)

        self.thread = threading.Thread(target=self.ws.run_forever)
        self.thread.start()

    def disconnect(self):
        self.is_running = False
        if self.ws:
            self.ws.close()
        if self.thread:
            self.thread.join()

if __name__ == "__main__":
    ws_manager = WebSocketManager("wss://your-angel-one-websocket-url", ["NIFTY"])
    ws_manager.connect()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        ws_manager.disconnect()
