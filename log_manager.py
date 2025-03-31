import logging


def setup_logging(log_file='algo_trading.log'):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )


if __name__ == "__main__":
    setup_logging()
    logging.info('Logging system initialized successfully.')
