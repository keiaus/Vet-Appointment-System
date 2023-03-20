from tkinter import * # gui import
import tkinter as tk # gui import
from tkinter import ttk # necessary for comboboxes
import pyodbc # necessary for aws rds sql server connection
from userfile import *
from vetfile import *
from adminfile import *

#Connection to AWS RDS SQL Server (required to run properly)
connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=Arthur;PWD=123;')
cursor = connection.cursor()


def calendar_display():
    cal = Calendar(calendar, selectmode = 'day', year = 2023, month = 3, day = 14)
    cal.pack(pady = 300)
    
    date = Label(calendar, text = "")
    date.pack(pady = 20)
