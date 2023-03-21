from tkinter import * # gui import
import tkinter as tk # gui import
from tkinter import ttk # necessary for comboboxes
import pyodbc # necessary for aws rds sql server connection
from tkcalendar import Calendar # gui import (must install tkcalendar "pip install tkcalendar")
from datetime import datetime
from userfile import * 
from vetfile import *
from adminfile import *
#Connection to AWS RDS SQL Server (required to run properly)
connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=Arthur;PWD=123;')
cursor = connection.cursor()

# Used to show each frame as the menu is interacted with
def vetapp():
    create_vetapp()
    calendar_display()
    x.user_register()
    x.user_login()
    x.user_after_login_menu()
    x.user_update_account_menu()
    x.pet_register()
    y.vet_login()
    y.vet_after_login_menu()
    y.vet_update_schedule_menu()
    y.vet_update_account_menu()
    z.admin_register()
    z.admin_login()
    z.admin_after_login_menu()
    show_frame(account_page)

# Opens the calendar menu on click (on base menu frame)
def calendar_clicked():
    window.title("Calendar")
    show_frame(calendar)


# Used to show each frame as the menu is interacted with
def show_frame(frame):
    frame.tkraise()
    
# Opens the account creation menu on click (on base menu frame)
def account_creation_clicked():
    window.title("Create Your Account")
    show_frame(account_create)

# Opens the login menu on click (on base menu frame)
def user_log_in_clicked():
    window.title("User Log In")
    show_frame(user_log_in)

# Returns to the base account page on click
def return_to_main():
    window.title("Home")
    if(isinstance(label,Label)):
        label.destroy()
        clear_all_frame()
        show_frame(account_page)
    else:
        clear_all_frame()
        show_frame(account_page)

def clear_all_frame():
    for widgets in user_update_pet_info.winfo_children():
        widgets.destroy()
    for widgets in vet_update_pet.winfo_children():
        widgets.destroy()
    for widgets in admin_vet_dropdown.winfo_children():
        widgets.destroy()
    user_update_pet_info.pack_forget()
    vet_update_pet.pack_forget()
    admin_vet_dropdown.pack_forget()
    
# Closes the menu
def close_clicked():
    window.destroy()

# Program window configuration
window = Tk()
window.state('zoomed')
window.title("Home")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

account_page = Frame(window)
account_create = Frame(window)
calendar = Frame(window)
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
vet_update_schedule = Frame(window)
vet_update_pet = Frame(window)
admin_log_in = Frame(window)
admin_menu = Frame(window)
admin_update_info = Frame(window)
admin_create_vet = Frame(window)
admin_delete_vet = Frame(window)
admin_vet_dropdown = Frame(window)

for frame in (account_page, account_create, user_log_in, user_pet_menu, user_pet_add,  user_menu, user_update_info, user_update_pet_info, 
              user_update_pet_dropdown, vet_log_in, vet_menu, vet_update_info, vet_update_schedule, vet_update_pet,
              admin_log_in, admin_menu, admin_update_info, admin_create_vet, admin_delete_vet, admin_vet_dropdown, calendar):
    frame.grid(row=0, column=0, sticky='nsew')
    
x = user(window, account_page, account_create, user_log_in, user_pet_menu, user_pet_add,  user_menu, user_update_info, user_update_pet_info, user_update_pet_dropdown)
y = vet(window, account_page, vet_log_in, vet_menu, vet_update_info, vet_update_schedule, vet_update_pet)
z = admin(window, account_page, admin_log_in, admin_menu, admin_update_info, admin_create_vet, admin_delete_vet, admin_vet_dropdown)

label = None
    ##on click
def updateLabel(event):
    seldate.config(text = "Selected Date: " + cal.get_date())

def calendar_display():
    cal = Calendar(calendar,mindate = datetime(2020, 1, 1),
                          maxdate = datetime(2023, 12, 30),
                          showweeknumbers = False,
                          showothermonthdays = False,
                          background = "green",
                          foreground = "white",
                          selectbackground = "red", 
                          normalbackground = "lightgreen",
                          weekendbackground = "darkgreen",
                          weekendforeground = "white")
    cal.pack()
 
    ##date = Label(calendar, text = "")
    ##date.pack(pady = 20)

   ## cal.pack()
 
    cal.bind("<<CalendarSelected>>", updateLabel)
 
    seldate = tk.Label(calendar, text = "Selected Date: ")
    seldate.pack()




    ##drop down for vets
    global cal_view_vet_menu_label

    Label(calendar, text = "").pack()
    cal_view_vet_menu_label = Label(calendar, text = "View/Delete Veterinarians Menu", font = "times 15")
    cal_view_vet_menu_label.pack()

    query= "SELECT Concat(VetID, ', ', VetLoginID, ', ', VetFirstName, ', ', VetLastName) FROM VETACCOUNTINFO"

    my_data = cursor.execute(query) # SQLAlchem engine result
    my_list = [r for r, in my_data] # create a  list 

    sel=tk.StringVar()

    cb1 = ttk.Combobox(calendar, values=my_list,width=15,textvariable = sel)
    cb1.pack(padx=30,pady=30)





# **Don't touch**
# Main window on program start
def create_vetapp():
    account_page_header = Label(account_page, text='Vet Appointment System', font='times 50 bold', bg='SpringGreen4', anchor=N, pady=50)
    account_page_header.pack(fill='both')

    Label(account_page, text="").pack()

    create_button = Button(account_page, text='Create Account', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:account_creation_clicked())
    create_button.pack(pady=15, side=TOP)

    user_log_button = Button(account_page, text='User Log In', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:user_log_in_clicked())
    user_log_button.pack(pady=15, side=TOP)

    vet_log_button = Button(account_page, text='Vet Log In', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:y.vet_log_in_clicked())
    vet_log_button.pack(pady=15, side=TOP)
    
    admin_log_button = Button(account_page, text='Admin Log In', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:z.admin_log_in_clicked())
    admin_log_button.pack(pady=15, side=TOP)

    calendar_button = Button(account_page, text='Calendar', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:calendar_clicked())
    calendar_button.pack(pady=15, side=TOP)

    close_button = Button(account_page, text='Close System', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:close_clicked())
    close_button.pack(pady=15, side=TOP)


# Tells the user that the username they're trying to register with was taken
def username_taken():
    global username_taken_screen
    username_taken_screen = Toplevel(window)
    username_taken_screen.title("Alerts")
    username_taken_screen.geometry("300x150")
    Label(username_taken_screen, text="Username is already taken").pack()
    Button(username_taken_screen, text="OK", command=delete_username_taken).pack()

# Closes the username_taken() pop-up
def delete_username_taken():
    username_taken_screen.destroy()

# Main window on program start (loops until closed)
vetapp()
window.mainloop()