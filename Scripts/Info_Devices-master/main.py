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
__version__ = "0.3.2"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguezpadilla@gmail.com"
__status__ = "Development"


from functions.devicedatacolletion import DeviceDataColletion
from functions.threadconfig import ThreadConfig


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


def main():
    """
    Principal Funciotion.

    In there are functions to calls.
    """
    try:
        ip_list = [
            "192.168.100.1", "192.168.100.2",
            "192.168.100.3", "192.168.100.4"
            ]

        ThreadConfig(DeviceDataColletion, ip_list)

    except KeyboardInterrupt:
        print(
            f"\n\n\t{red}Has detenido el {green}programa {red}con el teclado.")

    except UnboundLocalError:
        print()

    finally:
        print(f"{green}{'Fin del programa':^60}{color_reset}\n")
        print(f" {red}{'*'*66}")
        print(
            f"      {blue}Desarrollado y mantenido"
            + f" por: {green}Ing. {__author__}")
        print(f"\t    {blue}Contacto: {green}{__email__}")
        print(f"\t\t        {blue}Version: {green}{__version__}")
        print(f" {red}{'*'*66}{color_reset}\n\n")


if __name__ == "__main__":
    main()
