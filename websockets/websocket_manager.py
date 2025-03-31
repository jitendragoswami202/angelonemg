from websocket_client import WebSocketClient
import time

class WebSocketManager:
    def __init__(self):
        self.client = WebSocketClient()
        self.channels = ["market-data", "order-status", "account-info"]

    def start(self):
        self.client.connect()
        time.sleep(1)  # Allow connection to establish
        self.client.subscribe(self.channels)

    def stop(self):
        self.client.close()

if __name__ == "__main__":
    manager = WebSocketManager()
    try:
        manager.start()
    except KeyboardInterrupt:
        print("🛑 Stopping WebSocket Manager")
        manager.stop()
