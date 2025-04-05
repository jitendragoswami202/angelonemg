import time
import json
from auth import Auth

auth = Auth()
auth.load_tokens() 

REFRESH_INTERVAL = 3600  

while True:
    try:
        new_access_token = auth.refresh_access_token()
        if new_access_token:
            print(f"New Access Token: {new_access_token}")
        else:
            print("Failed to refresh access token. Trying again in 5 minutes.")

        time.sleep(REFRESH_INTERVAL)
    except Exception as e:
        print(f"Error in auto_token_generator: {str(e)}")
        time.sleep(300)  