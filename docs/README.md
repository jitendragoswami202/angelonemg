# Algo Trading Bot

This project is a fully automated, high-frequency market-making trading bot designed for options trading using Angel One API, WebSockets, and Google Cloud VM. The bot is capable of executing up to 5 trades per second.

## Features
- Market-Making Strategy optimized for high-frequency trading
- Dynamic Spread Adjustment
- Inventory Management
- Order Cancellation Logic
- Real-time WebSocket data streaming
- REST API integration for trade execution
- Logging for monitoring and troubleshooting

## Files
- `bot.py`: Main script to initiate and manage the bot
- `strategy.py`: Market-making strategy logic
- `trade_executor.py`: Handles order placement, cancellation, and modification
- `websocket_manager.py`: Manages WebSocket connections
- `websocket_client.py`: Client-side WebSocket handling
- `utils.py`: Utility functions and logging
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (saved in your Google Cloud VM)

## Environment Variables (.env)
```
API_KEY=your_api_key
ACCESS_TOKEN=your_access_token
CLIENT_CODE=your_client_code
BASE_URL=https://your-angel-one-api-url
```

## Installation
1. Clone the repository:
```
git clone https://github.com/your-username/your-repo.git
```
2. Navigate to the directory:
```
cd your-repo
```
3. Install dependencies:
```
pip install -r requirements.txt
```

## Usage
Run the bot with:
```
python bot.py
```

## Deployment
This bot is designed to run on your Google Cloud VM. Ensure all environment variables are properly configured.

## License
This project is licensed under the MIT License.

