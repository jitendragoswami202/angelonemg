import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to safely convert environment variables
def safe_float(env_var, default):
    try:
        return float(os.getenv(env_var, default))
    except (ValueError, TypeError):
        return default

def safe_int(env_var, default):
    try:
        return int(os.getenv(env_var, default))
    except (ValueError, TypeError):
        return default

def safe_bool(env_var, default):
    return str(os.getenv(env_var, default)).strip().lower() in {"true", "1", "yes"}

# 🚀 Angel One API Credentials (Stored Securely in .env)
ANGEL_ONE_API_KEY = os.getenv("ANGEL_ONE_API_KEY")
ANGEL_ONE_CLIENT_ID = os.getenv("ANGEL_ONE_CLIENT_ID")
ANGEL_ONE_PASSWORD = os.getenv("ANGEL_ONE_PASSWORD")
ANGEL_ONE_TOTP_SECRET = os.getenv("ANGEL_ONE_TOTP_SECRET")

# Ensure all required API credentials are set
if not all([ANGEL_ONE_API_KEY, ANGEL_ONE_CLIENT_ID, ANGEL_ONE_PASSWORD, ANGEL_ONE_TOTP_SECRET]):
    raise ValueError("❌ Missing Angel One API credentials! Check your .env file.")

# ☁️ Google Cloud VM Details
PROJECT_ID = os.getenv("GCP_PROJECT_ID")
ZONE = os.getenv("GCP_ZONE")
INSTANCE_NAME = os.getenv("GCP_INSTANCE_NAME")

# Ensure Google Cloud details are set
if not all([PROJECT_ID, ZONE, INSTANCE_NAME]):
    raise ValueError("❌ Missing Google Cloud VM details! Check your .env file.")

# 📈 Trading Bot Settings
TRADE_SYMBOL = os.getenv("TRADE_SYMBOL", "NIFTY 27 Mar 24100 Call")
TRADE_QUANTITY = safe_int("TRADE_QUANTITY", 1)
TRADE_STRATEGY = os.getenv("TRADE_STRATEGY", "OPTIONS")

STOP_LOSS = safe_float("STOP_LOSS", 0.5)  # Example: 0.5% Stop Loss
TARGET_PROFIT = safe_float("TARGET_PROFIT", 1.0)  # Example: 1% Target Profit

# 🌐 Webhook & Redirect URLs
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
REDIRECT_URL = os.getenv("REDIRECT_URL")

if not all([WEBHOOK_URL, REDIRECT_URL]):
    raise ValueError("❌ Missing Webhook URLs! Check your .env file.")

# 🛠 Debugging & Logs
DEBUG_MODE = safe_bool("DEBUG_MODE", True)
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()  # Options: DEBUG, INFO, WARNING, ERROR

# ✅ Order Execution Settings
ORDER_TYPE = os.getenv("ORDER_TYPE", "LIMIT")  # Options: MARKET, LIMIT
EXCHANGE = os.getenv("EXCHANGE", "NSE")  # Options: NSE, BSE, MCX

# 🚀 Print confirmation
print("✅ Config loaded successfully!")
