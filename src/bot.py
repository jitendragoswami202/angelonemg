import time
from notifier import send_telegram_alert

try:
    print("🚀 Starting Trading Bot...")
    while True:
        # Run your strategy
        time.sleep(1)

except Exception as e:
    error_msg = f"⚠ BOT CRASHED: {str(e)}"
    send_telegram_alert(error_msg)
import time, os
from notifier import send_telegram_alert

def restart_bot():
    """Restarts the bot after a crash"""
    send_telegram_alert("⚠ BOT CRASHED! Restarting...")
    os.execv(__file__, ["python3"] + sys.argv)

try:
    print("🚀 Starting Trading Bot...")
    while True:
        # Run your strategy
        time.sleep(1)

except Exception as e:
    error_msg = f"⚠ BOT CRASHED: {str(e)}"
    send_telegram_alert(error_msg)
    restart_bot()
import json

CONFIG_FILE = "/home/user/algo-trading-bot/config.json"

def load_config():
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)

config = load_config()

# Use settings in your bot logic
lot_size = config["lot_size"]
max_risk = config["max_risk"]
strategy = config["strategy"]
