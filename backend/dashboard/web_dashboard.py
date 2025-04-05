# web_dashboard.py

from flask import Flask, request, jsonify
from utils import log_message
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Algo Trading Bot Web Dashboard is Running"


@app.route('/start-bot', methods=['POST'])
def start_bot():
    try:
        subprocess.Popen(['python3', 'bot.py'])
        log_message("Bot started successfully.")
        return jsonify({"status": "Bot started successfully."})
    except Exception as e:
        log_message(f"Error starting bot: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/stop-bot', methods=['POST'])
def stop_bot():
    try:
        os.system("pkill -f bot.py")
        log_message("Bot stopped successfully.")
        return jsonify({"status": "Bot stopped successfully."})
    except Exception as e:
        log_message(f"Error stopping bot: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/status', methods=['GET'])
def status():
    try:
        # Check if the bot is running
        result = subprocess.run(['pgrep', '-f', 'bot.py'], capture_output=True, text=True)
        if result.returncode == 0:
            return jsonify({"status": "Bot is running."})
        else:
            return jsonify({"status": "Bot is not running."})
    except Exception as e:
        log_message(f"Error checking bot status: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
