import os
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class VMControl:
    def __init__(self, instance_name: str, project_id: str, zone: str):
        self.instance_name = instance_name
        self.project_id = project_id
        self.zone = zone

    def start_vm(self):
        try:
            logging.info(f'Starting VM: {self.instance_name}')
            result = subprocess.run([
                'gcloud', 'compute', 'instances', 'start', self.instance_name,
                '--project', self.project_id,
                '--zone', self.zone
            ], check=True, capture_output=True, text=True)
            logging.info(f'VM started successfully: {result.stdout}')
        except subprocess.CalledProcessError as e:
            logging.error(f'Failed to start VM: {e.stderr}')
            return False
        return True

    def stop_vm(self):
        try:
            logging.info(f'Stopping VM: {self.instance_name}')
            result = subprocess.run([
                'gcloud', 'compute', 'instances', 'stop', self.instance_name,
                '--project', self.project_id,
                '--zone', self.zone
            ], check=True, capture_output=True, text=True)
            logging.info(f'VM stopped successfully: {result.stdout}')
        except subprocess.CalledProcessError as e:
            logging.error(f'Failed to stop VM: {e.stderr}')
            return False
        return True
        
