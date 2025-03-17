from auth import API_KEY, CLIENT_ID, SECRET_KEY, REDIRECT_URL
import requests

# Example: API Authentication
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
        
        # Check if authentication was successful
        if response.status_code == 200 and response_data.get("status") == "success":
            return response_data
        else:
            return {"error": response_data.get("message", "Authentication failed")}
    
    except Exception as e:
        return {"error": str(e)}

# Run Authentication
auth_response = authenticate()
print("Authentication Response:", auth_response)
