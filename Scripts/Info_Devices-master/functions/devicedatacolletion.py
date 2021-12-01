#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script create database devices information.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.5.2"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguezpadilla@gmail.com"
__status__ = "Development"


from pymongo import MongoClient
from netmiko import Netmiko
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException


# Colores para impresion en pantalla.
color_reset = "\x1b[0m"
red = "\x1b[00;00;1;031m"
red_blink = "\x1b[00;00;05;031m"
magent = "\x1b[00;00;02;033m"
magent_blink = "\x1b[00;00;05;033m"
blue = "\x1b[00;00;1;034m"
blue_blink = "\x1b[00;00;5;034m"
green = "\x1b[00;00;01;092m"
green_blink = "\x1b[00;00;5;092m"


def DeviceDataColletion(ip_address):
    """
    Add device data to MongoDB.

    This function add data of Device to MongoDB like a file.
    """
    device = {
            "device_type": "cisco_ios",             # Tipo de dispositivo.
            "ip": ip_address,                       # IP Address.
            "username": "cesar",                    # Nombre de Usuario.
            "password": "cesar",                    # Password de usuario.
            "secret": "cesar",                      #
            }

    try:
        # Establish SSH conexion
        net_connect = Netmiko(**device)

        # Enter to Privilege mode
        net_connect.enable()

        # Define value to command
        command = "show version"

        # Send command 'show version' with TextFSM
        output = net_connect.send_command(command, use_textfsm=True)

        # Dictionary to device_info
        device_info = {}

        # Add Hostname to device_info
        device_info["Hostname"] = output[0].get("hostname")
        # Add Version number to device_info
        device_info["Version"] = output[0].get("version")

        # Check if "/" in ios name and strip
        ios_image = output[0]["running_image"]
        if "/" in ios_image:
            ios_image = ios_image.strip("/")
            device_info["IOS Image"] = ios_image
        else:
            device_info["IOS Image"] = ios_image

        # Add Serial Number to device_info
        device_info["Serial"] = output[0]["serial"][0]

        # Define value to command
        command = "show interfaces"
        # Send command 'show version' with TextFSM
        output = net_connect.send_command(command, use_textfsm=True)

        # Add interface list to device_info["Interfaces"]
        interfaces_list = []
        # Cicle for to interface on output
        for interface in output:
            # Interface Dictionary
            dict_interface = {}
            # Add interface type
            dict_interface["Interface"] = interface["interface"]
            # Add IP Address
            dict_interface["IP Address"] = interface["ip_address"]
            # Add Mac Address
            dict_interface["Mac Address"] = interface["address"]
            # Add Link status
            dict_interface["Link Status"] = interface["link_status"]
            # Add Description
            dict_interface["Description"] = interface["description"]
            # Add Protocol Status
            dict_interface["Protocol Status"] = interface["protocol_status"]
            # Add mtu
            dict_interface["MTU"] = interface["mtu"]
            # Add Duplex
            dict_interface["Duplex"] = interface["duplex"]
            # Add Speed
            dict_interface["Speed"] = interface["speed"]
            # Add Input errors
            dict_interface["Input Errors"] = interface["input_errors"]
            # Add Output Errors
            dict_interface["Output Errors"] = interface["output_errors"]

            # Add dictionary 'dict_interface' to interfaces_list
            interfaces_list.append(dict_interface)

        # 'Add interfaces_list' to 'device_info'
        device_info["Interfaces"] = interfaces_list

        # Disconnect Session SSH
        net_connect.disconnect()

        # Create connection with MongoDB
        with MongoClient("mongodb://localhost:27017/") as mongo_client:
            dbBranchOffice = mongo_client["BranchOffices"]
            dbBranchCollection = dbBranchOffice["Devices"]

            # Filter of consult
            filter = {
                "Serial": device_info["Serial"]
            }

            # Count if exist one coincidencia
            result = dbBranchCollection.count(filter=filter)

            # If result is '0' then
            if not result:
                dbBranchCollection.insert_one(device_info)
                print(
                    f"Add {device_info['Hostname']} with "
                    + f"{ip_address} device.")
            else:
                new_values = {
                    "$set": {
                        "Hostname": device_info["Hostname"],
                        "Interfaces": interfaces_list
                        }
                }
                dbBranchCollection.update(filter, new_values)
                print(
                    f"Update {device_info['Hostname']} with "
                    + f"{ip_address} device."
                )

    # Manejo de excepciones
    except NetMikoTimeoutException:
        print("No se encuentra el dispositivo.")
        print(f"""
{red}Common causes of this problem are:
1. Incorrect hostname or IP address.
2. Wrong TCP port.
3. Intermediate firewall blocking access.
            """)

    except NetMikoAuthenticationException:
        print("Credenciales equivocadas.")

    except KeyboardInterrupt:
        print(
            f"\n\n\t{red}Has detenido el {green}programa {red}con el teclado.")
