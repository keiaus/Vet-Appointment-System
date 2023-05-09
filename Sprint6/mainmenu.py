from tkinter import * # gui import
import tkinter as tk # gui import
from tkinter import ttk # necessary for comboboxes
import pyodbc # necessary for aws rds sql server connection
from userfile import * # contains all registered user-related functions
from vetfile import * # contains all veterinarian-related functions
from adminfile import * # contains all administrator-related functions
from calendar_utils import * # contains all calendar-related functions for unregistered users

#Connection to AWS RDS SQL Server (required to run properly)
connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=Arthur;PWD=123;')
cursor = connection.cursor()

# calls methods from the specific classes in order to have frames filled with the proper widgets
def vetapp():
    create_vetapp()
    c.calendar_display()
    x.user_register()
    x.user_login()
    x.user_after_login_menu()
    y.vet_after_login_menu()
    z.admin_after_login_menu()
    show_frame(account_page)

# Used to show each frame as the menu is interacted with
def show_frame(frame):
    frame.tkraise()

# Shows the calendar frame when an unregistered user clicks its button from the main menu
def calendar_clicked():
    window.title("Calendar")
    show_frame(calendar_frame)

def clear_all_frame():
    for widgets in z.admin_log_in.winfo_children():
        widgets.destroy()
    z.admin_log_in.pack_forget()

# Closes the system
def close_clicked():
    window.destroy()

# Program window configuration
window = Tk()
window.state('zoomed')
window.title("Home")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

#creates all required frames for the system
account_page = Frame(window)
account_create = Frame(window)
user_log_in = Frame(window)
user_menu = Frame(window)
user_pet_menu = Frame(window)
user_pet_add = Frame(window)
user_update_info = Frame(window)
vet_log_in = Frame(window)
vet_menu = Frame(window)
vet_update_info = Frame(window)
user_update_pet_info = Frame(window)
user_update_pet_dropdown = Frame(window)
user_searchvet_frame = Frame(window)
vet_update_schedule = Frame(window)
vet_update_pet = Frame(window)
vet_daily_appointment = Frame(window)
vet_canceled_appointments = Frame(window)
vet_upload_pet_rec = Frame(window)
admin_log_in = Frame(window)
admin_menu = Frame(window)
admin_update_info = Frame(window)
admin_create_vet = Frame(window)
admin_delete_vet = Frame(window)
admin_vet_dropdown = Frame(window)
calendar_frame = Frame(window)
user_calendar_frame = Frame(window)
user_appointment = Frame(window)
cancel_menu_frame = Frame(window)

# grids all frames of the system
for frame in (account_page, account_create, user_log_in, user_pet_menu, user_pet_add,  user_menu, user_update_info, 
              user_update_pet_info, user_update_pet_dropdown, user_searchvet_frame, vet_log_in, vet_menu, vet_update_info, 
              vet_update_schedule, vet_update_pet, vet_canceled_appointments, vet_upload_pet_rec, admin_log_in, admin_menu, 
              admin_update_info, admin_create_vet, admin_delete_vet, admin_vet_dropdown,
              calendar_frame, user_calendar_frame, user_appointment, cancel_menu_frame, vet_daily_appointment):
    frame.grid(row=0, column=0, sticky='nsew')
    

# creates a user from the user class    
x = user(window, account_page, account_create, user_log_in, user_pet_menu, user_pet_add,  user_menu, user_update_info, user_update_pet_info, user_update_pet_dropdown, user_appointment, user_calendar_frame, cancel_menu_frame, user_searchvet_frame)

# creates a vet from the vet class 
y = vet(window, account_page, vet_log_in, vet_menu, vet_update_info, vet_update_schedule, vet_update_pet, vet_daily_appointment, vet_canceled_appointments, vet_upload_pet_rec)

# creates a admin from the admin class 
z = admin(window, account_page, admin_log_in, admin_menu, admin_update_info, admin_create_vet, admin_delete_vet, admin_vet_dropdown)

# creates a calendar from the CalendarUtils class 
c = CalendarUtils(window, calendar_frame, account_page)
label = None

# Main window on program start
def create_vetapp():
    account_page_header = Label(account_page, text='Vet Appointment System', font='times 50 bold', bg='SpringGreen4', anchor=N, pady=50)
    account_page_header.pack(fill = "both")

    # frame to store all buttons and labels
    mainframe = Frame(account_page)
    mainframe.pack()

    # main menu buttons for the log ins and quick access calendar
    create_button = Button(mainframe, text='Create Account', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:x.account_creation_clicked())
    user_log_button = Button(mainframe, text='User Log In', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:x.user_log_in_clicked())
    vet_log_button = Button(mainframe, text='Vet Log In', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:y.vet_log_in_clicked())
    admin_log_button = Button(mainframe, text='Admin Log In', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:z.admin_log_in_clicked())
    calendar_button = Button(mainframe, text='Calendar', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:calendar_clicked())
    close_button = Button(mainframe, text='Close System', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:close_clicked())

    # grids all buttons and labels in order to spread them out
    Label(mainframe, text = " ", font = "times 15").grid(row = 1, column = 2)
    create_button.grid(row = 2, column = 1)
    Label(mainframe, text = " ", font = "times 15").grid(row = 3, column = 2)
    user_log_button.grid(row = 4, column = 1)
    Label(mainframe, text = " ", font = "times 15").grid(row = 5, column = 2)
    vet_log_button.grid(row = 4, column = 3)
    Label(mainframe, text = " ", font = "times 15").grid(row = 1, column = 2)
    admin_log_button.grid(row = 2, column = 3)
    Label(mainframe, text = " ", font = "times 15").grid(row = 3, column = 2)
    calendar_button.grid(row = 6, column = 2)
    Label(mainframe, text = " ", font = "times 15").grid(row = 5, column = 2)
    # if we add another button, it goes here: row 6, column 3
    Label(mainframe, text = " ", font = "times 15").grid(row = 7, column = 2)
    close_button.grid(row = 8, column = 2)

    # configuration of the grids, in order to assign weights
    mainframe.grid_columnconfigure(0, weight = 1)
    mainframe.grid_columnconfigure(4, weight = 1)

# # ###########################################################################################################################################################################


# Main window on program start (loops until closed)
vetapp()
window.mainloop()