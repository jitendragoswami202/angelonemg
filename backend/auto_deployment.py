# auto_deployment.py - Deployment Automation
import os
import subprocess
import time
from dotenv import load_dotenv

load_dotenv()

REPO_URL = os.getenv('GITHUB_REPO_URL')  # Your GitHub repository URL
BRANCH = os.getenv('BRANCH', 'main')  # Branch to deploy from

LOCAL_DIR = '/home/your_user/your_project_folder'  # Local directory for deployment


def clone_or_pull_repo():
    if os.path.exists(LOCAL_DIR):
        print('Pulling latest changes from the repository...')
        subprocess.run(['git', '-C', LOCAL_DIR, 'pull', 'origin', BRANCH])
    else:
        print('Cloning the repository...')
        subprocess.run(['git', 'clone', REPO_URL, LOCAL_DIR])


def install_requirements():
    print('Installing dependencies...')
    subprocess.run(['pip', 'install', '-r', os.path.join(LOCAL_DIR, 'requirements.txt')])


def start_bot():
    print('Starting the trading bot...')
    subprocess.Popen(['python', os.path.join(LOCAL_DIR, 'main.py')])


def deploy():
    try:
        clone_or_pull_repo()
        install_requirements()
        start_bot()
    except Exception as e:
        print(f"Deployment failed: {str(e)}")


if __name__ == "__main__":
    while True:
        deploy()
        print('Deployment successful. Checking for updates in 10 minutes...')
        time.sleep(600)  # Check for updates every 10 minutes
