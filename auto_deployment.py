# auto_deployment.py

import os
import subprocess
from utils import log_message

def deploy_bot():
    try:
        log_message("Starting deployment...")

        # Run the deployment script
        result = subprocess.run(['bash', 'deployment_script.sh'], capture_output=True, text=True)
        
        if result.returncode == 0:
            log_message("Deployment completed successfully.")
        else:
            log_message(f"Deployment failed with error: {result.stderr}")
    except Exception as e:
        log_message(f"Deployment error: {e}")


if __name__ == "__main__":
    deploy_bot()
