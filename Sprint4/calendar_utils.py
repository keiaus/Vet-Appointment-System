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
        cal = Calendar(calendar_display_frame, selectmode = 'day', year = 2023, month = 4, day = 25)

        cal.grid(row=0, column = 1)

        calendar_display_frame.grid_columnconfigure(0, weight=1)
        calendar_display_frame.grid_columnconfigure(6, weight=1)

        schedule_label = Frame(self.calendar_frame)
        schedule_label.pack(side=LEFT, anchor="ne")
        schedule_label.grid_columnconfigure(0, weight=1)
        schedule_label.grid_columnconfigure(6, weight=1)

        query = "SELECT Concat(VetID, ', ', VetFirstName, ', ', VetLastName, ', ', Specialization) FROM VETACCOUNTINFO"
        
        ##drop down for vets
        global cal_view_vet_menu_label


        global cal_view_vet_menu_label
        cal_view_vet_menu_label = Label(calendar_display_frame, text = "Select a Vet", font = "times 15 bold")
        cal_view_vet_menu_label.grid(row=1, column=1)
        my_data = cursor.execute(query) # SQLAlchem engine result
        my_list = [r for r, in my_data]

        sel=tk.StringVar()
        cb1 = ttk.Combobox(calendar_display_frame, values=my_list,width=25,textvariable = sel)
        cb1.grid(row=2, column=1)
        Label(calendar_display_frame, text=' ', font="times 10 bold").grid(row = 3, column = 1)
        Button(calendar_display_frame, text="Return to Main Menu", width=20, height=1, font='times 10 bold', bd=20, bg='SpringGreen4', command = self.return_to_main).grid(row=4, column=1)

        # This function retrieves the VetID, day, and time of vet appointments stored in VetScheduleInfo 
        def schedule_retrieval(event):
            global schedule_label
            for widget in schedule_label.winfo_children():
                widget.destroy()

            sel = cb1.get().split(",")

            my_list1 = list()
            my_list2 = list()
            my_list3 = list()
            my_list4 = list()
            my_list5 = list()
            my_list6 = list()
            my_list7 = list()
            
            my_list8 = list()
            my_list9 = list()
            my_list10 = list()
            my_list11 = list()
            my_list12 = list()
            my_list13 = list()
            my_list14 = list()
            my_list15 = list()
            
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
            saturday_label = Label(schedule_label, text=my_list6[0], font="times 10 bold")
            saturday_label.grid(row=6, column=3)

            Label(schedule_label, text="Sunday", font="Times 10 bold").grid(row=7, column=1)
            sunday_vet_id = cursor.execute("SELECT Sunday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list7.append([r for r, in sunday_vet_id])
            sunday_label = Label(schedule_label, text=my_list7[0], font="times 10 bold")
            sunday_label.grid(row=7, column=3)


            Label(schedule_label, text="Vet Information", font="Times 10 bold").grid(row=0, column=6)
            
            Label(schedule_label, text="First Name", font="Times 10 bold").grid(row=1, column=5)
            first_name = cursor.execute("SELECT VetFirstName FROM VETAccountINFO WHERE VETID = ?", sel[0])
            my_list8.append([r for r, in first_name])
            first_name_label = Label(schedule_label, text=my_list8[0], font="times 10 bold")
            first_name_label.grid(row=1, column=7)

            Label(schedule_label, text="Last Name", font="Times 10 bold").grid(row=2, column=5)
            last_name = cursor.execute("SELECT VetLastName FROM VETAccountINFO WHERE VETID = ?", sel[0])
            my_list9.append([r for r, in last_name])
            last_name_label = Label(schedule_label, text=my_list9[0], font="times 10 bold")
            last_name_label.grid(row=2, column=7)

            Label(schedule_label, text="Phone Number", font="Times 10 bold").grid(row=3, column=5)
            phone_number = cursor.execute("SELECT VetPhoneNumber FROM VETAccountINFO WHERE VETID = ?", sel[0])
            my_list10.append([r for r, in phone_number])
            phone_number_label = Label(schedule_label, text=my_list10[0], font="times 10 bold")
            phone_number_label.grid(row=3, column=7)

            Label(schedule_label, text="Email Address", font="Times 10 bold").grid(row=4, column=5)
            email_address  = cursor.execute("SELECT VetEmailAddress FROM VETAccountINFO WHERE VETID = ?", sel[0])
            my_list11.append([r for r, in email_address])
            email_address_label = Label(schedule_label, text=my_list11[0], font="times 10 bold")
            email_address_label.grid(row=4, column=7)

            Label(schedule_label, text="Street Address", font="Times 10 bold").grid(row=5, column=5)
            street_address  = cursor.execute("SELECT VetStreetAddress FROM VETAccountINFO WHERE VETID = ?", sel[0])
            my_list12.append([r for r, in street_address])
            street_address_label = Label(schedule_label, text=my_list12[0], font="times 10 bold")
            street_address_label.grid(row=5, column=7)

            Label(schedule_label, text="City", font="Times 10 bold").grid(row=6, column=5)
            city  = cursor.execute("SELECT VetCity FROM VETAccountINFO WHERE VETID = ?", sel[0])
            my_list13.append([r for r, in city])
            city_label = Label(schedule_label, text=my_list13[0], font="times 10 bold")
            city_label.grid(row=6, column=7)

            Label(schedule_label, text="State", font="Times 10 bold").grid(row=7, column=5)
            state  = cursor.execute("SELECT VetState FROM VETAccountINFO WHERE VETID = ?", sel[0])
            my_list14.append([r for r, in state])
            state_label = Label(schedule_label, text=my_list14[0], font="times 10 bold")
            state_label.grid(row=7, column=7)
            
            Label(schedule_label, text="Zip", font="Times 10 bold").grid(row=8, column=5)
            zip  = cursor.execute("SELECT VetZip FROM VETAccountINFO WHERE VETID = ?", sel[0])
            my_list15.append([r for r, in zip])
            zip_label = Label(schedule_label, text=my_list15[0], font="times 10 bold")
            zip_label.grid(row=8, column=7)
            
        cb1.bind("<<ComboboxSelected>>", schedule_retrieval)
        