#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is create a Windows for Add new Devices.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020, LLDP Neighbors"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.4.5"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguez@gmail.com"
__status__ = "Development"


# Import functions
# import threading
from os import getcwd
from pymongo import MongoClient
from tkinter import ttk
from tkinter import Button
from tkinter import Entry
from tkinter import END
from tkinter import Label
from tkinter import LabelFrame
from tkinter import PhotoImage
from tkinter import StringVar
from tkinter import Toplevel
# Libraries own
from functions.CreateTMPFolder import CreateTMPFolder
# from functions.defaultconfig import defaultConfig
# from functions.graphvis import graphicsVIS
# from functions.lldp import lldpConfig
# from functions.removefiles import RemoveFiles
# from functions.threadconfig import ThreadConfigSSH


class Devices:
    """
    Mode Devices.

    Mode Devices.
    """

    # Constructor Mode
    def __init__(self, window):
        """
        Mode Constructor.

        Metodo constructor.
        """
        self.wind = window
        self.wind.title("LLDP/CDP Discovery")
        self.wind.geometry("400x550")

        # Creating a Frame Container
        frame = LabelFrame(self.wind, text="Register a new Device")
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Name Input
        Label(master=frame, text="Name: ").grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)

        # IPv4 Input
        Label(master=frame, text="IPv4/6: ").grid(row=2, column=0)
        self.IP_Address = Entry(frame)
        self.IP_Address.grid(row=2, column=1)

        # Button Save
        Button(
            master=frame,
            text="Add Device", command=self.add_device).grid(
                                    row=3, columnspan=2, sticky="w"+"e")

        # Output Messages
        self.message = Label(text="", anchor="center")
        self.message.grid(row=3, column=0, columnspan=2, sticky="w"+"e")

        # Tree table
        tupleColumns = ("#1", "#2")
        self.tree = ttk.Treeview(
                                height=15,
                                columns=tupleColumns,
                                selectmode="extended",
                                show="headings")

        self.tree.grid(row=5, column=0, columnspan=3)
        self.tree.heading("#1", text="Name", anchor="center")
        self.tree.heading("#2", text="IP Address", anchor="center")

        # Buttons
        Button(
            text="Delete").grid(
                                    row=6, column=0, stick="w"+"e")
        Button(
            text="Edit").grid(
                                    row=6, column=1, stick="w"+"e")
        Button(text="LLDP Discovery").grid(
                                    row=8, column=0, stick="w"+"e")
        Button(text="CDP Discovery").grid(row=8, column=1, stick="w"+"e")

        # Filling the Rows
        self.get_devices()


    def get_devices(self):
        """
        Mode Constructor.

        Metodo constructor.
        """
        # Query
        query = {
            "$query": {},
            "$orderby": {
                "Number": -1
                }
            }

        # Cleaning table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        # Query data
        db_rows = self.run_query(query)

        # Filling data
        for row in db_rows:
            self.tree.insert(
                    "", 0,
                    text=row["Number"],
                    values=(
                        row["Name"],
                        row["IP_Address"]))


    def run_query(self, query, arguments=[]):
        """
        Mode Constructor.

        Metodo constructor.
        """
        mongo_client, dbDevices, dbDevicesColl = self.mongo_client()

        if len(arguments) == 0:
            result = dbDevicesColl.find(filter=query)
        else:
            result = dbDevicesColl.find(
                                    filter=query,
                                    sort=arguments[0],
                                    limit=arguments[1])

        print(result)
        return result


    def mongo_client(self):
        """
        Mode Constructor.

        Mode Constructor.
        """
        nameDatabase = "DBDevices"
        nameDatabaseCollection = "Devices"

        mongo_client = MongoClient("mongodb://localhost:27017/")

        dblist = mongo_client.list_database_names()

        if nameDatabase not in dblist:
            # Connect to DBDatabase.
            dbDevices = mongo_client[nameDatabase]
            # Connect to Devices Collection.
            dbDevicesColl = dbDevices[nameDatabaseCollection]

        else:
            # Connect to DBDatabase.
            dbDevices = mongo_client[nameDatabase]
            # Connect to LLDP Collection.
            dbDevicesColl = dbDevices[nameDatabaseCollection]

        return mongo_client, dbDevices, dbDevicesColl

    
    def add_query(self, parameters):
        """
        Mode Constructor.

        Metodo constructor.
        """
        mongo_client, dbDevices, dbDevicesColl = self.mongo_client()

        device = {}
        device["Number"] = parameters[0]
        device["Name"] = parameters[1]
        device["IP_Address"] = parameters[2]
        dbDevicesColl.insert_one(device)

        mongo_client.close()

    def add_device(self):
        """
        Validate Branch.

        Validation Branch.
        """
        # Verificar if exist one element.
        parameter = True
        count = self.count_devices(parameter)

        if count != 0:
            # Query
            query = {}
            sort = list(
                {
                    'Number': -1
                }.items())
            limit = 1

            arguments = [sort, limit]

            # Query data to find 'Number id'
            db_rows = self.run_query(query, arguments)
            for row in db_rows:
                if row["Number"] is not None:
                    number = row["Number"]
                    number = int(number)
                    number += 1
        elif count == 0:
            number = count + 1

        if self.validation():
            name, ip_address = self.name.get(), self.IP_Address.get()
            parameters = (number, name, ip_address)
            self.add_query(parameters)
            message = (
                    f"El dispositivo {name} con {ip_address}"
                    + f" ha sido agregado correctamente.")
            self.message["text"] = message
            self.name.delete(0, END)
            self.IP_Address.delete(0, END)

        else:
            self.message["text"] = "Nombre e IP del dispositivo es requerido."
        self.get_devices()


    def count_devices(self, parameter=True):
        """
        Mode Constructor.

        Metodo constructor.
        """
        if parameter:
            mongo_client, dbDevices, dbDevicesColl = self.mongo_client()
        else:
            mongo_client, dbDevices, dbDevicesColl = self.mongo_client2()

        count = dbDevicesColl.estimated_document_count()

        mongo_client.close()

        return count

    # Validation Input User
    def validation(self):
        """
        Validate Device.

        Validation Device.
        """
        if (len(self.name.get()) != 0 and len(self.IP_Address.get()) != 0):
            return True