#!/usr/bin/python3
from script import *


def main_menu():
    cp('-'*20)
    cp('1.Display available RAM')
    cp('2.Display load average')
    cp('3.Display Hostname details')
    cp('4.Display All process count')
    cp('5.Display uptime')
    cp('6.Exit')
    cp('-'*20)


if __name__ == '__main__':
    while True:
        main_menu()
        ch = int(input('Enter choice : '))
        if ch == 1:
            display_aval_RAM()
        elif ch == 2:
            display_load_avg()
        elif ch == 3:
            hostname_details()
        elif ch == 4:
            process_count()
        elif ch == 5:
            display_uptime()
        elif ch == 6:
            break
        else:
            console.print('oops ! wrong option  ', style='bold red')
