#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is create an application for create a topology view.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020, Ping IPv4 Branche Offices Devices"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "0.4.5"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguez@gmail.com"
__status__ = "Development"


# Import functions
from tkinter import Tk
from functions.Devices import Devices


def main():
    """
    Funcion Principal.

    Esta funcion llama a las demas funciones de la carpeta 'functions'.
    """
    mainwindow = Tk()
    # Create Principal Window
    Devices(mainwindow)

    mainwindow.mainloop()


if __name__ == "__main__":
    main()
