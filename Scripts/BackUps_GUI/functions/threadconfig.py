#!/usr/bin/env  python3
"""
This script is create for ping IPv4.

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


from threading import Thread


# Colores para impresion en pantalla.
color_reset = "\x1b[0m"
red = "\x1b[00;00;1;031m"
red_blink = "\x1b[00;00;05;031m"
magent = "\x1b[00;00;02;033m"
magent_blink = "\x1b[00;00;02;033m"
blue = "\x1b[00;00;1;034m"
blue_blink = "\x1b[00;00;5;034m"
green = "\x1b[00;00;01;092m"
green_blink = "\x1b[00;00;5;092m"


def ThreadConfigSSH(function, ip_list, data_info):
    """
    Funcion para la ejecucion de hilos para la configuracion simultanea.

    Realiza multiples conexiones creando hilos para dicha tarea.
    Para quitar los mensajes de los demas.
    """
    try:
        threads = []

        for ip in ip_list:
            th = Thread(target=function, args=(ip, data_info))
            th.start()
            threads.append(th)

        for th in threads:
            th.join()

    except KeyboardInterrupt:
        print("You canceled the operation with the keyboard")
