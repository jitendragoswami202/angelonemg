from flask import Flask, render_template, jsonify
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

positions = {
    'RELIANCE': 10,
    'TCS': 5,
    'INFY': 7
}

data = {
    'current_price': 1050,
    'buy_signal': True,
    'sell_signal': False
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/positions')
def get_positions():
    logging.info('Fetching current positions...')
    return jsonify(positions)


@app.route('/data')
def get_data():
    logging.info('Fetching current data...')
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
