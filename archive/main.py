import curses

# Debug mode flag
DEBUG_MODE = True

# Define a class to represent a server and its configuration
class Server:
    instance_count = 0
    def __init__(self, hostname, ip, port):
        Server.instance_count += 1
        self.unique_id = f"server{Server.instance_count:03d}"

        self.hostname = hostname
        self.ip = ip
        self.port = port
        self.enable_https = False
        self.url = ''
        self.enable_dns = False
        self.dns = ''
        self.enable_tcp = False
        self.connection_status = 'Disconnected'
        self.monitoring_tasks = {}

    def add_monitor_task(self, task_id, task_config):
        self.monitoring_tasks[task_id] = task_config
    
    def rem_monitor_task(self, task_id):
        if task_id in self.monitoring_tasks:
            del self.monitoring_tasks[task_id]

    def __str__(self):
        return (f"Server(ID: {self.unique_id}, Hostname: {self.hostname}, IP: {self.ip}, Port: {self.port}, "
                f"HTTPS: {self.enable_https}, URL: {self.url}, DNS: {self.enable_dns}, DNS Address: {self.dns}, "
                f"TCP: {self.enable_tcp}, Connection Status: {self.connection_status}, "
                f"Monitoring Tasks: {len(self.monitoring_tasks)})")

# Dictionary to store configured servers
configured_servers = {}

def print_debug(stdscr, text):
    if DEBUG_MODE:
        stdscr.addstr(0, 40, "Debug Mode: ON", curses.A_REVERSE)
        stdscr.addstr(1, 40, text)

def main_menu(stdscr):
    k = 0
    left_margin = 4
    top_margin = 2

    curses.curs_set(0)  # Hide cursor

    while k != ord('q'):  # Press 'q' to quit
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == ord('1'):
            configure_server(stdscr)
        elif k == ord('2'):
            run_monitoring(stdscr)

        # Main Menu UI with margins
        stdscr.addstr(top_margin, left_margin, "Menu 1 Configured Servers:")
        for i, server in enumerate(configured_servers.keys()):
            stdscr.addstr(top_margin + i + 1, left_margin + 2, server)

        menu_options = "Options:\n\n1. Configure Server\n\n2. Run Monitoring\n\nq to quit app"
        stdscr.addstr(top_margin + 8, left_margin, menu_options)
        stdscr.refresh()

        print_debug(stdscr, f"Configured Servers: {len(configured_servers)}")

        k = stdscr.getch()

def configure_server(stdscr):
    curses.echo()  # Enable echoing of characters
    stdscr.clear()
    left_margin = 4
    top_margin = 2

    # Server configuration UI with margins
    stdscr.addstr(top_margin, left_margin, "******* Configure Server Menu 2*******\n")
    stdscr.addstr(top_margin + 2, left_margin, "Set Hostname or IP Address:")
    hostname = stdscr.getstr(top_margin + 3, left_margin).decode('utf-8')

    new_server = Server(hostname)
    stdscr.addstr(top_margin + 5, left_margin, "1. Enable HTTPS Monitoring (y) or n:")
    if stdscr.getstr(top_margin + 6, left_margin).decode('utf-8').lower() == 'y':
        new_server.enable_https = True
        stdscr.addstr(top_margin + 7, left_margin, "1.1. Set URL:")
        new_server.url = stdscr.getstr(top_margin + 8, left_margin).decode('utf-8')

    # Debug log
    print_debug(stdscr, str(new_server))

    configured_servers[hostname] = new_server  # Save the configured server
    curses.noecho()
    stdscr.clear()
    stdscr.addstr(top_margin, left_margin, "Server configured. Press any key to return to the main menu.")
    stdscr.getch()  # Wait for user input before returning

def run_monitoring(stdscr):
    # Placeholder for monitoring functionality
    stdscr.addstr(2, 4, "Monitoring functionality not implemented. Press any key to return.")
    stdscr.getch()

# Entry point
def start_app():
    curses.wrapper(main_menu)

# Uncomment the line below to run the application in a terminal environment that supports curses.
start_app()
