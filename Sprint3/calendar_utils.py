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

    def __init__(self, window, calendar_frame, account_page):
        super().__init__()
        self.window = window
        self.calendar_frame = calendar_frame
        self.account_page = account_page
    
    def show_frame(self,frame):
        frame.tkraise()

    def calendar_display_clicked(self):
        self.window.title("Calendar Display")
        self.show_frame(self.calendar_frame)

    def return_to_main(self):
        self.window.title("Home")
        self.show_frame(self.account_page)

    # This function displays the calendar
    def calendar_display(self):

        global schedule_label

        #Calendar
        calendar_display_frame = tk.Frame(self.calendar_frame)
        calendar_display_frame.pack(anchor = "nw", side=LEFT, expand=False, fill = "both")
        cal = Calendar(calendar_display_frame, selectmode = 'day', year = 2023, month = 3, day = 14)

        
        # # ***Stores the selected date and vet***
        # # ================================================================================================================
        # date_label_2 = tk.Label(calendar_display_frame, text = f'Selected Date: {cal.get_date()}', font="Times 30 bold")
        # vet_label_2 = tk.Label(calendar_display_frame, text = "Test", font="Times 30 bold") # Displays the vet selected
        # # vet_label_2 = tk.Label(calendar_display_frame, text = f'{on_click()}', font="Times 30 bold") # Displays the vet selected

        cal.grid(row=0, column = 3)
        # # ====================================
        # date_label_2.grid(row = 0, column = 5)
        # vet_label_2.grid(row=2, column=5)

        calendar_display_frame.grid_columnconfigure(0, weight=1)
        calendar_display_frame.grid_columnconfigure(6, weight=1)

        schedule_label = Frame(self.calendar_frame)
        schedule_label.pack(side=LEFT, fill="x", anchor="ne")
        schedule_label.grid_columnconfigure(0, weight=1)
        schedule_label.grid_columnconfigure(6, weight=1)

        query = "SELECT Concat(VetID, ', ', VetFirstName, ', ', VetLastName, ', ', Specialization) FROM VETACCOUNTINFO"
        
        ##drop down for vets
        global cal_view_vet_menu_label

        vet_dropdown_frame = tk.Frame(self.calendar_frame)
        vet_dropdown_frame.pack( fill="x", anchor="n")
        cal_view_vet_menu_label = Label(vet_dropdown_frame, text = "Select a Vet", font = "times 15 bold")
        cal_view_vet_menu_label.grid(row=1, column=1)

        vet_dropdown_frame.grid_columnconfigure(0, weight=1)
        vet_dropdown_frame.grid_columnconfigure(2, weight=1)

        my_data = cursor.execute(query) # SQLAlchem engine result
        my_list = [r for r, in my_data] # create a list 

        sel=tk.StringVar()
        cb1 = ttk.Combobox(vet_dropdown_frame, values=my_list,width=25,textvariable = sel)
        cb1.grid(row=2, column=1)

        Button(vet_dropdown_frame, text="Return to Main Menu", width=20, height=1, font='times 10 bold', bd=20, bg='SpringGreen4', command = self.return_to_main).grid(row=2, column=3)

        # vet_label = tk.Label(calendar_display_frame, text = f'Selected Vet: {sel.get()}', font="Times 30 bold")
        # vet_label.grid(row=1, column=5)

        # This function displays the vet schedule times 
        # Onclick date
        # def updateLabel(event):
        #     date_label_2.config(text = "Selected Date: " + cal.get_date())
        #     vet_label.config(text = "Selected Vet: " + sel.get())
            
        #     ######Finding position and parsing comma
        #     parseOutVetID = sel.get()
        #     parsedList=parseOutVetID.split(",")
        #     parsedVetID = parsedList[0]
            
        #     ###Finding day of the week
        #     date_str  = cal.get_date()
        #     dateObj = datetime.strptime(date_str,'%m/%d/%y')
        #     dayOftheWeek = dateObj.weekday()
        #     daysOfWeek = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
        #     selectedDay = daysOfWeek[dayOftheWeek]

        #     #date.replace()
        #     #dayOfWeek=date.isoweekday()
        #     #dtdate = pickedDate.split("/")
        #     #start_date = d(dtdate.index(2),dtdate.index(0),dtdate.index(1))
        #     #weekday = start_date.weekday()
            
        #     displayVetID.config(text = "###This needs to be vet ID### " + parsedVetID)
        #     DisplayDay.config(text = "###This the day of the week### " + selectedDay)

            # t.config(text = "Selected Vet: " + on_click())

        # queryVetSchedule = "SELECT Concat(VetID, ', ', VetFirstName, ', ', VetLastName) FROM VETACCOUNTINFO"

        ##date_label = tk.Label(calendar_display_frame, text = "Selected Date: ")
        ##date_label.grid(row=2, column=0)

        ##############################
        ##this needs to display VET ID 
        ##############################
        # displayVetID = tk.Label(calendar_display_frame, text = sel)
        # displayVetID.grid(row=1, column=2)

        # DisplayDay = tk.Label(calendar_display_frame, text = sel)
        # DisplayDay.grid(row=3, column=1)
        
        # This function retrieves the VetID, day, and time of vet appointments stored in VetScheduleInfo 
        def schedule_retrieval(event):

            global schedule_label

            sel = cb1.get().split(",")

            my_list1 = list()
            my_list2 = list()
            my_list3 = list()
            my_list4 = list()
            my_list5 = list()
            my_list6 = list()
            my_list7 = list()
            
            Label(schedule_label, text="Vet Schedule", font="Times 10 bold").grid(row=0, column=2)

            Label(schedule_label, text="Monday", font="Times 10 bold").grid(row=1, column=1)
            monday_vet_id = cursor.execute("SELECT Monday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list1.append([r for r, in monday_vet_id])
            monday_label = Label(schedule_label, text=my_list1[0], font="times 10 bold")
            monday_label.grid(row=1, column=3)

            Label(schedule_label, text="Tuesday", font="Times 10 bold").grid(row=2, column=1)
            tuesday_vet_id = cursor.execute("SELECT Tuesday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list2.append([r for r, in tuesday_vet_id])
            tuesday_label = Label(schedule_label, text=my_list2[0], font="times 10 bold")
            tuesday_label.grid(row=2, column=3)

            Label(schedule_label, text="Wednesday", font="Times 10 bold").grid(row=3, column=1)
            wednesday_vet_id = cursor.execute("SELECT Wednesday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list3.append([r for r, in wednesday_vet_id])
            wednesday_label = Label(schedule_label, text=my_list3[0], font="times 10 bold")
            wednesday_label.grid(row=3, column=3)

            Label(schedule_label, text="Thursday", font="Times 10 bold").grid(row=4, column=1)
            thursday_vet_id = cursor.execute("SELECT Thursday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list4.append([r for r, in thursday_vet_id])
            thursday_label = Label(schedule_label, text=my_list4[0], font="times 10 bold")
            thursday_label.grid(row=4, column=3)

            Label(schedule_label, text="Friday", font="Times 10 bold").grid(row=5, column=1)
            friday_vet_id = cursor.execute("SELECT Friday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list5.append([r for r, in friday_vet_id])
            friday_label = Label(schedule_label, text=my_list5[0], font="times 10 bold")
            friday_label.grid(row=5, column=3)

            Label(schedule_label, text="Saturday", font="Times 10 bold").grid(row=6, column=1)
            saturday_vet_id = cursor.execute("SELECT Saturday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list6.append([r for r, in saturday_vet_id])
            saturday_label = Label(schedule_label, text=my_list6[0], font="times 15 bold")
            saturday_label.grid(row=6, column=3)

            Label(schedule_label, text="Sunday", font="Times 10 bold").grid(row=7, column=1)
            sunday_vet_id = cursor.execute("SELECT Sunday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list7.append([r for r, in sunday_vet_id])
            sunday_label = Label(schedule_label, text=my_list7[0], font="times 10 bold")
            sunday_label.grid(row=7, column=3)

            Button(schedule_label, text="Clear Schedule", width=15, height=1, font='times 10 bold', bd=20, bg='SpringGreen4', command = clear_schedule_label).grid(row=8, columnspan=5, column=2)

        def clear_schedule_label():
            global schedule_label
            
            for widgets in schedule_label.winfo_children():
                widgets.destroy()
            
        cb1.bind("<<ComboboxSelected>>", schedule_retrieval)
        