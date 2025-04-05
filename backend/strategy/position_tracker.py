import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class PositionTracker:
    def __init__(self):
        self.positions = {}

    def update_position(self, symbol, action, quantity):
        try:
            logging.info(f'Updating position for {symbol} - Action: {action} - Quantity: {quantity}')

            if action == 'BUY':
                if symbol in self.positions:
                    self.positions[symbol] += quantity
                else:
                    self.positions[symbol] = quantity

            elif action == 'SELL':
                if symbol in self.positions:
                    self.positions[symbol] -= quantity
                    if self.positions[symbol] <= 0:
                        del self.positions[symbol]
                else:
                    logging.warning(f'Sell action received for non-existing position: {symbol}')
            else:
                logging.warning(f'Invalid action: {action}')

            logging.info(f'Updated Positions: {self.positions}')

        except Exception as e:
            logging.error(f'Error updating position: {str(e)}')

    def get_positions(self):
        return self.positions


if __name__ == "__main__":
    tracker = PositionTracker()
    tracker.update_position('RELIANCE', 'BUY', 10)
    tracker.update_position('TCS', 'BUY', 5)
    tracker.update_position('RELIANCE', 'SELL', 5)
    logging.info(tracker.get_positions())
  
