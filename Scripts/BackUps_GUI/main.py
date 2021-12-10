#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is create an application for create a backups.

A function is defined that allows the creation of the graphical interface that
the neighbor relations project.
"""
__author__ = "Cesar Alonso Salvador Rodriguez Padilla"
__copyright__ = "LLDP Relationships"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguezpadilla@gmail.com"
__status__ = "Development"



# Import functions
from tkinter import Tk
from functions.BackUPGUI import BackUPGUI




def main():
    """
    Funcion Principal.

    Esta funcion llama a las demas funciones de la carpeta 'functions'.
    """
    mainwindow = Tk()
    # Create Principal Window
    BackUPGUI(mainwindow)

    mainwindow.mainloop()


if __name__ == "__main__":
    main()
