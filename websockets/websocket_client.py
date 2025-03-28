import websocket
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class WebSocketClient:
    def __init__(self, ws_url, feed_token, api_key):
        self.ws_url = ws_url
        self.feed_token = feed_token
        self.api_key = api_key
        self.ws = None

    def on_message(self, ws, message):
        try:
            data = json.loads(message)
            logging.info(f'Received Message: {data}')
        except json.JSONDecodeError as e:
            logging.error(f'Error decoding message: {str(e)}')

    def on_error(self, ws, error):
        logging.error(f'WebSocket error: {str(error)}')

    def on_close(self, ws, close_status_code, close_msg):
        logging.info('WebSocket connection closed.')

    def on_open(self, ws):
        logging.info('WebSocket connection opened.')
        auth_payload = {
            'action': 'authenticate',
            'api_key': self.api_key,
            'feed_token': self.feed_token
        }
        ws.send(json.dumps(auth_payload))

    def connect(self):
        self.ws = websocket.WebSocketApp(
            self.ws_url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self.ws.run_forever()


if __name__ == "__main__":
    ws_client = WebSocketClient(
        ws_url="wss://ws.angelbroking.com",  # Replace with your WS URL
        feed_token="YOUR_FEED_TOKEN",
        api_key="YOUR_API_KEY"
    )
    ws_client.connect()
    
