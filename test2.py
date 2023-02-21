
#  # After Login Menu

#  # YOUR PART ******************************

# def after_login_menu():
#     global after_login_screen
#     after_login_screen = Toplevel(login_screen())
#     after_login_screen.geometry("300x250")
#     after_login_screen.title("User Update Menu")
#     Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
#     Label(text="").pack()
#     Button(text="Update Account Info", height="2", width="50", command = update_account_menu).pack()
#     Label(text="").pack()
#     Button(text="Log Out", height="2", width="30", command = logout).pack()
 
# # Updating account info

# def update_account_menu():
    
#     global user_id
#     global first_name_var 
#     first_name_var= StringVar()
#     global last_name_var
#     last_name_var = StringVar()
#     global email_var
#     email_var = StringVar()
#     global phone_number_var
#     phone_number_var = StringVar()
#     global street_address_var
#     street_address_var = StringVar()
#     global city_var
#     city_var = StringVar()
#     global state_var
#     state_var = StringVar()
#     global zip_var
#     zip_var = StringVar()
#     global update_account_info_screen
#     update_account_info_screen = Toplevel(login_screen)
#     update_account_info_screen.title = ("User Account Update")
#     update_account_info_screen.geometry("1360x764")
    
#     first_name_label = Label(update_account_info_screen, text='First Name', font=('calibre', 12, 'bold'))
#     first_name_entry = Entry(update_account_info_screen, textvariable=first_name_var, font=('calibre', 10, 'normal'))
#     first_name_label.pack()
#     first_name_entry.pack()

#     last_name_label = Label(update_account_info_screen, text='Last Name', font=('calibre', 12, 'bold'))
#     last_name_entry = Entry(update_account_info_screen, textvariable=last_name_var, font=('calibre', 10, 'normal'))
#     last_name_label.pack()
#     last_name_entry.pack()

#     email_label = Label(update_account_info_screen, text='Email', font=('calibre', 12, 'bold'))
#     email_entry = Entry(update_account_info_screen, textvariable=email_var, font=('calibre', 10, 'normal'))
#     email_label.pack()
#     email_entry.pack()

#     phone_number_label = Label(update_account_info_screen, text='Phone Number', font=('calibre', 12, 'bold'))
#     phone_number_entry = Entry(update_account_info_screen, textvariable=phone_number_var, font=('calibre', 10, 'normal'))
#     phone_number_label.pack()
#     phone_number_entry.pack()

#     street_address_label = Label(update_account_info_screen, text='Street Address', font=('calibre', 12, 'bold'))
#     street_address_entry = Entry(update_account_info_screen, textvariable=street_address_var, font=('calibre', 10, 'normal'))
#     street_address_label.pack()
#     street_address_entry.pack()

#     city_label = Label(update_account_info_screen, text='City', font=('calibre', 12, 'bold'))
#     city_entry = Entry(update_account_info_screen, textvariable=city_var, font=('calibre', 10, 'normal'))
#     city_label.pack()
#     city_entry.pack()

#     state_label = Label(update_account_info_screen, text='State', font=('calibre', 12, 'bold'))
#     state_entry = Entry(update_account_info_screen, textvariable=state_var, font=('calibre', 10, 'normal'))
#     state_label.pack()
#     state_entry.pack()

#     zip_label = Label(update_account_info_screen, text='Zip Code', font=('calibre', 12, 'bold'))
#     zip_entry = Entry(update_account_info_screen, textvariable=zip_var, font=('calibre', 10, 'normal'))
#     zip_label.pack()
#     zip_entry.pack()
    
#     username1 = username_verify.get()
#     password1 = password_verify.get()
    
#     cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username1, password1)
#     user_login_ID = cursor.fetchone() 
#     cursor.execute("SELECT UserID FROM UserAccountINFO INNER JOIN UserLoginInfo ON UserAccountInfo.UserLoginID = UserLoginInfo.UserLoginID WHERE UserLoginID = ?", user_login_ID)
#     user_id = cursor.fetchone()
#     cursor.execute("UPDATE UserAccountInfo SET UserFirstName = ?, UserLastName = ?, UserPhoneNumber = ?, UserEmailAddress = ?, UserStreetAddress = ?, UserCity = ?, UserState = ?, UserZip = ? WHERE UserID = ?", first_name_var, last_name_var, phone_number_var, email_var, street_address_var, city_var, state_var, zip_var)
#     cursor.commit()
#     #needs testing and a final ok confirmation that it was updated and then closes out


from tkinter import *
import tkinter as tk
import pyodbc

connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=Arthur;PWD=123;')
cursor = connection.cursor()

def show_frame(frame):
    frame.tkraise()

def user_update_button_clicked():
    window.title("Update Account")
    show_frame(user_update_info)
    return user_update_account_menu()
    
def account_creation_clicked():
    window.title("Create Your Account")
    show_frame(account_create)
    return user_register()  

def user_log_in_clicked():
    window.title("User Log In")
    show_frame(user_log_in)
    return user_login()

def user_menu_launch():
    window.title("User Menu")
    show_frame(user_menu)
    return user_after_login_menu()

def vet_log_in_clicked():
    window.title("Vet Log In")
    show_frame(vet_log_in)
    return vet_login()

def vet_menu_launch():
    window.title("Vet Menu")
    show_frame(vet_menu)
    return vet_after_login_menu()

def return_to_main():
    window.title("home")
    show_frame(account_page)
    
def close_clicked():
    window.destroy()

window = Tk()
window.state('zoomed')
window.title("Home")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

account_page = Frame(window)
account_create = Frame(window)
user_log_in = Frame(window)
user_menu = Frame(window)
user_update_info = Frame(window)
vet_log_in = Frame(window)
vet_menu = Frame(window)
vet_update_info = Frame(window)
vet_update_schedule = Frame(window)

for frame in (account_page, account_create, user_log_in, user_menu, user_update_info, vet_log_in, vet_menu, vet_update_info, vet_update_schedule):
    frame.grid(row=0, column=0, sticky='nsew')

account_page_header = Label(account_page, text='Vet Appointment System', font='times 50 bold', bg="SpringGreen4", anchor=N, pady=50)
account_page_header.pack(fill='both')

create_button = Button(account_page, text='Create Account', font='times 30', command=lambda:account_creation_clicked())
create_button.pack(pady=15, side=TOP)

user_log_button = Button(account_page, text='User Log In', font='times 30', command=lambda:user_log_in_clicked())
user_log_button.pack(pady=15, side=TOP)

vet_log_button = Button(account_page, text='Vet Log In', font='times 30', command=lambda:vet_log_in_clicked())
vet_log_button.pack(pady=15, side=TOP)

close_button = Button(account_page, text='Close System', font='times 30', command=lambda:close_clicked())
close_button.pack(pady=15, side=TOP)

# ACCOUNT CREATION
def user_register():
    global username
    global password
    global username_entry
    global password_entry 
    username = StringVar()
    password = StringVar()
 
    Label(account_create, text="Please enter details below", font='times 50 bold', bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
    Label(account_create, text="").pack()
    username_lable = Label(account_create, font='times 30', text="Username")
    username_lable.pack()
    username_entry = Entry(account_create, font='times 30', textvariable=username)
    username_entry.pack()
    password_lable = Label(account_create, font='times 30', text="Password")
    password_lable.pack()
    password_entry = Entry(account_create, font='times 30', textvariable=password, show='*')
    password_entry.pack()
    Label(account_create, text="").pack()
    Button(account_create, text="Register", width=10, height=1, font='times 20', bd=20, bg='SpringGreen4', command = register_user).pack()

def register_user():
 
    global user_login_ID 
    username_info = username.get()
    password_info = password.get()
    
    user_login_ID = None
    if(username_info == "" or password_info == ""):
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        empty_login_info()
    else:
        cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username_info, password_info)
        user_login_ID = cursor.fetchone()
        if(user_login_ID == None):
            cursor.execute("INSERT INTO UserLoginInfo VALUES(?,?)", username_info, password_info)
            cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username_info, password_info)
            user_login_ID = cursor.fetchone() 
            cursor.execute("INSERT INTO UserAccountInfo(UserLoginID) VALUES(?)", user_login_ID)
            cursor.commit()
    
            username_entry.delete(0, END)
            password_entry.delete(0, END)
 
            Label(account_create, text="Registration Success", fg="green", font=("calibri", 11)).pack()
            Button(account_create, text="Return to Main Menu", command=return_to_main).pack()   
        else:
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            username_taken()
 
def username_taken():
    global username_taken_screen
    username_taken_screen = Toplevel(window)
    username_taken_screen.title("")
    username_taken_screen.geometry("300x150")
    Label(username_taken_screen, text="Username is already taken").pack()
    Button(username_taken_screen, text="OK", command=delete_username_taken).pack()

def delete_username_taken():
    username_taken_screen.destroy()
    
def empty_login_info():
    global empty_login_info_screen
    empty_login_info_screen = Toplevel(window)
    empty_login_info_screen.title("")
    empty_login_info_screen.geometry("300x150")
    Label(empty_login_info_screen, text="A field was empty, please try again.").pack()
    Button(empty_login_info_screen, text="OK", command=delete_empty_login_info).pack()    

def delete_empty_login_info():
    empty_login_info_screen.destroy()
###########################################################################################################################

#USER LOG IN
def user_login():
    Label(user_log_in, text="Please enter details below to login").pack()
    Label(user_log_in, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(user_log_in, text="Username * ").pack()
    username_login_entry = Entry(user_log_in, textvariable=username_verify)
    username_login_entry.pack()
    Label(user_log_in, text="").pack()
    Label(user_log_in, text="Password * ").pack()
    password_login_entry = Entry(user_log_in, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(user_log_in, text="").pack()
    Button(user_log_in, text="Login", width=10, height=1, command = user_login_verify).pack()

def user_login_verify():
    global username1
    global password1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    user_login_ID = None
    if(username1 == "" or password1 == ""):
        user_invalid_login()
    else:
        cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username1, password1)
        user_login_ID = cursor.fetchone()
        if(user_login_ID != None):
            user_menu_launch()
            #USER SUB MENU REPLACES THE SUCCESS MESSAGE
        else:
            user_invalid_login()

# def user_login_sucess():
#     global login_success_screen
#     login_success_screen = Toplevel(window)
#     login_success_screen.title("Account")
#     login_success_screen.geometry("150x100")
#     Label(login_success_screen, text="Login Successful").pack()
#     Button(login_success_screen, text="OK", command=delete_user_login_success).pack()

# def delete_user_login_success():
#     login_success_screen.destroy()
 
def user_invalid_login():
    global invalid_login_screen
    invalid_login_screen = Toplevel(window)
    invalid_login_screen.title("Success")
    invalid_login_screen.geometry("150x100")
    Label(invalid_login_screen, text="Invalid Login ").pack()
    Button(invalid_login_screen, text="OK", command=delete_user_invalid_login).pack()

def delete_user_invalid_login():
    invalid_login_screen.destroy()
###################################################################################################################################################

#VET LOGIN
def vet_login():
    Label(vet_log_in, text="Please enter details below to login").pack()
    Label(vet_log_in, text="").pack()
 
    global vet_username_verify
    global vet_password_verify
 
    vet_username_verify = StringVar()
    vet_password_verify = StringVar()
 
    global vet_username_login_entry
    global vet_password_login_entry
 
    Label(vet_log_in, text="Username * ").pack()
    vet_username_login_entry = Entry(vet_log_in, textvariable=vet_username_verify)
    vet_username_login_entry.pack()
    Label(vet_log_in, text="").pack()
    Label(vet_log_in, text="Password * ").pack()
    vet_password_login_entry = Entry(vet_log_in, textvariable=vet_password_verify, show= '*')
    vet_password_login_entry.pack()
    Label(vet_log_in, text="").pack()
    Button(vet_log_in, text="Login", width=10, height=1, command = vet_login_verify).pack()

def vet_login_verify():
    username1 = vet_username_verify.get()
    password1 = vet_password_verify.get()
    vet_username_login_entry.delete(0, END)
    vet_password_login_entry.delete(0, END)
    vet_login_ID = NONE
    if(username1 == "" or password1 == ""):
        vet_invalid_login()
    else:
        cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?",username1, password1)
        vet_login_ID = cursor.fetchone()
        if(vet_login_ID != None):
            vet_menu_launch()
            #VET SUB MENU REPLACES THE SUCCESS MESSAGE
        else:
            vet_invalid_login()

# def vet_login_sucess():
#     global login_success_screen
#     login_success_screen = Toplevel(window)
#     login_success_screen.title("Account")
#     login_success_screen.geometry("150x100")
#     Label(login_success_screen, text="Login Successful").pack()
#     Button(login_success_screen, text="OK", command=delete_vet_login_success).pack()

# def delete_vet_login_success():
#     login_success_screen.destroy()
 
def vet_invalid_login():
    global invalid_login_screen
    invalid_login_screen = Toplevel(window)
    invalid_login_screen.title("Success")
    invalid_login_screen.geometry("150x100")
    Label(invalid_login_screen, text="Invalid Login ").pack()
    Button(invalid_login_screen, text="OK", command=delete_vet_invalid_login).pack()

def delete_vet_invalid_login():
    invalid_login_screen.destroy()
######################################################################################################################################

#USER SUB MENU
def user_after_login_menu():
    Label(user_menu, text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(user_menu, text="").pack()
    Button(user_menu, text="Update Account Info", height="2", width="50", command =lambda:user_update_button_clicked()).pack()
    Label(user_menu, text="").pack()
    Button(user_menu, text="Log Out", height="2", width="30", command = return_to_main).pack()
######################################################################################################################################

#VET SUB MENU

def vet_after_login_menu():
    Label(vet_menu, text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(vet_menu,text="").pack()
    Button(vet_menu,text="Update Account Info", height="2", width="50").pack()
    Label(vet_menu,text="").pack()
    Button(vet_menu,text="Update Schedule Info", height="2", width="50").pack()
    Label(vet_menu,text="").pack()
    Button(vet_menu,text="Log Out", height="2", width="30", command = return_to_main).pack()
######################################################################################################################################

#USER UPDATE ACCOUNT
def user_update_account_menu():
    
    global user_id
    user_id = StringVar()
    global first_name_var 
    first_name_var= StringVar()
    global last_name_var
    last_name_var = StringVar()
    global email_var
    email_var = StringVar()
    global phone_number_var
    phone_number_var = StringVar()
    global street_address_var
    street_address_var = StringVar()
    global city_var
    city_var = StringVar()
    global state_var
    state_var = StringVar()
    global zip_var
    zip_var = StringVar()
    
    first_name_label = Label(user_update_info, text='First Name', font=('calibre', 12, 'bold'))
    first_name_entry = Entry(user_update_info, textvariable=first_name_var, font=('calibre', 10, 'normal'))
    first_name_label.pack()
    first_name_entry.pack()

    last_name_label = Label(user_update_info, text='Last Name', font=('calibre', 12, 'bold'))
    last_name_entry = Entry(user_update_info, textvariable=last_name_var, font=('calibre', 10, 'normal'))
    last_name_label.pack()
    last_name_entry.pack()

    email_label = Label(user_update_info, text='Email', font=('calibre', 12, 'bold'))
    email_entry = Entry(user_update_info, textvariable=email_var, font=('calibre', 10, 'normal'))
    email_label.pack()
    email_entry.pack()

    phone_number_label = Label(user_update_info, text='Phone Number', font=('calibre', 12, 'bold'))
    phone_number_entry = Entry(user_update_info, textvariable=phone_number_var, font=('calibre', 10, 'normal'))
    phone_number_label.pack()
    phone_number_entry.pack()

    street_address_label = Label(user_update_info, text='Street Address', font=('calibre', 12, 'bold'))
    street_address_entry = Entry(user_update_info, textvariable=street_address_var, font=('calibre', 10, 'normal'))
    street_address_label.pack()
    street_address_entry.pack()

    city_label = Label(user_update_info, text='City', font=('calibre', 12, 'bold'))
    city_entry = Entry(user_update_info, textvariable=city_var, font=('calibre', 10, 'normal'))
    city_label.pack()
    city_entry.pack()

    state_label = Label(user_update_info, text='State', font=('calibre', 12, 'bold'))
    state_entry = Entry(user_update_info, textvariable=state_var, font=('calibre', 10, 'normal'))
    state_label.pack(side =TOP)
    state_entry.pack()

    zip_label = Label(user_update_info, text='Zip Code', font=('calibre', 12, 'bold'))
    zip_entry = Entry(user_update_info, textvariable=zip_var, font=('calibre', 10, 'normal'))
    zip_label.pack()
    zip_entry.pack()

    Button(user_update_info, text='Submit', font='50', command=lambda:user_update_account).pack()

# Where we left off
# We need to figure out how to get the queries updated
def user_update_account():
    cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username1, password1)
    user_login_ID = cursor.fetchone()
    cursor.execute("SELECT UserID FROM UserAccountInfo INNER JOIN UserLoginInfo ON UserAccountInfo.UserLoginID = UserLoginInfo.UserLoginID WHERE UserAccountInfo.UserLoginID = ?", user_login_ID)
    user_id = cursor.fetchone()
    cursor.execute("UPDATE UserAccountInfo SET UserFirstName = ?, UserLastName = ?, UserPhoneNumber = ?, UserEmailAddress = ?, UserStreetAddress = ?, UserCity = ?, UserState = ?, UserZip = ? WHERE UserID = ?", str(first_name_var), str(last_name_var), str(phone_number_var), str(email_var), str(street_address_var), str(city_var), str(state_var), str(zip_var), str(user_id))
    cursor.commit()
    Label(user_update_info, text="Update Successful", fg="green", font=("calibri", 11)).pack()
    
show_frame(account_page)
window.mainloop()

#UPDATE USER INFO ACCOUNT QUERIES

# cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username1, password1)
# user_login_ID = cursor.fetchone() 
# cursor.execute("SELECT UserID FROM UserAccountINFO INNER JOIN UserLoginInfo ON UserAccountInfo.UserLoginID = UserLoginInfo.UserLoginID WHERE UserLoginID = ?", user_login_ID)
# user_id = cursor.fetchone()
# cursor.execute("UPDATE UserAccountInfo SET UserFirstName = ?, UserLastName = ?, UserPhoneNumber = ?, UserEmailAddress = ?, UserStreetAddress = ?, UserCity = ?, UserState = ?, UserZip = ? WHERE UserID = ?", first_name_var, last_name_var, phone_number_var, email_var, street_address_var, city_var, state_var, zip_var)
# cursor.commit()
# needs testing and a final ok confirmation that it was updated and then closes out

# VET SCHEDULE CODE AND QUERIES

#    global monday 
#    monday= StringVar()
#    global tuesday
#    tuesday = StringVar()
#    global wednesday
#    wednesday = StringVar()
#    global thursday
#    thursday = StringVar()
#    global friday
#    friday = StringVar()
#    global saturday
#    saturday = StringVar()
#    global sunday
#    sunday = StringVar()



#    monday_label = Label(update_account_page, text='Monday', font=('calibre', 12, 'bold'))
#    monday_entry = Entry(update_account_page, textvariable=monday, font=('calibre', 10, 'normal'))
#    monday_label.pack()
#    monday_entry.pack()

#    tuesday_label = Label(update_account_page, text='Tuesday', font=('calibre', 12, 'bold'))
#    tuesday_entry = Entry(update_account_page, textvariable=tuesday, font=('calibre', 10, 'normal'))
#    tuesday_label.pack()
#    tuesday_entry.pack()

#    wednesday_label = Label(update_account_page, text='Wednesday', font=('calibre', 12, 'bold'))
#    wednesday_entry = Entry(update_account_page, textvariable=wednesday, font=('calibre', 10, 'normal'))
#    wednesday_label.pack()
#    wednesday_entry.pack()

#    thursday_label = Label(update_account_page, text='Thursday', font=('calibre', 12, 'bold'))
#    thursday_entry = Entry(update_account_page, textvariable=thursday, font=('calibre', 10, 'normal'))
#    thursday_label.pack()
#    thursday_entry.pack()

#    friday_label = Label(update_account_page, text='Friday', font=('calibre', 12, 'bold'))
#    friday_entry = Entry(update_account_page, textvariable=friday, font=('calibre', 10, 'normal'))
#    friday_label.pack()
#    friday_entry.pack()

#    saturday_label = Label(update_account_page, text='Saturday', font=('calibre', 12, 'bold'))
#    saturday_entry = Entry(update_account_page, textvariable=saturday, font=('calibre', 10, 'normal'))
#    saturday_label.pack()
#    saturday_entry.pack()

#    sunday_label = Label(update_account_page, text='Sunday', font=('calibre', 12, 'bold'))
#    sunday_entry = Entry(update_account_page, textvariable=sunday, font=('calibre', 10, 'normal'))
#    sunday_label.pack()
#    sunday_entry.pack()


#   vetUsername = vet_username_verify.get()
#   vetPassword = vet_password_verify.get()
    
#   cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?", vetUsername, vetPassword)
#   vet_login_ID = cursor.fetchone() 
#   cursor.execute("SELECT VetID FROM VetAccountINFO INNER JOIN VetLoginInfo ON VetAccountInfo.VetLoginID = VetLoginInfo.VetLoginID WHERE VetLoginID = ?", vet_login_ID)
#   vet_id = cursor.fetchone()

# cursor.execute("INSERT INTO VetScheduleInfo(VetID, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) VALUES(?,?,?,?,?,?,?,?)", vet_id, monday, tuesday, wednesday, thursday, friday, saturday, sunday);