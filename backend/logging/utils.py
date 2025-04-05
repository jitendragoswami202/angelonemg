# utils.py

import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_message(message):
    print(message)
    logging.info(message)

def current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def load_env_variables():
    from dotenv import load_dotenv
    import os

    load_dotenv()
    api_key = os.getenv('API_KEY')
    access_token = os.getenv('ACCESS_TOKEN')
    client_code = os.getenv('CLIENT_CODE')
    base_url = os.getenv('BASE_URL')

    return api_key, access_token, client_code, base_url
