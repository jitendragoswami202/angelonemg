import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class MarketDataFetcher:
    def __init__(self, api_key, access_token):
        self.api_key = api_key
        self.access_token = access_token
        self.base_url = 'https://api.angelbroking.com/rest/market/feed'

    def fetch_data(self, symbols):
        try:
            logging.info('Fetching market data...')

            payload = {
                'api_key': self.api_key,
                'access_token': self.access_token,
                'symbols': symbols
            }

            response = requests.post(self.base_url, json=payload)
            response.raise_for_status()

            data = response.json()
            if data['status'] == 'success':
                logging.info('Market data fetched successfully.')
                return data['data']
            else:
                logging.error(f'Error fetching market data: {data}')
                return None

        except requests.RequestException as e:
            logging.error(f'Request error while fetching data: {str(e)}')
            return None
        except Exception as e:
            logging.error(f'Unexpected error: {str(e)}')
            return None


if __name__ == "__main__":
    fetcher = MarketDataFetcher(api_key="YOUR_API_KEY", access_token="YOUR_ACCESS_TOKEN")
    symbols = ["RELIANCE", "TCS", "INFY"]
    data = fetcher.fetch_data(symbols)
    logging.info(data)
  
