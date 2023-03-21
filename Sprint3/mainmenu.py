from tkinter import * # gui import
import tkinter as tk # gui import
from tkinter import ttk # necessary for comboboxes
import pyodbc # necessary for aws rds sql server connection
<<<<<<< HEAD
from userfile import *
from vetfile import *
from adminfile import *
from calendar import *
=======
from tkcalendar import Calendar # gui import (must install tkcalendar "pip install tkcalendar")
from userfile import *
from vetfile import *
from adminfile import *
>>>>>>> origin/workingCal.3.20.23.vetproj
#Connection to AWS RDS SQL Server (required to run properly)
connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=Arthur;PWD=123;')
cursor = connection.cursor()

# Used to show each frame as the menu is interacted with
def vetapp():
    create_vetapp()
<<<<<<< HEAD
=======
    calendar_display()
>>>>>>> origin/workingCal.3.20.23.vetproj
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

<<<<<<< HEAD
=======
# Opens the calendar menu on click (on base menu frame)
def calendar_clicked():
    window.title("Calendar")
    show_frame(calendar)


>>>>>>> origin/workingCal.3.20.23.vetproj
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

<<<<<<< HEAD
# def admin_log_in_clicked():
#     window.title("Admin Log In")
#     show_frame(admin_log_in)

# def admin_menu_launch():
#     window.title("Admin Menu")
#     if(isinstance(label,Label)):
#         label.destroy()
#         clear_admin_frame()
#         z.admin_vet_dropdown_menu()
#         show_frame(admin_menu)
#     else:
#         clear_admin_frame()
#         z.admin_vet_dropdown_menu()
#         show_frame(admin_menu)

# def admin_dropdown_clicked():
#     window.title("Admin Vet Delete")
#     if(isinstance(label,Label)):
#         label.destroy()
#         show_frame(admin_vet_dropdown)
#     else:
#         show_frame(admin_vet_dropdown)

# def admin_vet_create_clicked():
#     window.title("Create a Vet")
#     show_frame(admin_create_vet)

=======
>>>>>>> origin/workingCal.3.20.23.vetproj
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
<<<<<<< HEAD

# def clear_user_frame():
#     for widgets in user_update_pet_info.winfo_children():
#         widgets.destroy()
#     user_update_pet_info.pack_forget()

# def clear_vet_frame():
#     for widgets in vet_update_pet.winfo_children():
#         widgets.destroy()
#     vet_update_pet.pack_forget()

# def clear_admin_frame():
#     for widgets in admin_vet_dropdown.winfo_children():
#         widgets.destroy()
#     admin_vet_dropdown.pack_forget()
=======
>>>>>>> origin/workingCal.3.20.23.vetproj
    
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
<<<<<<< HEAD
=======
calendar = Frame(window)
>>>>>>> origin/workingCal.3.20.23.vetproj
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
<<<<<<< HEAD
calendar = Frame(window)
=======
>>>>>>> origin/workingCal.3.20.23.vetproj

for frame in (account_page, account_create, user_log_in, user_pet_menu, user_pet_add,  user_menu, user_update_info, user_update_pet_info, 
              user_update_pet_dropdown, vet_log_in, vet_menu, vet_update_info, vet_update_schedule, vet_update_pet,
              admin_log_in, admin_menu, admin_update_info, admin_create_vet, admin_delete_vet, admin_vet_dropdown, calendar):
    frame.grid(row=0, column=0, sticky='nsew')
    
x = user(window, account_page, account_create, user_log_in, user_pet_menu, user_pet_add,  user_menu, user_update_info, user_update_pet_info, user_update_pet_dropdown)
y = vet(window, account_page, vet_log_in, vet_menu, vet_update_info, vet_update_schedule, vet_update_pet)
z = admin(window, account_page, admin_log_in, admin_menu, admin_update_info, admin_create_vet, admin_delete_vet, admin_vet_dropdown)

label = None
<<<<<<< HEAD
# **Don't touch**
# Main window on program start


# Opens the calendar menu on click (on base menu frame)
def calendar_clicked():
    window.title("Calendar")
    show_frame(calendar)

=======

def calendar_display():
    cal = Calendar(calendar, selectmode = 'day', year = 2023, month = 3, day = 14)
    cal.pack(pady = 300)
    
    date = Label(calendar, text = "")
    date.pack(pady = 20)

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
>>>>>>> origin/workingCal.3.20.23.vetproj
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


<<<<<<< HEAD


=======
>>>>>>> origin/workingCal.3.20.23.vetproj
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

<<<<<<< HEAD
# # ###########################################################################################################################################################################

# #Admin Log In
# def admin_login():
#     Label(admin_log_in, text="Please enter details below to login", font="times 50 bold", bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
#     Label(admin_log_in, text="").pack()
 
#     global admin_username_verify
#     global admin_password_verify
 
#     admin_username_verify = StringVar()
#     admin_password_verify = StringVar()
 
#     global admin_username_login_entry
#     global admin_password_login_entry
 
#     Label(admin_log_in, font="times 30", text="Username").pack()
#     admin_username_login_entry = Entry(admin_log_in, font="times 30", textvariable=admin_username_verify)
#     admin_username_login_entry.pack()
#     Label(admin_log_in, text="").pack()
#     Label(admin_log_in, font="times 30", text="Password").pack()
#     admin_password_login_entry = Entry(admin_log_in, font="times 30", textvariable=admin_password_verify, show= '*')
#     admin_password_login_entry.pack()
#     Label(admin_log_in, text="").pack()
#     Button(admin_log_in, text="Login", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = admin_login_verify).pack()
#     Label(admin_log_in, text="").pack()
#     Button(admin_log_in, text="Return to Main Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = return_to_main).pack()

# ###################################################################################################################################################################################
# # Admin Log In Verification
# def admin_login_verify():
#     global admin_login_ID
#     global label
#     global username3
#     global password3
#     username3 = admin_username_verify.get()
#     password3 = admin_password_verify.get()
#     admin_username_login_entry.delete(0, END)
#     admin_password_login_entry.delete(0, END)
#     admin_login_ID = NONE
#     if(username3 == "" or password3 == ""):
#         admin_invalid_login()
#     else:
#         cursor.execute("SELECT AdminLoginID FROM AdminLoginInfo WHERE AdminUserName = ? AND AdminPassword = ?",username3, password3)
#         admin_login_ID = cursor.fetchone()
#         if(admin_login_ID != None):
#             admin_menu_launch()
#         else:
#             admin_invalid_login()

# ###################################################################################################################################################################################

# # admin invalid login
# def admin_invalid_login():
#     global invalid_login_screen
#     invalid_login_screen = Toplevel(window)
#     invalid_login_screen.title("Alert")
#     invalid_login_screen.geometry("300x150")
#     Label(invalid_login_screen, text="Invalid Login ").pack()
#     Button(invalid_login_screen, text="OK", command=delete_admin_invalid_login).pack()

# # Removes the admin_invalid_login() pop-up on click
# def delete_admin_invalid_login():
#     invalid_login_screen.destroy()

# ######################################################################################################################################

# # Menu that appears after successful admin login
# #NEEEDS BUTTON REPLACEMENT
# def admin_after_login_menu():
#     Label(admin_menu, text="Select Your Choice", font='times 50 bold', bg='SpringGreen4', anchor=N, pady=50).pack(fill=BOTH)
#     Label(admin_menu,text="").pack()
#     Button(admin_menu,text="Create a Vet Login", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command =lambda:admin_vet_create_clicked()).pack()
#     Label(admin_menu,text="").pack()
#     Button(admin_menu,text="Delete a Vet", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = lambda:admin_dropdown_clicked()).pack()
#     Label(admin_menu,text="").pack()
#     Button(admin_menu,text="Log Out", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = return_to_main).pack()
    
# ################################################################################################################################################

# def admin_register():
#     global username4
#     global password4
#     global username_entry1
#     global password_entry1 
#     username4 = StringVar()
#     password4 = StringVar()
 
#     Label(admin_create_vet, text="Please enter details below", font='times 50 bold', bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
#     Label(admin_create_vet, text="").pack()
#     username_label = Label(admin_create_vet, font='times 30', text="Username")
#     username_label.pack()
#     username_entry1 = Entry(admin_create_vet, font='times 30', textvariable=username4)
#     username_entry1.pack()
#     password_label = Label(admin_create_vet, font='times 30', text="Password")
#     password_label.pack()
#     password_entry1 = Entry(admin_create_vet, font='times 30', textvariable=password4, show='*')
#     password_entry1.pack()
#     Label(admin_create_vet, text="").pack()
#     Button(admin_create_vet, text="Register", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = add_vet_creation).pack()
#     Label(admin_create_vet, text="").pack()
#     Button(admin_create_vet, text="Return to Admin Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = admin_menu_launch).pack()

# # Admin Vet Account Creation
# def add_vet_creation():
#     global label
#     global vet_login_ID
#     global vet_ID
#     username_info = username4.get()
#     password_info = password4.get()
    
#     vet_login_ID = None
#     vet_ID = None
#     if(username_info == "" or password_info == ""):
#         username_entry1.delete(0, END)
#         password_entry1.delete(0, END)
#         empty_login_info()
#     else:
#         cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?", username_info, password_info)
#         vet_login_ID = cursor.fetchone()
#         if(vet_login_ID == None):
#             cursor.execute("INSERT INTO VetLoginInfo VALUES(?,?)", username_info, password_info)
#             cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?", username_info, password_info)
#             vet_login_ID = cursor.fetchone() 
#             cursor.execute("INSERT INTO VetAccountInfo(VetLoginID) VALUES(?)", vet_login_ID)
#             cursor.execute("SELECT VetID FROM VetAccountInfo WHERE VetLoginID =?", vet_login_ID)
#             vet_ID = cursor.fetchone()
#             cursor.execute("INSERT INTO VetScheduleInfo(VetID) VALUES(?)", vet_ID)
#             cursor.commit()
#             username_entry1.delete(0, END)
#             password_entry1.delete(0, END)
 
#             label = Label(admin_create_vet, text="Registration Successful", fg="green", font="times 20")
#             label.pack() 
#         else:
#             username_entry1.delete(0, END)
#             password_entry1.delete(0, END)
#             username_taken()    

# # Menu that appears after View Veterinarians is clicked by an admin
# def admin_vet_dropdown_menu():
#     global admin_view_vet_menu_label
    
#     Label(admin_vet_dropdown, text = "").pack()
#     admin_view_vet_menu_label = Label(admin_vet_dropdown, text = "View/Delete Veterinarians Menu", font = "times 15")
#     admin_view_vet_menu_label.pack()

#     query= "SELECT Concat(VetID, ', ', VetLoginID, ', ', VetFirstName, ', ', VetLastName) FROM VETACCOUNTINFO"
                
#     my_data = cursor.execute(query) # SQLAlchem engine result
#     my_list = [r for r, in my_data] # create a  list 
   
#     sel=tk.StringVar()

#     cb1 = ttk.Combobox(admin_vet_dropdown, values=my_list,width=15,textvariable = sel)
#     cb1.pack(padx=30,pady=30)

#     def admin_confirmation_popup():
#         global admin_confirmation
#         admin_confirmation = Toplevel(window)
#         admin_confirmation.title("Alert")
#         admin_confirmation.geometry("300x150")
#         Label(admin_confirmation, text=f'You selected {cb1.get()}.').pack()
#         Button(admin_confirmation, text="Delete", command=admin_confirmation_del).pack()
#         Button(admin_confirmation, text="No", command=admin_confirmation_des).pack()

#     def admin_confirmation_del():
#         global label
#         sel = cb1.get().split(", ")
#         cursor.execute("DELETE FROM VetScheduleInfo where VetID=?", sel[0])
#         cursor.execute("DELETE FROM VetAccountInfo WHERE VetID=?", sel[0]) 
#         cursor.execute("DELETE FROM VetLoginInfo WHERE VetLoginID=?", sel[1])
#         cursor.commit()
#         label = Label(admin_vet_dropdown, text ="Successfully deleted!")
#         label.pack()
#         cb1.set('')
#         admin_confirmation_des()
    
#     def admin_confirmation_des():
#         admin_confirmation.destroy()
    
#     #buttons
#     Label(admin_vet_dropdown, text = "").pack()
#     Button(admin_vet_dropdown, text="Delete Vet", width = 20, height = 1, font = 'times 20', bd = 20, bg = 'SpringGreen4', command = admin_confirmation_popup).pack()
#     Label(admin_vet_dropdown, text = "").pack()
#     Button(admin_vet_dropdown, text="Return to Admin Menu", width = 20, height = 1, font = 'times 20', bd = 20, bg = 'SpringGreen4', command = admin_menu_launch).pack()

# ####################################################################################################################################################################

# Main window on program start (loops until closed)



=======
# Main window on program start (loops until closed)
>>>>>>> origin/workingCal.3.20.23.vetproj
vetapp()
window.mainloop()