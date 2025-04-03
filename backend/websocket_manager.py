# websocket_manager.py - Managing WebSocket Connections
from websocket_client import WebSocketClient
import time
import logging

class WebSocketManager:
    def __init__(self):
        self.client = WebSocketClient()
        self.logger = logging.getLogger("WebSocketManager")
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def start(self):
        self.logger.info("Starting WebSocket Client")
        self.client.start()

    def stop(self):
        self.logger.info("Stopping WebSocket Client")
        self.client.stop()

    def restart(self):
        self.logger.info("Restarting WebSocket Client")
        self.stop()
        time.sleep(5)  # Graceful restart delay
        self.start()

if __name__ == "__main__":
    manager = WebSocketManager()
    manager.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        manager.stop()
        print("WebSocket Manager Stopped")
