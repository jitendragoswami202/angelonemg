#!/bin/bash

echo "🚀 Pulling latest updates..."
cd /home/user/algo-trading-bot  # Change to your bot directory
git pull origin main

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🔄 Restarting bot..."
pkill -f app.py  # Stop running bot
nohup python3 app.py > logs/bot.log 2>&1 &  # Restart bot in background

echo "✅ Deployment complete!"
