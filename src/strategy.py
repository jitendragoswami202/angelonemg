import logging

class TradingStrategy:
    def __init__(self, profit_target=0.01, max_loss=0.02):
        self.profit_target = profit_target  # 1% profit per trade
        self.max_loss = max_loss  # 2% maximum loss per trade

    def evaluate(self, market_data, traded_balance):
        try:
            bid_price = market_data.get('bid_price')
            ask_price = market_data.get('ask_price')

            if bid_price is None or ask_price is None:
                logging.warning('Missing bid or ask price from market data')
                return None

            spread = ask_price - bid_price

            # Smart Money Strategy Logic
            potential_profit = spread / ask_price

            if potential_profit >= self.profit_target:
                logging.info(f'Buy Signal - Potential Profit: {potential_profit * 100:.2f}%')
                return 'BUY'

            potential_loss = spread / bid_price

            if potential_loss >= self.max_loss:
                logging.info(f'Sell Signal - Potential Loss: {potential_loss * 100:.2f}%')
                return 'SELL'

            return None
        except Exception as e:
            logging.error(f'Error in strategy evaluation: {str(e)}')
            return None
          
