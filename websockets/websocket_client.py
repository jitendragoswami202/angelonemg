import asyncio
import websockets
import json
import os
from dotenv import load_dotenv

load_dotenv()

class WebSocketClient:
    def __init__(self):
        self.ws_url = os.getenv("ANGEL_ONE_WS_URL")
        self.api_key = os.getenv("API_KEY")
        self.access_token = os.getenv("ACCESS_TOKEN")
        self.market_data = {}

    async def connect(self):
        async with websockets.connect(self.ws_url) as websocket:
            await self.authenticate(websocket)
            await self.subscribe_to_market_data(websocket)
            await self.receive_messages(websocket)

    async def authenticate(self, websocket):
        auth_data = {
            "action": "authenticate",
            "api_key": self.api_key,
            "access_token": self.access_token
        }
        await websocket.send(json.dumps(auth_data))
        response = await websocket.recv()
        print("Authentication Response:", response)

    async def subscribe_to_market_data(self, websocket):
        subscription_data = {
            "action": "subscribe",
            "channels": ["market-data", "order-status", "account-info"]
        }
        await websocket.send(json.dumps(subscription_data))

    async def receive_messages(self, websocket):
        async for message in websocket:
            data = json.loads(message)
            self.process_message(data)

    def process_message(self, data):
        if "symbol" in data and "last_price" in data:
            self.market_data[data["symbol"]] = data
        elif data.get("type") == "order-status":
            print("Order Status Update:", data)
        elif data.get("type") == "account-info":
            print("Account Info Update:", data)

    def start(self):
        asyncio.run(self.connect())
