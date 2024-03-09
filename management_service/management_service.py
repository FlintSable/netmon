import socket
import threading
import json

class ManagementService:
    def __init__(self, config_file):
        self.config_file = config_file
        self.monitoring_services = []
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

            threading.Thread(target=self.handle_monitoring_service, args=(connection,)).start()

    def handle_monitoring_service(self, connection):
        try:
            while True:
                data = connection.recv(1024).decode('utf-8')
                print(f'received {data}')
                if data:
                    print('sending data back to the client')
                    message = json.loads(data)
                    if message['action'] == 'register':
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
    
    def register_monitoring_service(self, connection, message):
        print(f"Registering new monitoring service: {message['service_id']}")

    def process_report(self, message):
        print(f'Processing report from Monitoring Service: {message['task_id']}')

    def add_monitoring_service(self, host, port):
        print(f"Connecting to monitoring service at {host}:{port}")

    def distribute_tasks(self):
        print("Distributing tasks to monitoring services")

    def start(self):
        self.start_server()

