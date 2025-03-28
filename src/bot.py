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
