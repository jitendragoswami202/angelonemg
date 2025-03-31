import os
import time
import requests
import json
import websocket
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
API_KEY = os.getenv("API_KEY")
REDIRECT_URL = os.getenv("REDIRECT_URL")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
WEBSOCKET_URL = os.getenv("WEBSOCKET_URL")

# Generate Access Token using Refresh Token
def generate_access_token():
    url = "https://api.angelone.in/oauth/token"
    headers = {
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
        "redirect_uri": REDIRECT_URL
    })

    response = requests.post(url, headers=headers, data=payload)
    data = response.json()

    if response.status_code == 200 and "access_token" in data:
        access_token = data["access_token"]
        print("✅ Access Token Generated Successfully")
        return access_token
    else:
        print("❌ Failed to generate access token:", data)
        return None

# WebSocket Connection
def on_message(ws, message):
    data = json.loads(message)
    print(f"📥 Message Received: {data}")

def on_error(ws, error):
    print(f"❌ WebSocket Error: {error}")

def on_close(ws):
    print("🔌 WebSocket Connection Closed")

def on_open(ws):
    print("🌐 WebSocket Connection Established")
    # Subscribe to market data, positions, orders
    ws.send(json.dumps({
        "action": "subscribe",
        "channels": ["market-data", "order-status", "account-info"]
    }))

def connect_websocket(access_token):
    websocket_url = f"{WEBSOCKET_URL}?access_token={access_token}"
    ws = websocket.WebSocketApp(websocket_url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()

# Execute Buy Order
def place_order(access_token, symbol, qty, order_type="MARKET", transaction_type="BUY"):
    url = "https://api.angelone.in/orders"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    payload = json.dumps({
        "symbol": symbol,
        "quantity": qty,
        "order_type": order_type,
        "transaction_type": transaction_type,
        "product": "INTRADAY",
        "variety": "NORMAL",
    })

    response = requests.post(url, headers=headers, data=payload)
    data = response.json()

    if response.status_code == 200:
        print(f"✅ Order Placed Successfully: {data}")
    else:
        print(f"❌ Order Placement Failed: {data}")

# Main Execution
if __name__ == "__main__":
    # Generate Access Token
    access_token = generate_access_token()

    if access_token:
        # Connect to WebSocket
        connect_websocket(access_token)

        # Example: Place an order (You can replace with your strategy logic)
        place_order(access_token, "NIFTY23MAYFUT", qty=1)
