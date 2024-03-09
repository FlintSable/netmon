from helpers.network_utilities import calculate_icmp_checksum, ping
from helpers.server import Server
import curses

def main_menu(stdscr):
    stdscr.clear()
    stdscr.addstr("Main Menu\n")
    stdscr.addstr("1. Go to Sub Menu 1\n")
    stdscr.addstr("2. Run Monitoring\n")
    stdscr.addstr("q to quit\n")
    stdscr.refresh()

    configured_servers = {}
    while True:
        key = stdscr.getch()
        if key == ord('1'):
            sub_menu1_config_server(stdscr)
        elif key == ord('q'):
            break

def sub_menu1_config_server(stdscr):
    """This would be the configure server menu, an blank instance of a server needs to be
        created here. It should be passed to each sub menu 2 where it will be modified and returned to the sub menu 1.
        once all the changes have been applied to the server and its services, it should be stored in a configured servers list or dict"""
    stdscr.clear()
    stdscr.addstr("Sub Menu 1\n")
    stdscr.addstr("1. Enable and Configure HTTP & HTTPS\n")
    stdscr.addstr("2. Enable and Configure DNS & NTP\n")
    stdscr.addstr("3. Enable and Configure TCP & UDP\n")
    stdscr.addstr("4. Go back to Main Menu\n")
    stdscr.refresh()
    new_server_instance = Server()

    while True:
        key = stdscr.getch()
        if key == ord('1'):
            sub_menu2_http_https(stdscr, new_server_instance) # maybe I need to pass the server object through this
        if key == ord('2'):
            sub_menu2_dns_ntp(stdscr, new_server_instance)
        elif key == ord('3'):
            sub_menu2_tcp_udp(stdscr, new_server_instance)
        elif key == ord('4'):
            break

def sub_menu2_http_https(stdscr, instance):
    stdscr.clear()
    stdscr.addstr("Enable and Configure HTTP & HTTPS monitoring\n")
    stdscr.addstr("1. Enable or Disable HTTP\n")
    stdscr.addstr("2. Set URL\n")
    stdscr.addstr("1. Go back to Main Menu\n")
    stdscr.addstr("2. Go back to Sub Menu 1\n")
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key == ord('1'):
            stdscr.clear()
            stdscr.addstr("Enter 0 to disable or 1 to enable this service: ")
            stdscr.refresh()
            service_status = stdscr.getch() - ord('0')
        elif key == ord('2'):
            stdscr.clear()
            stdscr.addstr("Enter the URL: ")
            stdscr.refresh
            url = stdscr.getstr().decode('utf-8')
        elif key == ord('3'):
            main_menu(stdscr)
        elif key == ord('4'):
            sub_menu1_config_server(stdscr)

    return instance


def sub_menu2_dns_ntp(stdscr, instance):
    stdscr.clear()
    stdscr.addstr("Enable and Configure DNS & NTP monitoring\n")
    stdscr.addstr("5. Go back to Main Menu\n")
    stdscr.addstr("6. Go back to Sub Menu 1\n")
    stdscr.refresh()

    while True:
        key = stdscr.getch()

        if key == ord('5'):
            main_menu(stdscr)
        elif key == ord('6'):
            sub_menu1_config_server(stdscr)
    
    return instance

def sub_menu2_tcp_udp(stdscr, instance):
    stdscr.clear()
    stdscr.addstr("Enable and Configure TCP & UDP monitoring\n")
    stdscr.addstr("1. Go back to Main Menu\n")
    stdscr.addstr("2. Go back to Sub Menu 1\n")
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key == ord('1'):
            main_menu(stdscr)
        elif key == ord('2'):
            sub_menu1_config_server(stdscr)
    return instance

def main():
    curses.wrapper(main_menu)

if __name__ == "__main__":
    main()