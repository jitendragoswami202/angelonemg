import time
from api import AngelOneAPI  # Ensure you have an API handler
from config import SYMBOL, EXCHANGE, QUANTITY, ORDER_TYPE  # Load configuration

api = AngelOneAPI()  # Initialize API

def get_market_data(symbol, exchange):
    """Fetches best bid and ask price."""
    market_data = api.get_ltp(symbol, exchange)
    best_bid = market_data.get('best_bid', market_data.get('ltp'))
    best_ask = market_data.get('best_ask', market_data.get('ltp'))
    return best_bid, best_ask

def place_order(price, order_type):
    """Places an order at a given price."""
    order_params = {
        "symbol": SYMBOL,
        "exchange": EXCHANGE,
        "quantity": QUANTITY,
        "order_type": ORDER_TYPE,
        "price": price
    }
    response = api.place_order(order_params)
    return response

def execute_trade():
    """Executes the trading strategy."""
    best_bid, best_ask = get_market_data(SYMBOL, EXCHANGE)

    if best_ask:  # Ensure ask price is available
        entry_price = best_ask  # Enter at the lowest ask price
        target_price = round(entry_price * 1.01, 2)  # 1% profit target
        stop_loss_price = round(entry_price * 0.995, 2)  # 0.5% stop loss

        print(f"Placing Entry Order at {entry_price}")
        entry_response = place_order(entry_price, "BUY")

        if entry_response.get("status") == "success":
            print(f"✅ Entry Order Placed at {entry_price}")

            # Monitor price to exit
            while True:
                current_bid, current_ask = get_market_data(SYMBOL, EXCHANGE)
                
                if current_bid and current_bid >= target_price:
                    print(f"🎯 Target Reached! Selling at {current_bid}")
                    exit_response = place_order(current_bid, "SELL")
                    break

                elif current_bid and current_bid <= stop_loss_price:
                    print(f"⛔ Stop Loss Hit! Selling at {current_bid}")
                    exit_response = place_order(current_bid, "SELL")
                    break
                
                time.sleep(1)  # Wait before next check
        else:
            print(f"❌ Order Placement Failed: {entry_response}")

if __name__ == "__main__":
    execute_trade()
