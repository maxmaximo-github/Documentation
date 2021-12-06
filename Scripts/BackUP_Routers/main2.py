#!/usr/bin/env  python3


from contextlib import closing
from datetime import datetime
from pathlib import Path
from socket import AF_INET
from socket import SOCK_STREAM
from socket import socket
from telnetlib import Telnet
from netmiko import Netmiko
from zipfile import ZipFile


def check_OpenPort(host, port):
    with closing(socket(AF_INET, SOCK_STREAM)) as isOpenPort:
        if isOpenPort.connect_ex((host, port)) == 0:
            return [host, port]
        else:
            port = 22
            if isOpenPort.connect_ex((host, port)) == 0:
                return [host, port]


def ssh_configuration(device):
    dev = {
        "device_type": "cisco_ios",
        "ip": device[0],
        "username": "onenetwork",
        "password": "Delunoal12345"
    }

    with Netmiko(**dev) as ssh_connection:
        output = ssh_connection.send_command("show startup-config")

    for line in output.splitlines():
        if "hostname" in line:
            hostname = line.split(" ")[-1]
        # elif "domain" in line:
        #     domain = line.split(" ")[-1]

    hostname = (f"{hostname}")
    
    with open(file=f"{directory}/{hostname}", mode="w") as file:
        file.write(output)


def telnet_configuration(device):
    with Telnet(host=device[0]) as tel_conn:
        # tel_conn.set_debuglevel(3)
        tel_conn.read_until(bytes("Username: ", encoding="ascii"))
        tel_conn.write(bytes("onenetwork\n", encoding="ascii"))
        tel_conn.read_until(bytes("Password: ", encoding="ascii"))
        tel_conn.write(bytes("Delunoal12345\n", encoding="ascii"))

        command_list = [
            "terminal leng 0", "show running-config", "exit" 
        ]

        for command in command_list:
            tel_conn.write(bytes(f" {command} \r\n", encoding="ascii"))

        output = str(tel_conn.read_all(), encoding="ascii")
        
    for line in output.splitlines():
        if "hostname" in line:
            hostname = line.split(" ")[-1]
        # elif "domain" in line:
        #     domain = line.split(" ")[-1]

    hostname = (f"{hostname}")

    with open(file=f"{directory}/{hostname}", mode="w") as file:
        file.write(output)

def main():
    Path("./tmp").mkdir(parents=True, exist_ok=True)
    date_time = datetime.now().strftime("%H.%M.%S_%Y-%m-%d")
    global directory
    Path(f"./tmp/{date_time}").mkdir(parents=True, exist_ok=True)
    directory = Path(f"./tmp/{date_time}")

    port = 23
    ip_list = [
        "192.168.165.250", "192.168.169.253", "192.168.200.110"
    ]

    list = []
    for ip in ip_list:
        answer = check_OpenPort(ip, port)
        list.append(answer)

    for device in list:
        if device[-1] == 23:
            telnet_configuration(device)
        else:
            ssh_configuration(device)

    
    with ZipFile(file=f"{directory}.zip", mode="w") as zipfile:
        for dir in directory.iterdir():
            zipfile.write(dir)

                
        


if __name__ == '__main__':
    main()