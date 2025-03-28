import logging
from order_manager import OrderManager
from strategy import TradingStrategy
from market_data import MarketDataFetcher

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class TradingBot:
    def __init__(self, api_key, api_secret, access_token):
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = access_token
        self.market_data = MarketDataFetcher()
        self.strategy = TradingStrategy()
        self.order_manager = OrderManager(api_key, api_secret, access_token)

    def run(self):
        logging.info('Starting trading bot...')
        try:
            while True:  # Main bot loop
                market_data = self.market_data.fetch_data()
                signals = self.strategy.generate_signals(market_data)

                for signal in signals:
                    if signal['action'] == 'BUY':
                        self.order_manager.place_order(signal['symbol'], 'BUY', signal['quantity'])
                    elif signal['action'] == 'SELL':
                        self.order_manager.place_order(signal['symbol'], 'SELL', signal['quantity'])

        except KeyboardInterrupt:
            logging.info('Bot stopped by user.')
        except Exception as e:
            logging.error(f'Unexpected error: {str(e)}')


if __name__ == "__main__":
    bot = TradingBot(api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET", access_token="YOUR_ACCESS_TOKEN")
    bot.run()
    
