from tkinter import * # gui import
import tkinter as tk # gui import
from tkcalendar import Calendar # gui import (must install tkcalendar "pip install tkcalendar")
from tkinter import ttk # necessary for comboboxes
from registeredUser import *
from unRegisteredUser import *
from vet import *
from admin_utils import *
import pyodbc # necessary for aws rds sql server connection

# This class acts as the root of our system and calls every function in 
# correlation to each frame
class GUI(Tk):
    
    #Connection to AWS RDS SQL Server (required to run properly)
    connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=Arthur;PWD=123;')
    cursor = connection.cursor()

    # This function passes in two paramemters and is used as our main method to call each function 
    # in our system
    def __init__(self, window):
        super().__init__()
        self.window(window)
        UnRegisteredUser.user_register()
        RegisteredUser.user_login()
        RegisteredUser.user_after_login_menu()
        RegisteredUser.user_update_account_menu()
        RegisteredUser.pet_register()
        Vet.vet_login()
        Vet.vet_after_login_menu()
        Vet.vet_update_schedule_menu()
        Vet.vet_update_account_menu()
        AdminUtils.admin_register()
        AdminUtils.admin_login()
        AdminUtils.admin_after_login_menu()

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

    for frame in (account_page, account_create, calendar, user_log_in, user_pet_menu, user_pet_add,  user_menu, user_update_info, user_update_pet_info, 
                user_update_pet_dropdown, vet_log_in, vet_menu, vet_update_info, vet_update_schedule, vet_update_pet,
                admin_log_in, admin_menu, admin_update_info, admin_create_vet, admin_delete_vet, admin_vet_dropdown):
        frame.grid(row=0, column=0, sticky='nsew')

    # Used to show each frame as the menu is interacted with
    def show_frame(frame):
        frame.tkraise()

    # Returns to the base account page on click
    def return_to_main():
        GUI.window.title("Home")
        if(isinstance(label,Label)):
            label.destroy()
            GUI.clear_all_frame()
            GUI.show_frame(GUI.account_page)
        else:
            GUI.clear_all_frame()
            GUI.show_frame(GUI.account_page)

    def clear_all_frame():
        for widgets in GUI.user_update_pet_info.winfo_children():
            widgets.destroy()
        for widgets in GUI.vet_update_pet.winfo_children():
            widgets.destroy()
        for widgets in GUI.admin_vet_dropdown.winfo_children():
            widgets.destroy()
        GUI.user_update_pet_info.pack_forget()
        GUI.vet_update_pet.pack_forget()
        GUI.admin_vet_dropdown.pack_forget()

    def clear_user_frame():
        for widgets in GUI.user_update_pet_info.winfo_children():
            widgets.destroy()
        GUI.user_update_pet_info.pack_forget()

    def clear_vet_frame():
        for widgets in GUI.vet_update_pet.winfo_children():
            widgets.destroy()
        GUI.vet_update_pet.pack_forget()

    def clear_admin_frame():
        for widgets in GUI.admin_vet_dropdown.winfo_children():
            widgets.destroy()
        GUI.admin_vet_dropdown.pack_forget()

    # Opens the update schedule menu on click (for vets)
    def vet_update_schedule_clicked():
        GUI.window.title("Update Schedule")
        GUI.show_frame(GUI.vet_update_schedule)

    # Opens the update account menu on click (for vets)
    def vet_update_button_clicked():
        GUI.window.title("Update Account")
        GUI.show_frame(GUI.vet_update_info)

    # Opens the update pet menu on click (for vets)
    def vet_update_pet_clicked():
        GUI.window.title("Update Pet")
        GUI.show_frame(GUI.vet_update_pet)

    # Opens the update account menu on click (for users)
    def user_update_button_clicked():
        GUI.window.title("Update Account")
        GUI.show_frame(GUI.user_update_info)

    # Opens the update pet menu on click (for users)
    def user_update_pet_button_clicked():
        GUI.window.title("Update Pet Information")
        GUI.show_frame(GUI.user_update_pet_info)

    # Opens the account creation menu on click (on base menu frame)
    def account_creation_clicked(self, account_create):
        self.account_create = account_create
        GUI.window.title("Create Your Account")
        GUI.show_frame(GUI.account_create)

    # Opens the calendar menu on click (on base menu frame)
    def calendar_clicked():
        GUI.window.title("Calendar")
        GUI.show_frame(GUI.calendar)

    # Opens the login menu on click (on base menu frame)
    def user_log_in_clicked():
        GUI.window.title("User Log In")
        GUI.show_frame(GUI.user_log_in)

    # Opens the user menu after successful login (users)
    def user_menu_launch():
        GUI.window.title("User Menu")
        if(isinstance(label,Label)):
            label.destroy()
            GUI.clear_user_frame()
            RegisteredUser.user_update_pet_menu()
            GUI.show_frame(GUI.user_menu)
        else:
            GUI.clear_user_frame()
            RegisteredUser.user_update_pet_menu()
            GUI.show_frame(GUI.user_menu)

    # Opens the user pet menu after successful login (users)
    def user_pet_menu_launch():
        GUI.window.title("User Pet Menu")
        if(isinstance(label,Label)):
            label.destroy()
            GUI.show_frame(GUI.user_pet_menu)
        else:
            GUI.show_frame(GUI.user_pet_menu)

    # Opens the add pet screen on click
    def user_pet_add_clicked():
        GUI.window.title("Add a Pet(s)")
        if (isinstance(label, Label)):
            label.destroy()
            GUI.show_frame(GUI.user_pet_add)
        else:
            GUI.show_frame(GUI.user_pet_add)

    # Opens the vet login menu on click (vets)
    def vet_log_in_clicked():
        GUI.window.title("Vet Log In")
        GUI.show_frame(GUI.vet_log_in)

    # Opens the vet menu after login (vets)
    def vet_menu_launch():
        GUI.window.title("Vet Menu")
        if(isinstance(label,Label)):
            label.destroy()
            GUI.clear_vet_frame()
            Vet.vet_update_pet_info()
            GUI.show_frame(GUI.vet_menu)
        else:
            GUI.clear_vet_frame()
            Vet.vet_update_pet_info()
            GUI.show_frame(GUI.vet_menu)

    def admin_log_in_clicked():
        GUI.window.title("Admin Log In")
        GUI.show_frame(GUI.admin_log_in)

    def admin_menu_launch():
        GUI.window.title("Admin Menu")
        if(isinstance(label,Label)):
            label.destroy()
            GUI.clear_admin_frame()
            AdminUtils.admin_vet_dropdown_menu()
            GUI.show_frame(GUI.admin_menu)
        else:
            GUI.clear_admin_frame()
            AdminUtils.admin_vet_dropdown_menu()
            GUI.show_frame(GUI.admin_menu)

    def admin_dropdown_clicked():
        GUI.window.title("Admin Vet Delete")
        if(isinstance(label,Label)):
            label.destroy()
            GUI.show_frame(GUI.admin_vet_dropdown)
        else:
            GUI.show_frame(GUI.admin_vet_dropdown)

    def admin_vet_create_clicked():
        GUI.window.title("Create a Vet")
        GUI.show_frame(GUI.admin_create_vet)

    # Tells the user that a required field was empty
    def empty_info():
        global empty_info_screen
        empty_info_screen = Toplevel(GUI.window)
        empty_info_screen.title("Alert")
        empty_info_screen.geometry("300x150")
        Label(empty_info_screen, text="A field was empty, please try again.").pack()
        Button(empty_info_screen, text="OK", command=GUI.delete_empty_info).pack()    

    # Closes the empty_info() pop-up on click
    def delete_empty_info():
        empty_info_screen.destroy()

    # Tells the user that the username they're trying to register with was taken
    def username_taken():
        global username_taken_screen
        username_taken_screen = Toplevel(GUI.window)
        username_taken_screen.title("Alerts")
        username_taken_screen.geometry("300x150")
        Label(username_taken_screen, text="Username is already taken").pack()
        Button(username_taken_screen, text="OK", command=GUI.delete_username_taken).pack()

    # Closes the username_taken() pop-up
    def delete_username_taken():
        username_taken_screen.destroy()

    def calendar_display(self, calendar):
        self.calendar = calendar
        cal = Calendar(calendar, selectmode = 'day', year = 2023, month = 3, day = 14)
        cal.pack(pady = 300)
        
        date = Label(calendar, text = "")
        date.pack(pady = 20)

    # Closes the menu
    def close_clicked():
        GUI.window.destroy()

    global label
    label = None
    
    # **Don't touch**
    # Main window on program start
    # def create_vetapp():
    account_page_header = Label(account_page, text='Vet Appointment System', font='times 50 bold', bg='SpringGreen4', anchor=N, pady=50)
    account_page_header.pack(fill='both')

    Label(account_page, text="").pack()

    create_button = Button(account_page, text='Create Account', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:GUI.account_creation_clicked(GUI.window, GUI.account_create))
    create_button.pack(pady=15, side=TOP)

    user_log_button = Button(account_page, text='User Log In', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:GUI.user_log_in_clicked())
    user_log_button.pack(pady=15, side=TOP)

    vet_log_button = Button(account_page, text='Vet Log In', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:GUI.vet_log_in_clicked())
    vet_log_button.pack(pady=15, side=TOP)
    
    admin_log_button = Button(account_page, text='Admin Log In', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:GUI.admin_log_in_clicked())
    admin_log_button.pack(pady=15, side=TOP)

    calendar_button = Button(account_page, text='Calendar', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:GUI.calendar_clicked())
    calendar_button.pack(pady=15, side=TOP)

    close_button = Button(account_page, text='Close System', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:GUI.close_clicked())
    close_button.pack(pady=15, side=TOP)

    calendar_display(window, calendar)
    show_frame(account_page)
    
gui = GUI.window
gui.mainloop()