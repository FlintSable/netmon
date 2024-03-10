import threading
import time
import socket
from management_service.management_service import ManagementService
from monitoring_service.monitoring_service import MonitoringService

DEBUG_MODE = True

def start_management_service():
    management_service = ManagementService('configs/management_config.json')
    management_service.start()

def start_monitoring_service():
    host_name = socket.gethostname()
    timestamp = int(time.time())
    service_id = f"{host_name}_{timestamp}"
    monitoring_service = MonitoringService('localhost', 10000, service_id)
    monitoring_service.start()

if __name__ == "__main__":
    if DEBUG_MODE:
        management_thread = threading.Thread(target=start_management_service, daemon=True)
        management_thread.start()

        time.sleep(1)
        start_monitoring_service()

    else:
        management_thread = threading.Thread(target=start_management_service, daemon=True)
        management_thread.start()