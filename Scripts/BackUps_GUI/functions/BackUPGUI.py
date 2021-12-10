#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is create a Windows for Add new Devices.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
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
from datetime import datetime
from pathlib import Path
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
# Own libraries
from functions.backUPConfig import backUPConfig
from functions.threadconfig import ThreadConfigSSH


class BackUPGUI:
    """
    Create Window Template.

    Create window template for application.
    """

        # Constructor Mode
    def __init__(self, window):
        """
        Mode Constructor.

        Mode constructor.
        """
        self.wind = window
        self.wind.title("BackUP GUI")
        self.wind.geometry("420x500")

        # Creating a Frame Container
        frame = LabelFrame(self.wind, text="New Device")
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

        # Tree1 table
        tupleColumns = ("#1", "#2")
        self.tree = ttk.Treeview(
                                height=5,
                                columns=tupleColumns,
                                selectmode="extended",
                                show="headings")

        self.tree.grid(row=5, column=0, columnspan=3)
        self.tree.heading("#1", text="Name", anchor="center")
        self.tree.heading("#2", text="IP address", anchor="center")

        # Buttons
        Button(
            text="Delete", command=self.delete_device).grid(
                                    row=6, column=0, stick="w"+"e")
        Button(
            text="Update", command=self.edit_device).grid(
                                    row=6, column=1, stick="w"+"e")

        # Filling the Rows
        self.get_devices()

        # Creating a Frame Container
        frame2 = LabelFrame(self.wind, text="Server BackUP")
        frame2.grid(row=7, column=0, columnspan=4, pady=20)

        # Server Input
        Label(master=frame2, text="IPv4/v6 or hostname: ").grid(row=1, column=0)
        self.server = Entry(frame2)
        self.server.focus()
        self.server.grid(row=1, column=1)

        Button(
            master=frame2, text="Add Server", command=self.addServer).grid(
                                        row=1, column=2, stick="w"+"e")
        
        tupleColumns2 = ("#1",)
        self.tree2 = ttk.Treeview(
                                    master=frame2,
                                    height=1,
                                    columns=tupleColumns2,
                                    selectmode="extended",
                                    show="headings")


        self.tree2.grid(row=10, column=0, columnspan=3)
        self.tree2.heading("#1", text="Server", anchor="center")


        Button(
            text="BackUP", command=self.user_data).grid(
                                row=11, column=1, stick="w"+"e")

    
    def validationServer(self): 
        print("Hello World")
        if (len(self.server.get()) !=0):
            return True


    def addServer(self):

        record = self.tree2.get_children()
        for element in record:
            self.tree2.delete(element)

        if self.validationServer():
            server = self.server.get()


            message = (
                    f"El servidor {server} se agregado correctamente")
            self.message["text"] = message
            self.server.delete(0, END)
            self.tree2.insert(
            "", 0,
                text="Server", values=(server))

        else:
            self.message["text"] = "El nombre del servidor es requerido."



    def backUP(self, username_entry, password_entry, secret_entry):
        """
        BackUp Function.


        BackUp Function.
        """
        self.data_user.destroy()

        for child in self.tree2.get_children():
            server = self.tree2.item(child)["values"]
        server = server[-1]

        start_time = datetime.now()

        data_info = [
            username_entry, password_entry, secret_entry,
            server
        ]

        query = {}
        db_rows = self.run_query(query)

        ip_list = []
        for row in db_rows:
            ip_list.append(row["IP_Address"])

        
        ThreadConfigSSH(backUPConfig, ip_list, data_info)


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

        return result

    def run_query2(self, query, arguments=[]):
        """
        Mode Constructor.

        Metodo constructor.
        """
        mongo_client, dbDevices, dbDevicesColl = self.mongo_client2()

        if len(arguments) == 0:
            result = dbDevicesColl.find(filter=query)
        else:
            result = dbDevicesColl.find(
                                    filter=query,
                                    sort=arguments[0],
                                    limit=arguments[1])

        return result

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

    def delete_query(self, query):
        """
        Mode Constructor.

        Metodo constructor.
        """
        mongo_client, dbDevices, dbDevicesColl = self.mongo_client()

        # Delete Element
        dbDevicesColl.delete_one(filter=query)

        mongo_client.close()

    def update_query(self, query, new_values):
        """
        Mode Constructor.

        Metodo constructor.
        """
        mongo_client, dbDevices, dbDevicesColl = self.mongo_client()

        # Update Element
        dbDevicesColl.update_one(query, new_values)

        # Close MongoClient
        mongo_client.close()

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

    # Validation Input User
    def validation(self):
        """
        Validate Device.

        Validation Device.
        """
        if (len(self.name.get()) != 0 and len(self.IP_Address.get()) != 0):
            return True

    # Count Documents
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

    # Add New Device
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

    def delete_device(self):
        """
        Mode Constructor.

        Mode Constructor.
        """
        self.message["text"] = ""
        try:
            self.tree.item(self.tree.selection())["values"][0]
        except IndexError:
            self.message["text"] = "Por favor seleccione un registro."
            return
        self.message["text"] = ""
        data = self.tree.item(self.tree.selection())['values']
        name, ip_address = data[0], data[-1]
        # Query
        query = {
            "Name": name
        }
        self.delete_query(query)
        message = (
                f"El dispositivo {name} con {ip_address}"
                + f" fue eliminado correctamente")
        self.message["text"] = message
        self.get_devices()

    def edit_device(self):
        """
        Edit Devices.

        Function for edit devices.
        """
        self.message["text"] = ""
        try:
            self.tree.item(self.tree.selection())["values"][0]
        except IndexError:
            self.message["text"] = "Por favor seleccione un registro"
            return
        data = self.tree.item(self.tree.selection())['values']
        name, ip_address = data[0], data[-1]
        self.edit_wind = Toplevel()
        self.edit_wind.title("Editar Dispositivo")

        # Old Name
        Label(self.edit_wind, text="Anterior Nombre").grid(row=0, column=1)
        Entry(
            self.edit_wind,
            textvariable=StringVar(self.edit_wind, value=name),
            state="readonly").grid(row=0, column=2)
        # New Name
        Label(self.edit_wind, text="Nuevo Nombre").grid(row=1, column=1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row=1, column=2)

        # Old IP
        Label(
            self.edit_wind, text="Anterior Direccion IP").grid(row=2, column=1)
        Entry(
            self.edit_wind,
            textvariable=StringVar(self.edit_wind, value=ip_address),
            state="readonly").grid(row=2, column=2)
        # New IP
        Label(self.edit_wind, text="Nueva Direccion IP").grid(row=3, column=1)
        new_ip_address = Entry(self.edit_wind)
        new_ip_address.grid(row=3, column=2)

        Button(
            self.edit_wind,
            text="Actualizar",
            command=lambda: self.edit_query(
                name, new_name.get(),
                new_ip_address.get())).grid(
                                            row=4, column=2, stick="w"+"e")
        self.edit_wind.mainloop()

    def edit_query(self, name, new_name, new_ip_address):
        """
        Validate Branch.

        Validation Branch.
        """
        mongo_client, dbDevices, dbDevicesColl = self.mongo_client()

        query = {
            "Name": name,
        }

        new_values = {
            "$set": {
                "Name": new_name,
                "IP_Address": new_ip_address
            }
        }

        dbDevicesColl.update_one(query, new_values)

        self.edit_wind.destroy()
        message = f"Dispositivo {new_name} con IP {new_ip_address}"
        self.message["text"] = message
        self.get_devices()

    def user_data(self):
        """
        LLDP Discovery.

        Function for discover relationship with neighbors using LLDP Protocol.
        """
        self.data_user = Toplevel()
        self.data_user.title("Login")
        self.data_user.geometry("315x500")
        self.data_user.configure(background="white")

        directory = Path.cwd()
        image_file = PhotoImage(file=f"{directory}/image/lapiz.png")
        imagen_label = Label(self.data_user, image=image_file, bg="white")
        imagen_label.pack()

        Label(
            self.data_user,
            text="Por favor ingresa las credenciales",
            bg="white",
            font=("Helvtica", 15)).pack()

        Label(
            self.data_user,
            text="Para dispositivos de capa 2 y 3.",
            bg="white",
            font=("Helvtica", 15)).pack()

        Label(
            self.data_user,
            text="Username:",
            bg="white",
            font=("Helvtica", 15),
            fg="black").pack()

        username_entry = Entry(
                            self.data_user,
                            bg="white",
                            font=("Helvtica", 15))
        username_entry.focus()
        username_entry.pack()

        Label(
            self.data_user,
            text="Password:",
            bg="white",
            font=("Helvtica", 15),
            fg="black").pack()

        password_entry = Entry(
                            self.data_user,
                            bg="white",
                            font=("Helvtica", 15),
                            show='●')
        password_entry.pack()

        Label(
            self.data_user,
            text="Secret:",
            bg="white",
            font=("Helvtica", 15),
            fg="black").pack()

        secret_entry = Entry(
                            self.data_user,
                            bg="white",
                            font=("Helvtica", 15),
                            show='●')
        secret_entry.pack()

        login_button = Button(
                        self.data_user,
                        text="Login",
                        command=lambda: self.backUP(
                            username_entry.get(),
                            password_entry.get(),
                            secret_entry.get()))
        login_button.bind("<Return>", self.backUP)
        login_button.pack()

        self.data_user.mainloop()
