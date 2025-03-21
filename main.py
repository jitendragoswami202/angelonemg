from auth import API_KEY, CLIENT_ID, SECRET_KEY
from config import BASE_URL
import requests

# ✅ Check if environment variables are loaded
if not all([API_KEY, CLIENT_ID, SECRET_KEY]):
    raise ValueError("❌ ERROR: Missing API credentials. Check your .env file.")

# ✅ Angel One Authentication Function
def authenticate():
    url = f"{BASE_URL}/login"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Client-Id": CLIENT_ID,
        "X-Secret-Key": SECRET_KEY,
    }

    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Authentication Failed")

# ✅ Example Call
if __name__ == "__main__":
    print(authenticate())
