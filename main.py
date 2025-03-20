from auth import API_KEY, CLIENT_ID, SECRET_KEY
import requests

# ✅ Check if environment variables are loaded
if not all([API_KEY, CLIENT_ID, SECRET_KEY]):
    raise ValueError("❌ ERROR: Missing API credentials. Check your .env file.")

# ✅ Angel One Authentication Function
def authenticate():
    url = "https://apiconnect.angelbroking.com/rest/auth/angelbroking/user/v1/loginByPassword"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-ClientCode": CLIENT_ID,
        "X-APIKey": API_KEY
    }

    payload = {
        "clientcode": CLIENT_ID,
        "password": SECRET_KEY
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()

        if response.status_code == 200 and response_data.get("status") == "success":
            print("✅ Authentication Successful!")
            return response_data
        else:
            print(f"❌ Authentication Failed: {response_data.get('message', 'Unknown Error')}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"❌ Request Error: {str(e)}")
        return None

# ✅ Run Authentication
auth_response = authenticate()
if auth_response:
    print("🔹 Auth Token:", auth_response.get("data", {}).get("jwtToken", "No Token"))
