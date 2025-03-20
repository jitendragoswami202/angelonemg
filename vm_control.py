import os
import sys
from googleapiclient import discovery
from google.oauth2 import service_account

# Load Google Cloud Credentials
CREDENTIALS_PATH = "gcloud_service_key.json"  # Make sure this file exists

if not os.path.exists(CREDENTIALS_PATH):
    sys.exit(f"❌ Google Cloud credentials file not found: {CREDENTIALS_PATH}")

credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_PATH)
compute = discovery.build("compute", "v1", credentials=credentials)

# Set VM Details (Updated with Your Data)
PROJECT_ID = "teak-medium-453717-p8"  # ✅ Your Google Cloud Project ID
ZONE = "us-central1-a"  # ✅ Your VM Zone
INSTANCE_NAME = "instance-20250319-171515"  # ✅ Your VM Name

def start_vm():
    """Start the VM instance."""
    try:
        request = compute.instances().start(project=PROJECT_ID, zone=ZONE, instance=INSTANCE_NAME)
        response = request.execute()
        print(f"✅ VM {INSTANCE_NAME} is starting...")
        return response
    except Exception as e:
        print(f"❌ Error starting VM: {e}")

def stop_vm():
    """Stop the VM instance."""
    try:
        request = compute.instances().stop(project=PROJECT_ID, zone=ZONE, instance=INSTANCE_NAME)
        response = request.execute()
        print(f"✅ VM {INSTANCE_NAME} is stopping...")
        return response
    except Exception as e:
        print(f"❌ Error stopping VM: {e}")

def check_vm_status():
    """Check the VM instance status."""
    try:
        request = compute.instances().get(project=PROJECT_ID, zone=ZONE, instance=INSTANCE_NAME)
        response = request.execute()
        status = response.get("status", "UNKNOWN")
        print(f"🔍 VM {INSTANCE_NAME} status: {status}")
        return status
    except Exception as e:
        print(f"❌ Error fetching VM status: {e}")

# Handle Command-line Arguments
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❌ Usage: python vm_control.py [start|stop|status]")
        sys.exit(1)

    action = sys.argv[1].strip().lower()

    if action == "start":
        start_vm()
    elif action == "stop":
        stop_vm()
    elif action == "status":
        check_vm_status()
    else:
        print("❌ Invalid command! Use 'start', 'stop', or 'status'.")
        sys.exit(1)
