import websocket
import threading
import json
import time
from utils import get_token  # assume this gets your access token
from strategy import on_market_data  # callback to process market data

class AngelWebSocketManager:
    def __init__(self, feed_token, client_code):
        self.feed_token = feed_token
        self.client_code = client_code
        self.ws_url = "wss://ws.angelbroking.com/NestHtml5Mobile/socket/stream"
        self.ws = None
        self.subscribed_tokens = set()
        self.is_connected = False

    def _on_open(self, ws):
        print("WebSocket connected.")
        self.is_connected = True
        for token in self.subscribed_tokens:
            self.subscribe(token)

    def _on_message(self, ws, message):
        try:
            data = json.loads(message)
            if data.get('t') == 'tk':
                market_data = self._parse_data(data)
                on_market_data(market_data)
        except Exception as e:
            print(f"WebSocket message error: {e}")

    def _on_error(self, ws, error):
        print(f"WebSocket error: {error}")

    def _on_close(self, ws, *args):
        print("WebSocket closed.")
        self.is_connected = False
        time.sleep(2)
        self.connect()  # Reconnect

    def _parse_data(self, data):
        # Modify this function based on actual Angel One data format
        return {
            "symbol": data.get("tk"),
            "ltp": float(data.get("lp", 0)),
            "ask": float(data.get("ap", 0)),
            "bid": float(data.get("bp", 0)),
            "timestamp": time.time()
        }

    def connect(self):
        headers = {
            "Authorization": f"Bearer {self.feed_token}"
        }
        self.ws = websocket.WebSocketApp(
            self.ws_url,
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close,
            header=headers
        )
        wst = threading.Thread(target=self.ws.run_forever, daemon=True)
        wst.start()

    def subscribe(self, token):
        self.subscribed_tokens.add(token)
        if self.is_connected:
            payload = {
                "task": "mw",  # Market Watch
                "channel": f"nse_cm|{token}",
                "token": self.feed_token,
                "user": self.client_code,
                "acctid": self.client_code
            }
            self.ws.send(json.dumps(payload))

    def unsubscribe(self, token):
        if token in self.subscribed_tokens:
            self.subscribed_tokens.remove(token)
            if self.is_connected:
                payload = {
                    "task": "ud",
                    "channel": f"nse_cm|{token}",
                    "token": self.feed_token,
                    "user": self.client_code,
                    "acctid": self.client_code
                }
                self.ws.send(json.dumps(payload))
