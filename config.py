import os

# 🔹 Angel One API Credentials
ANGEL_ONE_API_KEY = os.getenv("ANGEL_ONE_API_KEY", "yUdBvecQ")  
ANGEL_ONE_CLIENT_ID = os.getenv("ANGEL_ONE_CLIENT_ID", "USSK3836")  
ANGEL_ONE_PASSWORD = os.getenv("ANGEL_ONE_PASSWORD", "Mg787916@$")  
ANGEL_ONE_TOTP_SECRET = os.getenv("ANGEL_ONE_TOTP_SECRET", "DDMAPLVKTLH35CYVPM7LJFETZE")  

# 🔹 Google Cloud VM Details
PROJECT_ID = "teak-medium-453718-p8"
ZONE = "us-cent4al1-a"
INSTANCE_NAME = "instance-20250319171515"

# 🔹 Bot Settings
TRADE_SYMBOL = "NIFTY 27 Mar 24100 Call"
TRADE_QUANTITY = 1
TRADE_STRATEGY = "OPTIONS"

# 🔹 Webhook URL (For Auto Trading Execution)
WEBHOOK_URL = "your_webhook_url_here"

# 🔹 Redirect URL (For API Authentication)
REDIRECT_URL = "https://angelonemg.netlify.app"

# 🔹 Logging & Debugging
DEBUG_MODE = True  # Set to False in production
