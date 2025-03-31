import asyncio
import json
import os
import websockets
from dotenv import load_dotenv

load_dotenv()

class TradeExecutor:
    def __init__(self):
        self.ws_url = os.getenv("ANGEL_ONE_WS_URL")
        self.api_key = os.getenv("API_KEY")
        self.access_token = os.getenv("ACCESS_TOKEN")

    async def execute_order(self, order_type, symbol, price, quantity):
        async with websockets.connect(self.ws_url) as websocket:
            await self.authenticate(websocket)
            order_request = {
                "action": "place_order",
                "order_type": order_type,
                "symbol": symbol,
                "price": price,
                "quantity": quantity
            }
            await websocket.send(json.dumps(order_request))
            response = await websocket.recv()
            return json.loads(response)

    async def authenticate(self, websocket):
        auth_data = {
            "action": "authenticate",
            "api_key": self.api_key,
            "access_token": self.access_token
        }
        await websocket.send(json.dumps(auth_data))
        response = await websocket.recv()
        print("Authentication Response:", response)
