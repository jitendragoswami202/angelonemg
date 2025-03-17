import os  
from dotenv import load_dotenv  

load_dotenv()  # .env

API_KEY = os.getenv("API_KEY")
CLIENT_ID = os.getenv("CLIENT_ID")
SECRET_KEY = os.getenv("SECRET_KEY")
REDIRECT_URL = os.getenv("REDIRECT_URL")

print("API Key:", API_KEY)
