import os
import websocket
import json
import threading
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
CLIENT_ID = os.getenv('CLIENT_ID')
ACCESS_TOKEN = os.getenv('REFRESH_TOKEN')
WEBSOCKET_URL = os.getenv('WEBSOCKET_URL')

class WebSocketClient:
    def __init__(self, url=WEBSOCKET_URL):
        self.url = url
        self.ws = None
        self.subscribed_channels = []

    def on_open(self, ws):
        print("✅ WebSocket connection established")
        self.authenticate()

    def on_message(self, ws, message):
        data = json.loads(message)
        print(f"📥 Received Message: {data}")
        
    def on_error(self, ws, error):
        print(f"❌ WebSocket Error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        print("❌ WebSocket connection closed")

    def authenticate(self):
        auth_payload = {
            "action": "authenticate",
            "api_key": API_KEY,
            "client_id": CLIENT_ID,
            "access_token": ACCESS_TOKEN
        }
        self.send(auth_payload)
        
    def subscribe(self, channels):
        for channel in channels:
            self.subscribed_channels.append(channel)
            subscribe_payload = {
                "action": "subscribe",
                "channel": channel
            }
            self.send(subscribe_payload)
        
    def send(self, payload):
        if self.ws:
            self.ws.send(json.dumps(payload))
        else:
            print("❌ WebSocket is not connected")

    def connect(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self.thread = threading.Thread(target=self.ws.run_forever)
        self.thread.start()

    def close(self):
        if self.ws:
            self.ws.close()
