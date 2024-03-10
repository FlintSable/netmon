import socket
import time
import json

class MonitoringService:
    def __init__(self, management_host, management_port, service_id):
        self.management_host = management_host
        self.management_port = management_port
        self.service_id = service_id
        self.tasks = []
        self.isConnected = False

    def start(self):
        """Attempt to connect to the management service and stay connected."""
        while True:
            try:
                if not self.isConnected:
                    self.connect_to_management()
                time.sleep(10)  # Check connection status every 10 seconds
            except Exception as e:
                self.isConnected = False
                print(f"Error: {e}. Attempting to reconnect...")
                time.sleep(5)  # Wait for 5 seconds before trying to reconnect

    def connect_to_management(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.management_host, self.management_port))
            self.isConnected = True
            print(f"Connected to Management Service at {self.management_host}:{self.management_port} with ID {self.service_id}")
            
            # Send registration message
            register_message = json.dumps({"action": "register", "service_id": self.service_id})
            sock.sendall(register_message.encode('utf-8'))

            while self.isConnected:
                # Listen for tasks
                try:
                    data = sock.recv(1024).decode('utf-8')
                    if data:
                        task = json.loads(data)
                        self.perform_task(task, sock)
                    else:
                        # Management Service closed the connection
                        self.isConnected = False
                        print("Lost connection to Management Service. Trying to reconnect...")
                except socket.error as e:
                    self.isConnected = False
                    print(f"Socket error occurred: {e}")
                except json.JSONDecodeError as e:
                    print(f"JSON decoding error occurred: {e}")

    def perform_task(self, task, sock):
        """Perform the assigned task and send back the result."""
        if task['action'] == 'monitor':
            print(f"Performing monitoring task: {task}")
            # Placeholder for actual monitoring logic
            
            # Simulate sending task completion report back to Management Service
            report = json.dumps({
                "action": "report",
                "service_id": self.service_id,
                "task_id": task.get("task_id", "unknown"),  # Assuming each task has a unique ID
                "status": "success",
                "details": "Task completed successfully."
            })
            sock.sendall(report.encode('utf-8'))
        else:
            print("Received unknown or unsupported task type")

    def send_report(self, report):
        # This method would send the task execution report back to the management service
        # Placeholder for sending the report back to the management service
        print(f"Sending report: {report}")

if __name__ == "__main__":
    host_name = socket.gethostname()
    timestamp = int(time.time())
    service_id = f"{host_name}_{timestamp}"
    monitoring_service = MonitoringService('localhost', 10000, service_id)
    monitoring_service.start()