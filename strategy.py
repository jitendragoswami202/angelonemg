import time
import logging
from angel_one_api import AngelOneAPI  # Angel One API integration

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Angel One API connection
api = AngelOneAPI()

# **Auto Settings**
SYMBOL = "NIFTY 27 Mar 24100 Call"  # Change this as per your requirement
EXCHANGE = "NSE"  # Choose from NSE, BSE, MCX
ORDER_TYPE = "LIMIT"
TRADE_PERCENTAGE = 0.2  # Allocate 20% of available balance for trade

def get_bid_ask(symbol):
    """ Fetch live Bid-Ask price from API """
    try:
        market_data = api.get_market_data(symbol)
        best_bid = market_data['best_bid']  # Highest buyer price
        best_ask = market_data['best_ask']  # Lowest seller price
        return best_bid, best_ask
    except Exception as e:
        logging.error(f"❌ Error fetching market data: {e}")
        return None, None

def get_available_balance():
    """ Fetch available funds from API """
    try:
        balance = api.get_funds()
        return balance['available_margin']
    except Exception as e:
        logging.error(f"❌ Error fetching balance: {e}")
        return None

def place_limit_order(symbol, price, quantity, order_type, exchange, transaction_type):
    """ Place a limit order """
    try:
        order_id = api.place_order(
            symbol=symbol,
            price=price,
            quantity=quantity,
            order_type=order_type,
            exchange=exchange,
            transaction_type=transaction_type
        )
        logging.info(f"✅ {transaction_type} Order Placed at {price} | Order ID: {order_id}")
        return order_id
    except Exception as e:
        logging.error(f"❌ Error placing order: {e}")
        return None

def bid_ask_spread_strategy():
    """ Enter at Lowest Ask Price, Exit at 1% Target or Max Possible Price """

    # **Auto Calculate Quantity**
    available_balance = get_available_balance()
    if not available_balance:
        logging.error("❌ Could not fetch available balance!")
        return
    
    best_bid, best_ask = get_bid_ask(SYMBOL)
    if not best_ask:
        logging.error("❌ No valid Ask price found, retrying...")
        return
    
    entry_price = best_ask  # **Enter at Lowest Ask Price**
    max_allocated_amount = available_balance * TRADE_PERCENTAGE
    quantity = int(max_allocated_amount // entry_price)  # **Auto Quantity Calculation**

    if quantity <= 0:
        logging.error("❌ Insufficient balance for trade!")
        return

    target_price = round(entry_price * 1.01, 2)  # **1% Target Profit**
    stop_loss_price = round(entry_price * 0.995, 2)  # **0.5% Stop Loss**

    logging.info(f"🚀 Trading {SYMBOL} on {EXCHANGE} | Quantity: {quantity}")
    logging.info(f"📊 Entry Price: {entry_price}, Target: {target_price}, Stop Loss: {stop_loss_price}")

    # **Place Limit Order at Best Ask Price**
    order_id = place_limit_order(SYMBOL, entry_price, quantity, ORDER_TYPE, EXCHANGE, "BUY")
    if not order_id:
        logging.error("❌ Entry Order Failed!")
        return

    # **Monitor Price Movements for Best Exit**
    max_price_seen = entry_price
    while True:
        time.sleep(2)  # **Reduce API load with a 2-second delay**
        best_bid, best_ask = get_bid_ask(SYMBOL)

        # **Track Maximum Price**
        if best_bid > max_price_seen:
            max_price_seen = best_bid
        
        # **Exit at Target Price or Max Possible Price**
        if best_bid >= target_price:
            logging.info("🎯 Target Hit! Placing Sell Order...")
            place_limit_order(SYMBOL, target_price, quantity, ORDER_TYPE, EXCHANGE, "SELL")
            break

        # **Stop Loss Condition**
        if best_bid <= stop_loss_price:
            logging.warning("⛔ Stop Loss Hit! Placing Sell Order...")
            place_limit_order(SYMBOL, stop_loss_price, quantity, ORDER_TYPE, EXCHANGE, "SELL")
            break

        # **Exit if Price Starts Dropping from Peak**
        if max_price_seen > best_bid * 1.005:  # If price drops 0.5% from peak
            logging.warning("📉 Price Dropped from Peak! Exiting...")
            place_limit_order(SYMBOL, best_bid, quantity, ORDER_TYPE, EXCHANGE, "SELL")
            break

# **Run the Strategy**
bid_ask_spread_strategy()
