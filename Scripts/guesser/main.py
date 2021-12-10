#!/usr/bin/env python3


from netmiko.terminal_server.terminal_server import TerminalServerTelnet

from logging import basicConfig
from logging import DEBUG
from logging import getLogger

from netmiko import SSHDetect
from netmiko import BaseConnection
from netmiko import Netmiko



basicConfig(filename="test.log", level=DEBUG)
logger = getLogger("netmiko")



def sshDetect(ip):
    device = {
        "device_type": "autodetect",
        "ip": ip,
        "username": username,
        "password": password,
        "session_log": "output.txt"
    }

    guesser = SSHDetect(**device).autodetect()

    return guesser




def main():

    global username
    global password
    username = "admin"
    password = "ant@huawei.com"
    ip = "192.168.90.254"

    print("Hola Mundo")

    # guesser = sshDetect(ip)

    # print(guesser)

    device = {
        "device_type": "huawei",
        "ip": ip,
        "username": username,
        "password": password,
        "session_log": "output.txt"
    }


    telnet_connection = TerminalServerTelnet(**device)
    output = telnet_connection.telnet_login()
    print(output)


if __name__ == "__main__":
    main()