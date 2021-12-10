#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is create an application for create a topology view.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Alonso Salvador Rodriguez Padilla"
__copyright__ = "LLDP Relationships"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesar.ropadilla@alumnos.udg.mx"
__status__ = "Development"


# Import functions
from random import randint
from json import dumps
from os import getcwd
from netmiko import Netmiko
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException
from time import sleep
from datetime import datetime


def backUPConfig(ip, data_info):
    """
    Funcion para realizar configuracion default.

    Realiza multiples conexiones creando hilos para dicha tarea.
    Para quitar los mensajes de los demas.
    
    """
    


    username, password, secret, server = data_info
    remote_device = {
        'device_type': 'autodetect',     # Tipo de dispositivo.
        'ip': ip,                       # IP Address.
        'username': username,            # Nombre de Usuario.
        'password': password,             # Password de usuario.
        'secret': secret,               # Password enable secret.
        }

    
    try:
        net_connect = Netmiko(**remote_device, verbose=True)
        net_connect.enable()

        date_time = datetime.now().strftime("%H.%M.%S-%Y%m%d")
        net_connect.write_channel(f"copy startup-config tftp: \n")
        count = 0
        while True:
            sleep(1)

            output = net_connect.read_channel()

            if count == 15:
                break

            elif "Address or name of remote host []?" in output:
                net_connect.write_channel(f"{server}\n")
                output = net_connect.read_channel()
                continue

            elif "Destination filename" in output:
                net_connect.write_channel(f"{remote_device['ip']}_{date_time}_backup.txt\n")
                output = net_connect.read_channel()
                continue

            else:
                count += 1
                continue

        net_connect.disconnect()


    except NetMikoTimeoutException:
        print("No se encuentra el dispositivo.")

    except NetMikoTimeoutException:
        print(f"Device {ip} not found.")

    except NetMikoAuthenticationException:
        print(f"Wrong credentials in {ip}.")

    except SSHException:
        print(f"Channel Closed in {ip}")

    except KeyboardInterrupt:
        print("You canceled the operation with the keyboard")

    except EOFError:
        print("Other error.")
