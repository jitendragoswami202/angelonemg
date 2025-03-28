import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class RiskManager:
    def __init__(self, max_risk_per_trade=0.01, max_positions=5):
        self.max_risk_per_trade = max_risk_per_trade  # Maximum risk per trade as a percentage of capital
        self.max_positions = max_positions  # Maximum number of open positions allowed
        self.open_positions = 0

    def can_place_trade(self, capital, risk_amount):
        try:
            logging.info('Checking if a new trade can be placed...')

            if self.open_positions >= self.max_positions:
                logging.warning('Max open positions limit reached. Cannot place more trades.')
                return False

            risk_per_trade = capital * self.max_risk_per_trade

            if risk_amount > risk_per_trade:
                logging.warning(f'Trade risk ({risk_amount}) exceeds allowed risk per trade ({risk_per_trade}).')
                return False

            logging.info('Trade can be placed.')
            return True
        except Exception as e:
            logging.error(f'Error in risk management: {str(e)}')
            return False

    def update_position(self, action):
        if action == 'BUY':
            self.open_positions += 1
            logging.info(f'Position opened. Total open positions: {self.open_positions}')
        elif action == 'SELL' and self.open_positions > 0:
            self.open_positions -= 1
            logging.info(f'Position closed. Total open positions: {self.open_positions}')
        else:
            logging.warning('Invalid action or no positions to close.')


if __name__ == "__main__":
    risk_manager = RiskManager()
    capital = 100000  # Example capital
    risk_amount = 500  # Example risk amount per trade

    if risk_manager.can_place_trade(capital, risk_amount):
        risk_manager.update_position('BUY')
    risk_manager.update_position('SELL')
    
