# websocket_client.py - Handles real-time market data streaming

import websocket
import json
from config import API_KEY, CLIENT_ID, WEBSOCKET_URL
from auth import generate_token

# Generate authentication token
TOKEN = generate_token()

def on_message(ws, message):
    """Handles incoming WebSocket messages (market data)."""
    data = json.loads(message)
    print("📊 Live Data:", data)

def on_error(ws, error):
    """Handles WebSocket errors."""
    print("❌ WebSocket Error:", error)

def on_close(ws, close_status_code, close_msg):
    """Handles WebSocket disconnection."""
    print("🔴 WebSocket Disconnected")

def on_open(ws):
    """Sends subscription request when WebSocket opens."""
    print("🟢 WebSocket Connected! Subscribing to live market data...")

    # Replace with actual instrument tokens (e.g., NIFTY options, stocks)
    instrument_tokens = ["26009", "26017"]  # Example token for NIFTY
    payload = {
        "action": "subscribe",
        "token": TOKEN,
        "instrument_tokens": instrument_tokens,
    }
    
    ws.send(json.dumps(payload))

def start_websocket():
    """Initializes WebSocket connection."""
    ws = websocket.WebSocketApp(
        WEBSOCKET_URL,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.on_open = on_open
    ws.run_forever()

if __name__ == "__main__":
    start_websocket()
