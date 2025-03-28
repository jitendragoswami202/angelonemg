from flask import Flask, jsonify
import os
from notifier import send_telegram_alert

app = Flask(__name__)

@app.route('/restart-bot', methods=['POST'])
def restart_bot():
    """Restarts the trading bot"""
    send_telegram_alert("🔄 Restarting bot via dashboard...")
    os.system("sudo supervisorctl restart algo_bot")
    return jsonify({"status": "success", "message": "Bot restarted successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

LOG_FILE = "/home/user/algo-trading-bot/logs/bot.out.log"

def stream_logs():
    """Continuously read log file & send updates to the frontend."""
    with open(LOG_FILE, "r") as file:
        file.seek(0, 2)  # Move to the end of the file
        while True:
            line = file.readline()
            if line:
                socketio.emit("log_update", {"log": line})
            time.sleep(0.5)

@app.route("/")
def index():
    return render_template("dashboard.html")

if __name__ == "__main__":
    threading.Thread(target=stream_logs, daemon=True).start()
    socketio.run(app, host="0.0.0.0", port=5001, debug=True)
from flask import Flask, jsonify
import os
from notifier import send_telegram_alert

app = Flask(__name__)

@app.route('/start-bot', methods=['POST'])
def start_bot():
    """Starts the bot using Supervisor"""
    os.system("sudo supervisorctl start algo_bot")
    send_telegram_alert("✅ Bot Started via Dashboard")
    return jsonify({"status": "success", "message": "Bot started successfully"})

@app.route('/stop-bot', methods=['POST'])
def stop_bot():
    """Stops the bot using Supervisor"""
    os.system("sudo supervisorctl stop algo_bot")
    send_telegram_alert("⛔ Bot Stopped via Dashboard")
    return jsonify({"status": "success", "message": "Bot stopped successfully"})

@app.route('/bot-status', methods=['GET'])
def bot_status():
    """Checks if the bot is running"""
    status = os.popen("sudo supervisorctl status algo_bot").read()
    running = "RUNNING" in status
    return jsonify({"running": running})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
