from flask import Flask, jsonify  # This is one import line
from dotenv import load_dotenv  # This is another import line
import os  # This is another import line

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/get_credentials', methods=['GET'])
def get_credentials():
    client_code = os.getenv('CLIENT_CODE')
    feed_token = os.getenv('FEED_TOKEN')
    return jsonify({"client_code": client_code, "feed_token": feed_token})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
