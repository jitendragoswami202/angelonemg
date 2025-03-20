import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch required API credentials
API_KEY = os.getenv("API_KEY")
CLIENT_ID = os.getenv("CLIENT_ID")
SECRET_KEY = os.getenv("SECRET_KEY")
REDIRECT_URL = os.getenv("REDIRECT_URL")

# Check if all required variables are available
if not all([API_KEY, CLIENT_ID, SECRET_KEY, REDIRECT_URL]):
    raise ValueError("❌ ERROR: Missing required environment variables. Check your .env file.")

# Optional: Print masked API details for debugging
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
if DEBUG:
    print(f"🔹 API Key Loaded: {API_KEY[:4]}****")  # Mask API Key
    print(f"🔹 Client ID: {CLIENT_ID}")
    print(f"🔹 Redirect URL: {REDIRECT_URL}")
