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
