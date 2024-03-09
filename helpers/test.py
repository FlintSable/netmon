import curses


def main(stdscr):
    # Clear the screen
    stdscr.clear()

    configured_servers = ["server1", "server2", "server3"]

    if configured_servers:
        stdscr.addstr(0, 0, "Configured Servers:")
        for i, server in enumerate(configured_servers):
            stdscr.addstr(i + 2, 0, f"\t {server}")
    else:
        stdscr.addstr(0, 0, "No configured servers found.")

    stdscr.addstr(len(configured_servers) + 3, 0, "Optopms:")
    stdscr.addstr(len(configured_servers) + 5, 0, "1. Configure New Server")
    stdscr.addstr(len(configured_servers) + 6, 0, "2. Exit")


    # Refresh the screen
    stdscr.refresh()

    # Wait for user input
    while True:
        key = stdscr.getch()

        if key == ord('1'):
            # Clear the screen
            stdscr.clear()

            # Print the loop menu
            stdscr.addstr(0, 0, "Configure Server")
            stdscr.addstr(2, 0, "1. Set Hostname or IP Address: ")
            stdscr.addstr(4, 0, "2. Enable HTTPS Monitoring: ")
            stdscr.addstr(6, 0, "3. Enable DNS Monitoring: ")
            stdscr.addstr(8, 0, "4. Enable TCP: " )
            stdscr.addstr(10, 0, "Press 'q' to go back to the main menu")
            # Refresh the screen
            stdscr.refresh()

            # counter = 0
            # # Enter the loop
            # while True:
            #     counter += 1
            #     stdscr.clear()
            #     stdscr.addstr(0, 0, "Loop Menu")
            #     stdscr.addstr(2, 0, f"Counter: {counter}")
            #     stdscr.addstr(3, 0, "Press 'q' to exit the loop")

            #     # Refresh the screen
            #     stdscr.refresh()
    
            #     key = stdscr.getch()

            #     if key == ord('q'):
            #         break  # Exit the loop and go back to the main menu
            
            # stdscr.clear()
            # stdscr.addstr(0, 0, "Main Menu")
            # stdscr.addstr(2, 0, "1. Start Loop")
            # stdscr.addstr(3, 0, "2. Exit")
            hostname = ""

            # user input while loop
            while True:
                key = stdscr.getch()

                if key == ord('q') or key == ord('Q'):
                    break  # Exit the submenu and go back to the main menu
                
                if key == ord('1'):
                    stdscr.refresh()
                    stdscr.addstr(2, 0, "1. Set Hostname or IP Address: ")
                    stdscr.refresh()
                    curses.echo()
                    hostname = stdscr.getstr(2, 32).decode("utf-8")
                    curses.noecho()
                    stdscr.addstr(2, 0, "1. Change Hostname or IP Address: " + hostname)
                    stdscr.refresh()
                    stdscr.move(10, 0)
                    stdscr.refresh()


            # Clear the screen
            stdscr.clear()

            # Print the main menu again
            stdscr.addstr(0, 0, "Configured Servers:")
            if configured_servers:
                for i, server in enumerate(configured_servers):
                    stdscr.addstr(i + 1, 0, f"{server}")
            else:
                stdscr.addstr(0, 0, "No configured servers found. Placeholder text.")
            stdscr.addstr(len(configured_servers) + 3, 0, "Options:")
            stdscr.addstr(len(configured_servers) + 5, 0, "1. Configure Server")
            stdscr.addstr(len(configured_servers) + 6, 0, "2. Exit")

            # Refresh the screen
            stdscr.refresh()
   

        elif key == ord('2'):
            break  # Exit the main menu loop and terminate the program

# Initialize curses and run the main function
curses.wrapper(main)