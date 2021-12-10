#!/usr/bin/env  python3

from datetime import datetime
from contextlib import closing
from socket import AF_INET
from socket import SOCK_STREAM
from socket import socket
from telnetlib import Telnet
from netmiko import Netmiko


def check_OpenPort(host, port):
    with closing(socket(AF_INET, SOCK_STREAM)) as isOpenPort:
        if isOpenPort.connect_ex((host, port)) == 0:
            return (host, port)
        else:
            port = 22
            if isOpenPort.connect_ex((host, port)) == 0:
                return (host, port)


def ssh_configuration(device, date_time):
    dev = {
        "device_type": "cisco_ios",
        "ip": device[0],
        "username": "cesar",
        "password": "cesar"
    }

    with Netmiko(**dev) as ssh_connection:
        output = ssh_connection.send_command("show startup-config")

    date_time = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    with open(file=f"{dev['ip']}-{date_time}", mode="w") as file:
        file.write(output)


def telnet_configuration(device, date_time):
    with Telnet(host=device[0]) as tel_conn:
        # tel_conn.set_debuglevel(3)
        tel_conn.read_until(bytes("Username: ", encoding="ascii"))
        tel_conn.write(bytes("cesar\n", encoding="ascii"))
        tel_conn.read_until(bytes("Password: ", encoding="ascii"))
        tel_conn.write(bytes("cesar\n", encoding="ascii"))
        tel_conn.write(bytes("terminal leng 0 \r\n", encoding="ascii"))
        tel_conn.write(bytes("show startup-config \r\n", encoding="ascii"))
        tel_conn.write(bytes("exit \r\n", encoding="ascii"))

        output = str(tel_conn.read_all(), encoding="ascii")

    with open(file=f"{device[0]}-{date_time}", mode="w") as file:
        file.write(output)

def main():
    date_time = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    port = 23
    ip_list = [
        "192.168.100.1", "192.168.100.5"
    ]

    list = []
    for ip in ip_list:
        answer = check_OpenPort(ip, port)
        list.append(answer)

    for device in list:
        if device[-1] == 23:
            telnet_configuration(device, date_time)

        else:
            ssh_configuration(device, date_time)

    print("Hello World")


if __name__ == '__main__':
    main()
