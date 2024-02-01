from helpers.network_utilities import calculate_icmp_checksum, ping
from helpers.server import Server
import curses


def main(stdscr):
    # Clear the screen
    stdscr.clear()

    # list loop version
    # configured_servers = []
    # if configured_servers:
    #     stdscr.addstr(0, 0, "Configured Servers:")
    #     for i, server in enumerate(configured_servers):
    #         stdscr.addstr(i + 2, 0, f"\t {server}")
    # else:
    #     stdscr.addstr(0, 0, "No configured servers found.")

    configured_servers = {}
    if configured_servers:
        stdscr.addstr(0,0, "Configured Servers:")
        for i, server in enumerate(configured_servers.keys()):
            stdscr.addstr(i + 2, 4, f"\t {server}")
    else:
        stdscr.addstr(0, 4, "No configured servers found.")

    stdscr.addstr(len(configured_servers) + 3, 4, "Enter an option:")
    # stdscr.addstr(len(configured_servers) + 3, len("Options: "), " ", curses.A_REVERSE)
    stdscr.addstr(len(configured_servers) + 5, 4, "1. Configure New Server")
    stdscr.addstr(len(configured_servers) + 7, 4, "q to quit app")

    stdscr.move(len(configured_servers) + 3, len("Enter an option: ") + 4)


    # Refresh the screen
    stdscr.refresh()

    # main menu
    while True:
        key = stdscr.getch()

        if key == ord('1'):

            
            # Clear the screen
            stdscr.clear()

            # Print the loop menu
            stdscr.addstr(0, 8, "******* Configure Server Menu *******")
            stdscr.addstr(2, 4, "Set Hostname or IP Address: ")

            # for i, service in enumerate()
            stdscr.addstr(6, 4, "1. Enable HTTPS Monitoring (y) or n: ")
            stdscr.addstr(8, 6, "1.1. Set URL: ")

            stdscr.addstr(10, 4, "2. Enable DNS Monitoring (y) or n: ")
            stdscr.addstr(12, 6, "2.1. Set DNS: ")

            stdscr.addstr(14, 4, "3. Enable TCP (y) or n: " )
            stdscr.addstr(18, 4, "Select a number to enable a service: ")
            stdscr.addstr(20, 4, "Press 'q' to go back to the main menu")


            stdscr.move(2, 32)
            stdscr.refresh()
            curses.echo()

            # checks for invalid input
            while True:
                hostname_input = stdscr.getstr(2, 32).decode("utf-8").strip()
                if hostname_input:
                    break
                else:
                    stdscr.addstr(4, 0, "Hostname cannot be empty. Press any key to try again.")
                    stdscr.refresh()
                    stdscr.getch()
                    stdscr.addstr(4, 0, " " * curses.COLS)


            configured_servers[hostname_input] = Server(hostname_input)
            curses.noecho()
            stdscr.refresh()
            stdscr.move(14, 41)
            stdscr.refresh()

            stdscr.move(6, 41)
            stdscr.refresh()
            curses.echo()
            while True:
                key = stdscr.getch()
                if key == ord('y'):
                    stdscr.move(8, 20)
                    input_url = stdscr.getstr(8, 20).decode("utf-8").strip()
                    # put that into the instantiated server
                    # enable the service
                    stdscr.move(10, 39)
                elif key == ord('n'):
                    stdscr.move(10, 39)
                break

            while True:
                key = stdscr.getch()
                if key == ord('y'):
                    stdscr.move(12, 20)
                    input_dns = stdscr.getstr(12, 20).decode("utf-8").strip()
                    # put that into the instantiated server
                    # enable the service
                    stdscr.move(14, 28)
                elif key == ord('n'):
                    stdscr.move(14, 28)
                break





            print("I guess were going to the main menu next then? ")
            # Clear the screen
            stdscr.clear()
            # Print the main menu again
            stdscr.addstr(0, 0, "Configured Servers:")
            if configured_servers:
                for i, server in enumerate(configured_servers.keys()):
                    stdscr.addstr(i + 1, 0, f"{configured_servers[server].name}")
            else:
                stdscr.addstr(0, 0, "No configured servers found. Placeholder text.")
            stdscr.addstr(len(configured_servers) + 3, 4, "Options:")
            stdscr.addstr(len(configured_servers) + 5, 4, "1. Configure Server")
            stdscr.addstr(len(configured_servers) + 7, 4, "1. Run Monitoring")

            stdscr.addstr(len(configured_servers) + 9, 4, "q to quit app")

            # Refresh the screen
            stdscr.refresh()


        elif key == ord('q'):
            break  # Exit the main menu loop and terminate the program



if __name__ == "__main__":
    curses.wrapper(main)