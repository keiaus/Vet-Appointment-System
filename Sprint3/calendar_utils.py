from tkinter import * # gui import
import tkinter as tk # gui import
from tkinter import ttk # necessary for comboboxes
import pyodbc # necessary for aws rds sql server connection
from tkcalendar import Calendar # gui import (must install tkcalendar "pip install tkcalendar")
from datetime import datetime
from datetime import date

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

    # This function displays the calendar
    def calendar_display(self):
        
        # This function retrieves the VetID, day, and time of vet appointments stored in VetScheduleInfo 
        def schedule_retrieval():

            sel = cb1.get().split(",")
            my_list = list()

            monday_vet_id = cursor.execute("SELECT Monday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list.append([r for r, in monday_vet_id])
            monday_label = Label(calendar_display_frame, text=f'{monday_vet_id}', font="times 20 bold")
            monday_label.grid(row=8, column=4)

            tuesday_vet_id = cursor.execute("SELECT Tuesday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list.append([r for r, in tuesday_vet_id])
            tuesday_label = Label(calendar_display_frame, text=f'{tuesday_vet_id}', font="times 20 bold")
            tuesday_label.grid(row=8, column=5)

            wednesday_vet_id = cursor.execute("SELECT Wednesday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list.append([r for r, in wednesday_vet_id])
            wednesday_label = Label(calendar_display_frame, text=f'{wednesday_vet_id}', font="times 20 bold")
            wednesday_label.grid(row=8, column=6)

            thursday_vet_id = cursor.execute("SELECT Thursday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list.append([r for r, in thursday_vet_id])
            thursday_label = Label(calendar_display_frame, text=f'{thursday_vet_id}', font="times 20 bold")
            thursday_label.grid(row=8, column=7)

            friday_vet_id = cursor.execute("SELECT Friday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list.append([r for r, in friday_vet_id])
            friday_label = Label(calendar_display_frame, text=f'{friday_vet_id}', font="times 20 bold")
            friday_label.grid(row=8, column=8)

            saturday_vet_id = cursor.execute("SELECT Saturday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list.append([r for r, in saturday_vet_id])
            saturday_label = Label(calendar_display_frame, text=f'{saturday_vet_id}', font="times 20 bold")
            saturday_label.grid(row=8, column=9)

            sunday_vet_id = cursor.execute("SELECT Sunday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list.append([r for r, in sunday_vet_id])
            sunday_label = Label(calendar_display_frame, text=f'{sunday_vet_id}', font="times 20 bold")
            sunday_label.grid(row=8, column=10)
            
            temp = my_list[0].split(":")
            string = temp[0] + " "  + temp[1] + " - " + temp[2] + " " + temp[3]
            Label(calendar_display_frame, text = f'{string}')

        #Calendar
        calendar_display_frame = tk.Frame(self.calendar_frame)
        calendar_display_frame.pack(side = "top", fill = "x")
        cal = Calendar(calendar_display_frame, selectmode = 'day', year = 2023, month = 3, day = 14)
        
        # ***Stores the selected date and vet***
        # ================================================================================================================
        date_label_2 = tk.Label(calendar_display_frame, text = f'Selected Date: {cal.get_date()}', font="Times 30 bold")
        vet_label_2 = tk.Label(calendar_display_frame, text = "Test", font="Times 30 bold") # Displays the vet selected
        # vet_label_2 = tk.Label(calendar_display_frame, text = f'{on_click()}', font="Times 30 bold") # Displays the vet selected

        cal.grid(row=3, column = 2)
        # ====================================
        date_label_2.grid(row = 0, column = 5)
        vet_label_2.grid(row=2, column=5)

        calendar_display_frame.grid_columnconfigure(0, weight=1)
        calendar_display_frame.grid_columnconfigure(5, weight=1)

        query = "SELECT Concat(VetID, ', ', VetFirstName, ', ', VetLastName) FROM VETACCOUNTINFO"
        
        ##drop down for vets
        global cal_view_vet_menu_label

        Label(calendar_display_frame, text = "").grid()
        cal_view_vet_menu_label = Label(calendar_display_frame, text = "Select a Vet", font = "times 15 bold")
        cal_view_vet_menu_label.grid(row=5, column=2)

        my_data = cursor.execute(query) # SQLAlchem engine result
        my_list = [r for r, in my_data] # create a list 

        sel=tk.StringVar()
        cb1 = ttk.Combobox(calendar_display_frame, values=my_list,width=15,textvariable = sel)
        cb1.grid(row=6, column=2)

        vet_label = tk.Label(calendar_display_frame, text = f'Selected Vet: {sel.get()}', font="Times 30 bold")
        vet_label.grid(row=1, column=5)

        # Onclick date
        def updateLabel(event):
            date_label_2.config(text = "Selected Date: " + cal.get_date())
            vet_label.config(text = "Selected Vet: " + sel.get())
            
            ######Finding position and parsing comma
            parseOutVetID = sel.get()
            parsedList=parseOutVetID.split(",")
            parsedVetID = parsedList[0]
            
            ###Finding day of the week
            date_str  = cal.get_date()
            dateObj = datetime.strptime(date_str,'%m/%d/%y')
            dayOftheWeek = dateObj.weekday()
            daysOfWeek = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
            selectedDay = daysOfWeek[dayOftheWeek]

            #date.replace()
            #dayOfWeek=date.isoweekday()
            #dtdate = pickedDate.split("/")
            #start_date = d(dtdate.index(2),dtdate.index(0),dtdate.index(1))
            #weekday = start_date.weekday()
            
            displayVetID.config(text = "###This needs to be vet ID### " + parsedVetID)
            DisplayDay.config(text = "###This the day of the week### " + selectedDay)

            # t.config(text = "Selected Vet: " + on_click())
        
        cal.bind("<<CalendarSelected>>", updateLabel)

        # queryVetSchedule = "SELECT Concat(VetID, ', ', VetFirstName, ', ', VetLastName) FROM VETACCOUNTINFO"

        ##date_label = tk.Label(calendar_display_frame, text = "Selected Date: ")
        ##date_label.grid(row=2, column=0)

        ##############################
        ##this needs to display VET ID 
        ##############################
        displayVetID = tk.Label(calendar_display_frame, text = sel)
        displayVetID.grid(row=1, column=2)

        DisplayDay = tk.Label(calendar_display_frame, text = sel)
        DisplayDay.grid(row=3, column=1)

        schedule_retrieval()