import socket
import json
import time

class MonitoringService:
    def __init__(self, management_host, management_port):
        self.management_host = management_host
        self.management_port = management_port

    def send_heartbeat(self, sock):
        """
        Send a heartbeat message to the Management Service
        """
        heartbeat_message = json.dumps({"action": "heartbeat", "status": "alive"})
        sock.sendall(heartbeat_message.encode('utf--8'))

    def start_client(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.management_host, self.management_port))
            print(f"Connected to Management Service at {(self.management_host, self.management_port)}")

            self.send_heartbeat(s)

            try:
                while True:
                    data = s.recv(1024)
                    if not data:
                        break
                    task = json.loads(data.decode())
                    print(f"Received task: {task}")

                    result = json.dumps({"result": "success", "details": "Task completed"})
                    s.sendall(result.encode('utf-8'))

                    time.sleep(1)
            except ConnectionResetError:
                print("Connection lost. Attempting to reconnect.")

if __name__ == "__main__":
    monitoring_service = MonitoringService('localhost', 10000)
    monitoring_service.start_client()