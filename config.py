import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# 🚀 Angel One API Credentials (Stored Securely in .env)
ANGEL_ONE_API_KEY = os.getenv("ANGEL_ONE_API_KEY", "")
ANGEL_ONE_CLIENT_ID = os.getenv("ANGEL_ONE_CLIENT_ID", "")
ANGEL_ONE_PASSWORD = os.getenv("ANGEL_ONE_PASSWORD", "")
ANGEL_ONE_TOTP_SECRET = os.getenv("ANGEL_ONE_TOTP_SECRET", "")

# ☁️ Google Cloud VM Details
PROJECT_ID = os.getenv("GCP_PROJECT_ID", "your-project-id")
ZONE = os.getenv("GCP_ZONE", "your-vm-zone")
INSTANCE_NAME = os.getenv("GCP_INSTANCE_NAME", "your-vm-name")

# 📊 Trading Bot Settings
TRADE_SYMBOL = os.getenv("TRADE_SYMBOL", "NIFTY 27 Mar 24100 Call")
TRADE_QUANTITY = int(os.getenv("TRADE_QUANTITY", "1"))
TRADE_STRATEGY = os.getenv("TRADE_STRATEGY", "OPTIONS")

try:
    STOP_LOSS = float(os.getenv("STOP_LOSS", "0.5"))  # Example: 0.5% Stop Loss
except ValueError:
    STOP_LOSS = 0.5

try:
    TARGET_PROFIT = float(os.getenv("TARGET_PROFIT", "1.0"))  # Example: 1% Target
except ValueError:
    TARGET_PROFIT = 1.0

# 🔗 Webhook & Redirect URLs
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://angelonemg.netlify.app/.netlify/functions/webhook")
REDIRECT_URL = os.getenv("REDIRECT_URL", "https://angelonemg.netlify.app")

# 🛠️ Debugging & Logs
DEBUG_MODE = os.getenv("DEBUG_MODE", "True").lower() in ["true", "1"]
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")  # Options: DEBUG, INFO, WARNING, ERROR

# 🏦 Order Execution Settings
ORDER_TYPE = os.getenv("ORDER_TYPE", "LIMIT")  # Options: MARKET, LIMIT
EXCHANGE = os.getenv("EXCHANGE", "NSE")  # Options: NSE, BSE, MCX
