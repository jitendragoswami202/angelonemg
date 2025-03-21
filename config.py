import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
BASE_URL = os.getenv("BASE_URL", "https://apiconnect.angelbroking.com/rest/auth")

# Safe Conversion Functions
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
    return str(os.getenv(env_var, str(default))).lower() in ["true", "1", "yes"]
