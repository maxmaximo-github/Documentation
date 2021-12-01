#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is create for ping IPv4 devices..
It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020, Ping IPv4 Branche Offices Devices"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguez@gmail.com"
__status__ = "Development"


# Import functions
# Import Own Functions
from functions.clearscreen import ClearScreen
from functions.createtmpfolder import CreateTMPFolder
from functions.jsonformat import JSONDataImport
from functions.inputoption import InputOption
from functions.menu import Menu
from functions.pingbranches import PingBranches
from functions.removefiles import RemoveFiles
from functions.rebootbranchesphones import RebootBranchesPhones


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
    Funcion Principal.
    Esta funcion llama a las demas funciones de la carpeta 'functions'.
    """
    # Clear Screen
    try:
        # Cleaner
        ClearScreen()

        # Create tmp folder if not exit
        CreateTMPFolder()

        # Remove tmp files
        RemoveFiles()

        branches = JSONDataImport()

        # Conditional for enter in while cicle
        if branches is not False:
            cicle = True
        else:
            cicle = False

        while cicle:
            # Cleaner
            ClearScreen()

            # Print Menu
            Menu()

            input_user = InputOption()

            # Condiciones de ejecucion del programa
            if input_user == 1:
                confirmation = PingBranches(branches)

                if confirmation:
                    continue
                else:
                    break

            elif input_user == 2:
                confirmation = RebootBranchesPhones(branches)

                if confirmation:
                    continue
                else:
                    break

            else:
                print("\n")
                break

    except KeyboardInterrupt:
        print(
            f"\n\n\t{red}Has detenido el {green}programa {red}con el teclado.")

    except UnboundLocalError:
        print()

    # except TypeError:
    #     print("No selecionaste algun archivo.")

    finally:
        print(f"{green}{'Fin del programa':^60}{color_reset}\n")
        print(f" {red}{'*'*66}")
        print(
            f"      {blue}Desarrollado y mantenido"
            + f" por: {green}Ing. {__author__}")
        print(f"\t    {blue}Contacto: {green}{__email__}")
        print(f"\t\t        {blue}Version: {green}{__version__}")
        print(f" {red}{'*'*66}{color_reset}\n\n")


if __name__ == '__main__':
    main()