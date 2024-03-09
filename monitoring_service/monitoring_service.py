import socket

class MonitoringService:
    def __init__(self, management_host, management_port):
        self.managemnet_host = management_host
        self.managemnet_port = management_port
        self.tasks = []

    def start(self):
        print(f"Connecting to Management Service at {self.managemnet_host}:{self.managemnet_port}")
        self.connect_to_management()

    def perform_task(self, task):
        print(f"Perfonming task: {task}")

    def connect_to_management(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_address = (self.managemnet_host, self.managemnet_port)
        print(f'connecting to {server_address[0]} port {server_address[1]}')
        sock.connect(server_address)

        try:
            message = 'This is the monitoring service. Requesting tasks....'
            print(f'sending {message}')
            sock.sendall(message.encode())

            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = sock.recv(1024)
                amount_received += len(data)
                print(f'received {data}')

        finally:
            print('closing socket')
            sock.close()
