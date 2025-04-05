import logging
from market_data import MarketDataFetcher
from strategy import TradingStrategy
from risk_manager import RiskManager
from order_manager import OrderManager
from position_tracker import PositionTracker
from log_manager import setup_logging


def main():
    setup_logging()

    logging.info('Starting the trading bot...')

    # Initialize components
    market_data_fetcher = MarketDataFetcher(api_key="YOUR_API_KEY", access_token="YOUR_ACCESS_TOKEN")
    strategy = TradingStrategy()
    risk_manager = RiskManager()
    order_manager = OrderManager(api_key="YOUR_API_KEY", access_token="YOUR_ACCESS_TOKEN")
    position_tracker = PositionTracker()

    capital = 100000  # Example capital
    symbol = 'RELIANCE'
    quantity = 1

    try:
        # Fetch market data
        market_data = market_data_fetcher.fetch_market_data(symbol)

        # Evaluate strategy
        action = strategy.evaluate(market_data)

        if action:
            risk_amount = 500  # Example risk amount per trade

            if risk_manager.can_place_trade(capital, risk_amount):
                order_id = order_manager.place_order(symbol, action, quantity, market_data['price'])

                if order_id:
                    position_tracker.update_position(symbol, action, quantity)

    except Exception as e:
        logging.error(f'Error in main execution: {str(e)}')


if __name__ == "__main__":
    main()
  
