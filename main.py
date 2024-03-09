import threading
import time
from management_service.management_service import ManagementService
from monitoring_service.monitoring_service import MonitoringService

DEBUG_MODE = True

def start_management_service():
    management_service = ManagementService('config/management/config.json')
    management_service.start()

def start_monitoring_service():
    monitoring_service = MonitoringService('localhost', 12345)
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