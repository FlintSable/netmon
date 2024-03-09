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
            stdscr.addstr(6, 4, "1. Enable HTTPS Monitoring: ")
            stdscr.addstr(8, 4, "2. Enable DNS Monitoring: (not working)")
            stdscr.addstr(10, 4, "3. Enable TCP: (not working)" )
            stdscr.addstr(14, 4, "Select a number to enable a service: ")
            stdscr.addstr(16, 4, "Press 'q' to go back to the main menu")


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
                    # stdscr.move(2, 28)
                    # stdscr.clrtoeol()
                    # stdscr.refresh()

            # hostname_input = stdscr.getstr(2, 28).decode("utf-8")
            configured_servers[hostname_input] = Server(hostname_input)
            curses.noecho()
            stdscr.refresh()
            stdscr.move(14, 41)
            stdscr.refresh()



            # sub menu for configuring services
            while True:
                key = stdscr.getch()

                if key == ord('q') or key == ord('Q'):
                    break  # Exit the submenu and go back to the main menu
            
                elif key == ord('1'):
                    # this would be a third sub menu
                    # each of these would need a while loop of their own
                    # which would terminate once the service config was completed
                    stdscr.clear()

                    stdscr.addstr(0, 8, "******* Configure HTTPS Monitoring *******")
                    stdscr.addstr(2, 4, "Set URL: ")
                    stdscr.move(2, 13)
                    stdscr.refresh()
                    curses.echo()
                    while True:
                        input_url = stdscr.getstr(2, 13).decode("utf-8").strip()
                        if input_url:
                            configured_servers[hostname_input].http_url(input_url)

                            print("leaving")
                            break # this took me out of the program completly
                        else:
                            stdscr.addstr(4, 0, "URL cannot be empty. Press any key to try again.")
                            stdscr.refresh()
                            stdscr.getch()
                            stdscr.addstr(4, 0, " " * curses.COLS)
                    
                    curses.noecho()
                    stdscr.refresh()
                    stdscr.move(14, 41)
                    stdscr.refresh()
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
            stdscr.addstr(len(configured_servers) + 7, 4, "2. Run Monitoring")
            stdscr.addstr(len(configured_servers) + 9, 4, "q to quit app")

            # Refresh the screen
            stdscr.refresh()


        elif key == ord('q'):
            break  # Exit the main menu loop and terminate the program
    
        elif key == ord('2'):
            



if __name__ == "__main__":
    curses.wrapper(main)