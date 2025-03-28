# risk_manager.py - Monitors risk, stop-loss, and profit-taking

import json
from order_manager import place_order, exit_order
from config import TRADING_CONFIG

# Initialize position tracking
positions = {}  # Stores current positions and P/L
daily_loss = 0

def update_positions(order_data):
    """Updates positions based on executed trades."""
    global daily_loss

    symbol = order_data["symbol"]
    price = float(order_data["price"])
    quantity = int(order_data["quantity"])
    transaction_type = order_data["transaction_type"]

    if transaction_type == "BUY":
        positions[symbol] = {"entry_price": price, "quantity": quantity}
    elif transaction_type == "SELL":
        if symbol in positions:
            entry_price = positions[symbol]["entry_price"]
            profit_loss = (price - entry_price) * quantity
            daily_loss += profit_loss

            print(f"📉 P/L for {symbol}: {profit_loss:.2f}")
            del positions[symbol]  # Remove position after exit

    # Check daily loss limit
    max_loss = TRADING_CONFIG["risk_percentage"] / 100 * 100000  # Example: 1% of 1L capital
    if daily_loss <= -max_loss:
        print("🚨 Max daily loss reached! Closing all positions...")
        close_all_positions()

def close_all_positions():
    """Closes all open positions when max loss is reached."""
    for symbol in list(positions.keys()):
        exit_order(symbol, positions[symbol]["quantity"])
        del positions[symbol]

def check_stop_loss():
    """Monitors stop-loss conditions and exits trades if triggered."""
    for symbol, pos in positions.items():
        current_price = get_live_price(symbol)
        entry_price = pos["entry_price"]
        stop_loss = entry_price * (1 - TRADING_CONFIG["stop_loss_percentage"] / 100)

        if current_price <= stop_loss:
            print(f"🚨 Stop-loss triggered for {symbol} at {current_price}")
            exit_order(symbol, pos["quantity"])
            del positions[symbol]

def get_live_price(symbol):
    """Fetches live price (dummy function, integrate with WebSocket data)."""
    return 22000  # Example: Replace with actual live price fetching logic
