# websocket_client.py

import websocket
import json
import threading
import time
from utils import log_message
from dotenv import load_dotenv
import os

load_dotenv()

class WebSocketClient:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.access_token = os.getenv("ACCESS_TOKEN")
        self.ws_url = os.getenv("WEBSOCKET_URL")  # Replace with Angel One WebSocket URL
        self.ws = None
        self.connected = False

    def on_message(self, ws, message):
        data = json.loads(message)
        log_message(f"Message received: {data}")
        # Handle incoming messages here (e.g., market data, order updates)

    def on_error(self, ws, error):
        log_message(f"WebSocket error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        log_message(f"WebSocket closed: {close_status_code} - {close_msg}")
        self.connected = False

    def on_open(self, ws):
        log_message("WebSocket connection established")
        self.connected = True
        # Subscribe to relevant channels (e.g., market data, order status, account info)
        subscription_message = json.dumps({
            "action": "subscribe",
            "channels": ["market-data", "order-status", "account-info"]
        })
        ws.send(subscription_message)

    def connect(self):
        self.ws = websocket.WebSocketApp(
            self.ws_url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )

        threading.Thread(target=self.ws.run_forever).start()

        while not self.connected:
            time.sleep(0.1)

    def disconnect(self):
        if self.ws:
            self.ws.close()
            self.connected = False


if __name__ == "__main__":
    client = WebSocketClient()
    client.connect()
    time.sleep(5)  # Keep the connection alive for testing
    client.disconnect()
