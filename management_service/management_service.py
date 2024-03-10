import socket
import threading
import json


class ManagementService:
    def __init__(self, config_file):
        self.config_file = config_file
        self.monitoring_services = {}
        self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as f:
            self.config = json.load(f)

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind the socket to the port
        server_address = ('localhost', 10000)
        print(f'starting up on {server_address[0]} port {server_address[1]}')
        server_socket.bind(server_address)

        server_socket.listen(5)

        while True:
            print('waiting for a connection')
            connection, client_address = server_socket.accept()
            print(f'connection from {client_address}')

            monitoring_service_id = f"{client_address[0]}:{client_address[1]}"
            self.monitoring_services[monitoring_service_id] = {
                "connection":connection,
                "address": client_address,
                "tasks": []
            }

            threading.Thread(target=self.handle_monitoring_service, args=(connection, monitoring_service_id)).start()

    def handle_monitoring_service(self, connection, monitoring_service_id):
        try:
            while True:
                data = connection.recv(1024).decode('utf-8')
                print(f'received {data}')
                if data:
                    print('sending data back to the client')
                    message = json.loads(data)
                    action = message.get('action')
                    if action == 'register':
                        self.register_monitoring_service(connection, message)
                    elif message['action'] == 'report':
                        self.process_report(message)
                    else:
                        print('Unknown action')
                else:
                    print('no data from client, closing connection')
                    break
        finally:
            connection.close()
            self.monitoring_services.pop(monitoring_service_id, None)
    
    def register_monitoring_service(self, connection, message):
        service_id = message['service_id']
        if service_id not in self.monitoring_services:
            self.monitoring_services[service_id] = {
                "connection": connection,
                "tasks": [],
                "status": "online"
            }
            print(f"Registering new monitoring service: {message['service_id']}")
            self.distribute_inital_tasks(service_id)
        else:
            print(f"Monitoring Service {service_id} is already registered.")

    def process_report(self, message):
        print(f'Processing report from Monitoring Service: {message['task_id']}')

    def add_monitoring_service(self, host, port):
        print(f"Connecting to monitoring service at {host}:{port}")

    def distribute_tasks(self):
        for ms_id, ms_info in self.monitoring_services.items():
            task = {
                "action": "monitor",
                "tasks": {
                    "type": "http",
                    "url": "http://google.com",
                    "frequency": 60
                }
            }
            ms_info["connection"].sendall(json.dumps(task).encode('utf-8'))

    def start(self):
        self.start_server()

if __name__ == "__main__":
    ms = ManagementService('config/management_config.json')
    threading.Thread(targets=ms.start, daemon=True).start()

