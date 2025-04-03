#!/bin/bash

# deployment_script.sh - Automated Deployment Script for Algo Trading Bot

# Update system packages
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Python and pip if not already installed
sudo apt-get install python3 python3-pip -y

# Install virtualenv for creating a virtual environment
pip3 install virtualenv

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Export environment variables from .env file
export $(grep -v '^#' .env | xargs)

# Run the bot
python bot.py &

# Print success message
echo "Deployment completed successfully and bot is running."
