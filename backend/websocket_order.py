# websocket_order.py - Executes orders via WebSockets

import websocket
import json
from config import API_KEY, CLIENT_ID, WEBSOCKET_URL
from auth import generate_token

# Generate authentication token
TOKEN = generate_token()

def on_message(ws, message):
    """Handles WebSocket responses for order execution."""
    data = json.loads(message)
    print("📢 Order Update:", data)

def on_error(ws, error):
    """Handles WebSocket errors."""
    print("❌ WebSocket Error:", error)

def on_close(ws, close_status_code, close_msg):
    """Handles WebSocket disconnection."""
    print("🔴 WebSocket Disconnected")

def on_open(ws):
    """Places a sample order when WebSocket opens."""
    print("🟢 WebSocket Connected! Placing order...")

    order_payload = {
        "action": "place_order",
        "token": TOKEN,
        "order": {
            "symbol": "NIFTY",  # Change to the required stock or option
            "quantity": 50,
            "order_type": "LIMIT",  # Options: MARKET, LIMIT
            "price": 22000,  # Change as per strategy
            "transaction_type": "BUY",  # Options: BUY, SELL
            "product_type": "MIS",  # Options: MIS, CNC, NRML
            "validity": "DAY"
        }
    }

    ws.send(json.dumps(order_payload))

def start_websocket_order():
    """Initializes WebSocket connection for order execution."""
    ws = websocket.WebSocketApp(
        WEBSOCKET_URL,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.on_open = on_open
    ws.run_forever()

if __name__ == "__main__":
    start_websocket_order()
