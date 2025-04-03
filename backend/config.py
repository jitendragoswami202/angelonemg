# config.py - Stores API credentials and trading configurations

API_KEY = "GxNM1r5a"
CLIENT_ID = "USSK3836"
SECRET_KEY = "9dee3b5a-0f5c-4227-8cb4-d0a69fab5b1d"

# Angel One API endpoints
LOGIN_URL = "https://apiconnect.angelbroking.com/rest/auth/angelbroking/user/v1/loginByPassword"
WEBSOCKET_URL = "wss://smartapisocket.angelone.in/websocket"

# Trading settings
TRADING_CONFIG = {
    "lot_size": 25,
    "max_orders_per_minute": 10,
    "risk_percentage": 1,  # 1% of capital per trade
    "stop_loss_percentage": 2,  # 2% stop loss
}
