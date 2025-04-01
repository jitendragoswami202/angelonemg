# websocket_client.py - WebSocket Communication
import websocket
import json
import threading
import time
from auth import Auth
from dotenv import load_dotenv
import os

load_dotenv()

WEBSOCKET_URL = os.getenv('WEBSOCKET_URL')

class WebSocketClient:
    def __init__(self):
        self.auth = Auth()
        self.auth.load_tokens()
        self.access_token = self.auth.access_token
        self.ws = None
        self.connected = False

    def on_message(self, ws, message):
        data = json.loads(message)
        print(f"Received Message: {data}")

    def on_error(self, ws, error):
        print(f"WebSocket Error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        print("WebSocket Closed")
        self.connected = False

    def on_open(self, ws):
        print("WebSocket Connection Established")
        self.connected = True

        # Example subscription message
        subscribe_message = {
            "action": "subscribe",
            "key": self.access_token,
            "feed": "nse_cm"
        }

        self.ws.send(json.dumps(subscribe_message))

    def connect(self):
        self.ws = websocket.WebSocketApp(
            WEBSOCKET_URL,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            header={"Authorization": f"Bearer {self.access_token}"}
        )

        self.ws.run_forever()

    def start(self):
        threading.Thread(target=self.connect).start()

    def stop(self):
        if self.ws:
            self.ws.close()

if __name__ == "__main__":
    client = WebSocketClient()
    client.start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            client.stop()
            break
