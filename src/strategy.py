import json
import os
import asyncio
import time
from websocket_client import WebSocketClient
from trade_executor import TradeExecutor
from dotenv import load_dotenv

load_dotenv()

class MarketMakingStrategy:
    def __init__(self):
        self.client = WebSocketClient()
        self.executor = TradeExecutor()
        self.symbol = os.getenv("SYMBOL", "NIFTY")  # Replace with your option symbol
        self.spread = float(os.getenv("SPREAD", 0.1))  # Spread in percentage
        self.quote_size = int(os.getenv("QUOTE_SIZE", 1))  # Number of contracts per quote
        self.inventory_limit = int(os.getenv("INVENTORY_LIMIT", 10))  # Max allowed position size
        self.active_orders = {}
        self.position = 0

    def calculate_quotes(self, last_price):
        """Calculate bid and ask prices based on the last traded price."""
        bid_price = last_price * (1 - self.spread / 100)
        ask_price = last_price * (1 + self.spread / 100)
        return bid_price, ask_price

    async def place_order(self, order_type, symbol, price):
        """Place a limit order via the trade executor asynchronously."""
        order_response = await self.executor.execute_order(order_type, symbol, price, self.quote_size)
        if order_response.get("status") == "success":
            order_id = order_response.get("order_id")
            self.active_orders[order_id] = {
                "symbol": symbol,
                "price": price,
                "order_type": order_type,
                "quantity": self.quote_size
            }
            print(f"Order Placed: {order_type} {symbol} at {price}")
        else:
            print(f"Order Failed: {order_response.get('error')}")

    def manage_inventory(self):
        """Adjust quotes if position exceeds inventory limit."""
        if abs(self.position) >= self.inventory_limit:
            print("Inventory limit reached. Adjusting quotes to reduce exposure.")
            if self.position > 0:
                self.spread += 0.05  # Increase spread for selling
            elif self.position < 0:
                self.spread += 0.05  # Increase spread for buying
        else:
            self.spread = float(os.getenv("SPREAD", 0.1))

    async def evaluate_market_data(self, data):
        """Evaluate real-time market data and adjust orders."""
        symbol = data.get("symbol")
        last_price = data.get("last_price")

        if symbol == self.symbol and last_price:
            bid_price, ask_price = self.calculate_quotes(last_price)

            # Place both buy and sell orders asynchronously
            await asyncio.gather(
                self.place_order("BUY", symbol, bid_price),
                self.place_order("SELL", symbol, ask_price)
            )

            # Inventory management
            self.manage_inventory()

    async def run(self):
        self.client.start()
        while True:
            tasks = []
            for symbol, data in self.client.market_data.items():
                tasks.append(self.evaluate_market_data(data))
            
            if tasks:
                await asyncio.gather(*tasks)
            
            await asyncio.sleep(0.2)  # Aim for 5 trades per second (1 / 0.2 = 5)

if __name__ == "__main__":
    strategy = MarketMakingStrategy()
    asyncio.run(strategy.run())
