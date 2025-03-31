from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import threading
import time
import random

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

bot_running = False

@app.route('/start-bot', methods=['POST'])
def start_bot():
    global bot_running
    bot_running = True
    return jsonify({'status': 'Bot started successfully.'})

@app.route('/stop-bot', methods=['POST'])
def stop_bot():
    global bot_running
    bot_running = False
    return jsonify({'status': 'Bot stopped successfully.'})


def send_updates():
    while True:
        if bot_running:
            data = {
                'openPositions': [{'symbol': 'NIFTY', 'quantity': 2, 'price': 18000}],
                'openOrders': [{'symbol': 'NIFTY', 'quantity': 1, 'price': 18010}],
                'availableFunds': 100000 + random.uniform(-1000, 1000),
                'totalPnL': random.uniform(-5, 5)
            }
            socketio.emit('update', data)
        time.sleep(0.2)  # Send updates 5 times per second


if __name__ == '__main__':
    update_thread = threading.Thread(target=send_updates)
    update_thread.daemon = True
    update_thread.start()
    socketio.run(app, host='0.0.0.0', port=5000)
    
