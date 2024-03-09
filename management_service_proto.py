import socket
import threading
import json

class ManagementService:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.monitoring_services = {}

    def handle_client(self, conn, addr):
        """ Handle incoming data from Monitoring Services. """
        with conn:
            print(f"Connected to Monitoring Services at {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                try:
                    message = json.loads(data.decode())
                    print(f"Received data from {addr}: {message}")
                except json.JSONDecodeError:
                    print("Received data is not in JSON format")
            print(f'Connection closed to Monitoring Service at {addr}')

    def start_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Management Service listening on {self.host}:{self.port}")
            while True:
                conn, addr = s.accept()
                client_thread = threading.Thread(target=self.handle_client, args=( conn, addr))
                client_thread.start()

if __name__ == "__main__":
    management_service = ManagementService('localhost', 10000)
    management_service.start_server()
