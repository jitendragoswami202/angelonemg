import os
import websocket
import json
from dotenv import load_dotenv

load_dotenv()

class WebSocketClient:
    def __init__(self, on_message, on_error, on_close):
        self.auth_token = os.getenv('AUTH_TOKEN')
        self.api_key = os.getenv('API_KEY')
        self.url = f"wss://smartapi.angelbroking.com/ws?jwtToken={self.auth_token}&clientcode={self.api_key}"
        self.ws = websocket.WebSocketApp(self.url, 
                                         on_message=on_message,
                                         on_error=on_error,
                                         on_close=on_close)

    def start(self):
        self.ws.run_forever()


def on_message(ws, message):
    data = json.loads(message)
    print('Received message:', data)


def on_error(ws, error):
    print('WebSocket Error:', error)


def on_close(ws):
    print('WebSocket Closed')


if __name__ == "__main__":
    client = WebSocketClient(on_message, on_error, on_close)
    client.start()
