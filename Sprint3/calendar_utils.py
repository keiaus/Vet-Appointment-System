from tkinter import * # gui import
import tkinter as tk # gui import
from tkinter import ttk # necessary for comboboxes
import pyodbc # necessary for aws rds sql server connection
from tkcalendar import Calendar # gui import (must install tkcalendar "pip install tkcalendar")
from datetime import datetime

#Connection to AWS RDS SQL Server (required to run properly)
connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=Arthur;PWD=123;')
cursor = connection.cursor()

class CalendarUtils():

    def __init__(self, window, calendar_frame):
        super().__init__()
        self.window = window
        self.calendar_frame = calendar_frame
    
    def show_frame(self,frame):
        frame.tkraise()

    def calendar_display_clicked(self):
        self.window.title("Calendar Display")
        self.show_frame(self.calendar_frame)

    def calendar_display(self):

        #Calendar
        calendar_display_frame = tk.Frame(self.calendar_frame)
        calendar_display_frame.pack(side = "top", fill = "x")

        cal = Calendar(calendar_display_frame, selectmode = 'day', year = 2023, month = 3, day = 14)
        date_label_2 = tk.Label(calendar_display_frame, text = f'Selected Date: {cal.get_date()}', font="Times 30 bold")
        vet_label = tk.Label(calendar_display_frame, text = f'Selected Vet: {cb_clicked()}', font="Times 30 bold")
        vet_label_2 = tk.Label(calendar_display_frame, text = "Test", font="Times 30 bold") # Displays the vet selected
        # vet_label_2 = tk.Label(calendar_display_frame, text = f'{on_click()}', font="Times 30 bold") # Displays the vet selected

        cal.grid(row=3, column = 2)
        date_label_2.grid(row = 0, column = 5)
        vet_label.grid(row=1, column=5)
        vet_label_2.grid(row=2, column=5)

        calendar_display_frame.grid_columnconfigure(0, weight=1)
        calendar_display_frame.grid_columnconfigure(5, weight=1)

        query = "SELECT Concat(VetID, ', ', VetFirstName, ', ', VetLastName) FROM VETACCOUNTINFO"

        # Onclick date
        # def updateLabel(event):
        #     date_label_2.config(text = "Selected Date: " + cal.get_date())
        #     t.config(text = "Selected Vet: ")
            # t.config(text = "Selected Vet: " + on_click())
        
        # cal.bind("<<CalendarSelected>>", updateLabel)
    
        # date_label = tk.Label(calendar_display_frame, text = "Selected Date: ")
        # date_label.grid(row=2, column=0)

        # t = tk.Label(calendar_display_frame, text = "Selected Vet: ")
        # t.grid(row=3, column=0)

        ##drop down for vets
        global cal_view_vet_menu_label

        Label(calendar_display_frame, text = "").grid()
        cal_view_vet_menu_label = Label(calendar_display_frame, text = "Select a Vet", font = "times 15 bold")
        cal_view_vet_menu_label.grid(row=4, column=0)

        my_data = cursor.execute(query) # SQLAlchem engine result
        my_list = [r for r, in my_data] # create a list 

        sel=tk.StringVar()

        cb1 = ttk.Combobox(calendar_display_frame, values=my_list,width=15,textvariable = sel)
        cb1.grid(row=5, column=0)

        def cb_clicked():
            selected_vet = Label(calendar_display_frame, text= f'{cb1.get()}')
            selected_vet.grid(row=4, column=0)
            
            # Label(calendar_display_frame, text = f'{selected_vet}', font="times 15 bold").grid(row=1, column=5)

        # def on_click():
        #     selected_vet = Label(calendar_display_frame, text=f'{cb1.get()}')
        #     selected_vet.grid(row=3, column=5)
            # selected_vet = f'{cb1.get()}'
            

    # # This function displays the calendar
    # def calendar_display():
    #     cal = Calendar(calendar, selectmode = 'day', year = 2023, month = 3, day = 14)
    #     cal.pack(pady = 300)
        
    #     date = Label(calendar, text = "")
    #     date.pack(pady = 20)
        
    #     cal.pack()
        
    #     query= "SELECT Concat(VetID, ', ', VetFirstName, ', ', VetLastName) FROM VETACCOUNTINFO"

        # ##onclick date
        # def updateLabel(event):
        #     label.config(text = "Selected Date: " + cal.get_date())
        #     t.config(text = "Selected Vet: " + on_click())
        
        # cal.bind("<<CalendarSelected>>", updateLabel)
    
    #     label = tk.Label(calendar, text = "Selected Date: ")

    #     label.pack()
    #     t = tk.Label(calendar, text = "Selected Date: ")
    #     t.pack()


    #     ##drop down for vets
    #     global cal_view_vet_menu_label

    #     Label(calendar, text = "").pack()
    #     cal_view_vet_menu_label = Label(calendar, text = "View/Delete Veterinarians Menu", font = "times 15")
    #     cal_view_vet_menu_label.pack()

    #     my_data = cursor.execute(query) # SQLAlchem engine result
    #     my_list = [r for r, in my_data] # create a  list 

    #     sel=tk.StringVar()

    #     cb1 = ttk.Combobox(calendar, values=my_list,width=15,textvariable = sel)
    #     cb1.pack(padx=30,pady=30)

    #     def on_click():
    #         selected_vet = f'{my_list}'
    #         return selected_vet