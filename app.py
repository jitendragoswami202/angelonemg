from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/get_credentials', methods=['GET'])
def get_credentials():
    client_code = os.getenv('CLIENT_CODE')
    feed_token = os.getenv('FEED_TOKEN')
    
    if not client_code or not feed_token:
        return jsonify({
            "success": False,
            "error": "Environment variables not properly set. Check .env file."
        }), 500

    return jsonify({
        "success": True,
        "data": {
            "client_code": client_code,
            "feed_token": feed_token
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
