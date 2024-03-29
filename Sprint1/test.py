from tkinter import *
import tkinter as tk
import pyodbc

connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=Arthur;PWD=123;')
cursor = connection.cursor()

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

def show_frame(frame):
    frame.tkraise()

def vet_update_schedule_clicked():
    window.title("Update Schedule")
    show_frame(vet_update_schedule)
    return vet_update_schedule_menu()

def vet_update_button_clicked():
    window.title("Update Account")
    show_frame(vet_update_info)
    return vet_update_account_menu()

def user_update_button_clicked():
    window.title("Update Account")
    show_frame(user_update_info)
    return user_update_account_menu()
    
def account_creation_clicked():
    window.title("Create Account")
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
    window.title("Home")
    show_frame(account_page)
    
def close_clicked():
    window.destroy()

for frame in (account_page, account_create, user_log_in, user_menu, user_update_info, vet_log_in, vet_menu, vet_update_info, vet_update_schedule):
    frame.grid(row=0, column=0, sticky='nsew')

account_page_header = Label(account_page, text='Vet Appointment System', font=("times 50"), anchor=N, bg="SpringGreen4", pady=50)
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

    global user_name_var
    user_name_var = StringVar()
    global user_name_entry
    global first_name_var
    first_name_var = StringVar()
    global first_name_entry
    global last_name_var
    last_name_var = StringVar()
    global last_name_entry
    global email_var
    email_var = StringVar()
    global email_entry
    global phone_number_var
    phone_number_var = StringVar()
    global phone_number_entry
    global street_address_var
    street_address_var = StringVar()
    global street_address_entry
    global city_var
    city_var = StringVar()
    global city_entry
    global state_var
    state_var = StringVar()
    global state_entry
    global zip_var 
    zip_var = StringVar()
    global zip_entry
    global password1_var
    password1_var = StringVar()
    global password1_entry
    global password2_var
    password2_var = StringVar()
    global password2_entry
    # global username
    # global password
    # global username_entry
    # global password_entry 
    # username = StringVar()
    # password = StringVar()
 
    # Label(account_create, text="Please enter details below", bg="blue").pack()
    # Label(account_create, text="").pack()
    # username_lable = Label(account_create, text="Username * ")
    # username_lable.pack()
    # username_entry = Entry(account_create, textvariable=username)
    # username_entry.pack()
    # password_lable = Label(account_create, text="Password * ")
    # password_lable.pack()
    # password_entry = Entry(account_create, textvariable=password, show='*')
    # password_entry.pack()
    # Label(account_create, text="").pack()
    # Button(account_create, text="Register", width=10, height=1, bg="blue", command = register_user).pack()

    header = Label(account_create, text="Create Your Account", font=('Arial', 25))
    header.pack(padx=0, pady=20)

    first_name_label = Label(account_create, text='First Name', font=('calibre', 12, 'bold'))
    first_name_entry = Entry(account_create, textvariable=first_name_var, font=('calibre', 10, 'normal'))
    first_name_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
    first_name_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

    last_name_label = Label(account_create, text='Last Name', font=('calibre', 12, 'bold'))
    last_name_entry = Entry(account_create, textvariable=last_name_var, font=('calibre', 10, 'normal'))
    last_name_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
    last_name_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

    user_name_label = Label(account_create, text='Username', font=('calibre', 12, 'bold'))
    user_name_entry = Entry(account_create, textvariable=user_name_var, font=('calibre', 10, 'normal'))
    user_name_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
    user_name_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

    email_label = Label(account_create, text='Email', font=('calibre', 12, 'bold'))
    email_entry = Entry(account_create, textvariable=email_var, font=('calibre', 10, 'normal'))
    email_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
    email_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

    phone_number_label = Label(account_create, text='Phone Number', font=('calibre', 12, 'bold'))
    phone_number_entry = Entry(account_create, textvariable=phone_number_var, font=('calibre', 10, 'normal'))
    phone_number_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
    phone_number_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

    street_address_label = Label(account_create, text='Street Address', font=('calibre', 12, 'bold'))
    street_address_entry = Entry(account_create, textvariable=street_address_var, font=('calibre', 10, 'normal'))
    street_address_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
    street_address_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

    city_label = Label(account_create, text='City', font=('calibre', 12, 'bold'))
    city_entry = Entry(account_create, textvariable=city_var, font=('calibre', 10, 'normal'))
    city_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
    city_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

    state_label = Label(account_create, text='State', font=('calibre', 12, 'bold'))
    state_entry = Entry(account_create, textvariable=state_var, font=('calibre', 10, 'normal'))
    state_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
    state_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

    zip_label = Label(account_create, text='Zip Code', font=('calibre', 12, 'bold'))
    zip_entry = Entry(account_create, textvariable=zip_var, font=('calibre', 10, 'normal'))
    zip_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
    zip_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

    password1_label = Label(account_create, text='Password', font=('calibre', 12, 'bold'))
    password1_entry = Entry(account_create, textvariable=password1_var, font=('calibre', 10, 'normal'), show='*')
    password1_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
    password1_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

    password2_label = Label(account_create, text='Confirm Password', font=('calibre', 12, 'bold'))
    password2_entry = Entry(account_create, textvariable=password2_var, font=('calibre', 10, 'normal'), show='*')
    password2_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
    password2_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

    btn = Button(account_create, text="Sign Up", bd=7, command=register_user, font='Helevetica')
    btn.pack(pady=40)

def register_user():

    global user_login_id
    user_login_id = None

    first_name_info = first_name_entry.get()
    last_name_info = last_name_entry.get()
    user_name_info = user_name_entry.get()
    email_info = email_entry.get()
    phone_number_info = phone_number_entry.get()
    street_address_info = street_address_entry.get()
    city_info = city_entry.get()
    state_info = state_entry.get()
    zip_info = zip_entry.get()
    password1_info = password1_entry.get()
    password2_info = password2_entry.get()

    # This checks if any fields are missing values
    if (not first_name_info or not last_name_info or not user_name_info or not email_info 
    or not phone_number_info or not street_address_info or not city_info or not state_info 
    or not zip_info or not password1_info or not password2_info):
        invalid_field_message = Message(account_create, text="Please fill in all required fields", fg='#ff1944', font="times 20")
        invalid_field_message.pack()
    
    elif password1_info != password2_info:
        invalid_password_message = Message(account_create, text="Passwords don't match", fg='#ff1944', font="times 20", anchor=E)
        invalid_password_message.pack()
        
    else:
        cursor.execute("select UserLoginID from UserLoginInfo where UserUserName = ? and ")
        cursor.execute("insert into UserAccountInfo values (?, ?, ?, ?, ?, ?, ?, ?)", 
        first_name_info, last_name_info, phone_number_info, email_info, street_address_info, 
        city_info, state_info, zip_info)
        cursor.commit()
        registered_message = Message(account_create, text="Registered Successfully", fg="#32CD32", font="times 20", anchor=S)
        registered_message.pack()
    
    # return account_creation_clicked()
    
    # else:
        # cursor.execute("insert into UserAccountInfo values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
        # first_name_info, last_name_info, user_name_info, email_info, phone_number_info, street_address_info, 
        # city_info, state_info, zip_info, password2_info)

# def register_user():
 
    # global user_login_ID 
    # username_info = user_name_var.get()
    # password_info = password.get()
    
#     user_login_ID = None
#     if(username_info == "" or password_info == ""):
#         username_entry.delete(0, END)
#         password_entry.delete(0, END)
#         empty_login_info()
#     else:
#         cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username_info, password_info)
#         user_login_ID = cursor.fetchone()
#         if(user_login_ID == None):
#             cursor.execute("INSERT INTO UserLoginInfo VALUES(?,?)", username_info, password_info)
#             cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username_info, password_info)
#             user_login_ID = cursor.fetchone() 
#             cursor.execute("INSERT INTO UserAccountInfo(UserLoginID) VALUES(?)", user_login_ID)
#             cursor.commit()
    
#             username_entry.delete(0, END)
#             password_entry.delete(0, END)
 
#             Label(account_create, text="Registration Success", fg="green", font=("calibri", 11)).pack()
#             Button(account_create, text="Return to Main Menu", command=return_to_main).pack()   
#         else:
#             username_entry.delete(0, END)
#             password_entry.delete(0, END)
#             username_taken()

def username_taken():
    global username_taken_screen
    username_taken_screen = Toplevel(window)
    username_taken_screen.title("Success")
    username_taken_screen.geometry("300x150")
    Label(username_taken_screen, text="Username is already taken").pack()
    Button(username_taken_screen, text="OK", command=delete_username_taken).pack()

def delete_username_taken():
    username_taken_screen.destroy()
    
def empty_login_info():
    global empty_login_info_screen
    empty_login_info_screen = Toplevel(window)
    empty_login_info_screen.title("Success")
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
    user_login_ID = NONE
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
    global username2
    global password2
    username2 = vet_username_verify.get()
    password2 = vet_password_verify.get()
    vet_username_login_entry.delete(0, END)
    vet_password_login_entry.delete(0, END)
    vet_login_ID = NONE
    if(username2 == "" or password2 == ""):
        vet_invalid_login()
    else:
        cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?",username2, password2)
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
    Button(vet_menu,text="Update Account Info", height="2", width="50", command =lambda:vet_update_button_clicked()).pack()
    Label(vet_menu,text="").pack()
    Button(vet_menu,text="Update Schedule Info", height="2", width="50", command = lambda:vet_update_schedule_clicked()).pack()
    Label(vet_menu,text="").pack()
    Button(vet_menu,text="Log Out", height="2", width="30", command = return_to_main).pack()
######################################################################################################################################

#USER UPDATE ACCOUNT
def user_update_account_menu():
    
    global user_id
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
    global first_name_entry
    global last_name_entry
    global email_entry
    global phone_number_entry
    global street_address_entry
    global city_entry
    global state_entry
    global zip_entry
    
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
    
    Button(user_update_info, text='Submit', font='50', command = user_update_account).pack()
    
def user_update_account():
    first_name_var = first_name_entry.get()
    last_name_var = last_name_entry.get()
    email_var = email_entry.get()
    phone_number_var = phone_number_entry.get()
    street_address_var = street_address_entry.get()
    city_var = city_entry.get()
    state_var = state_entry.get()
    zip_var = zip_entry.get()
    cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username1, password1)
    user_login_ID = cursor.fetchone()
    cursor.execute("SELECT UserID FROM UserAccountInfo INNER JOIN UserLoginInfo ON UserAccountInfo.UserLoginID = UserLoginInfo.UserLoginID WHERE UserAccountInfo.UserLoginID = ?", user_login_ID)
    user_id = cursor.fetchone()
    cursor.execute("UPDATE UserAccountInfo SET UserFirstName = ?, UserLastName = ?, UserPhoneNumber = ?, UserEmailAddress = ?, UserStreetAddress = ?, UserCity = ?, UserState = ?, UserZip = ? WHERE UserID = ?", first_name_var, last_name_var, phone_number_var, email_var, street_address_var, city_var, state_var, zip_var, user_id[0])
    cursor.commit()
    first_name_entry.delete(0,END)
    last_name_entry.delete(0,END)
    phone_number_entry.delete(0,END)
    email_entry.delete(0,END)
    street_address_entry.delete(0,END)
    city_entry.delete(0,END)
    state_entry.delete(0,END)
    zip_entry.delete(0,END)
    Label(user_update_info, text="Update Successful", fg="green", font=("calibri", 11)).pack()
    Button(user_update_info, text="Return to User Menu", width=25, height=1, command = user_menu_launch).pack()

##################################################################################################################################################

#VET UPDATE MENU
def vet_update_account_menu():
    
    global vet_id
    global vet_first_name_var 
    vet_first_name_var= StringVar()
    global vet_last_name_var
    vet_last_name_var = StringVar()
    global vet_email_var
    vet_email_var = StringVar()
    global vet_phone_number_var
    vet_phone_number_var = StringVar()
    global vet_street_address_var
    vet_street_address_var = StringVar()
    global vet_city_var
    vet_city_var = StringVar()
    global vet_state_var
    vet_state_var = StringVar()
    global vet_zip_var
    vet_zip_var = StringVar()
    global vet_first_name_entry
    global vet_last_name_entry
    global vet_email_entry
    global vet_phone_number_entry
    global vet_street_address_entry
    global vet_city_entry
    global vet_state_entry
    global vet_zip_entry
    
    vet_first_name_label = Label(vet_update_info, text='First Name', font=('calibre', 12, 'bold'))
    vet_first_name_entry = Entry(vet_update_info, textvariable=vet_first_name_var, font=('calibre', 10, 'normal'))
    vet_first_name_label.pack()
    vet_first_name_entry.pack()

    vet_last_name_label = Label(vet_update_info, text='Last Name', font=('calibre', 12, 'bold'))
    vet_last_name_entry = Entry(vet_update_info, textvariable=vet_last_name_var, font=('calibre', 10, 'normal'))
    vet_last_name_label.pack()
    vet_last_name_entry.pack()

    vet_email_label = Label(vet_update_info, text='Email', font=('calibre', 12, 'bold'))
    vet_email_entry = Entry(vet_update_info, textvariable=vet_email_var, font=('calibre', 10, 'normal'))
    vet_email_label.pack()
    vet_email_entry.pack()

    vet_phone_number_label = Label(vet_update_info, text='Phone Number', font=('calibre', 12, 'bold'))
    vet_phone_number_entry = Entry(vet_update_info, textvariable=vet_phone_number_var, font=('calibre', 10, 'normal'))
    vet_phone_number_label.pack()
    vet_phone_number_entry.pack()

    vet_street_address_label = Label(vet_update_info, text='Street Address', font=('calibre', 12, 'bold'))
    vet_street_address_entry = Entry(vet_update_info, textvariable=vet_street_address_var, font=('calibre', 10, 'normal'))
    vet_street_address_label.pack()
    vet_street_address_entry.pack()
  

    vet_city_label = Label(vet_update_info, text='City', font=('calibre', 12, 'bold'))
    vet_city_entry = Entry(vet_update_info, textvariable=vet_city_var, font=('calibre', 10, 'normal'))
    vet_city_label.pack()
    vet_city_entry.pack()

    vet_state_label = Label(vet_update_info, text='State', font=('calibre', 12, 'bold'))
    vet_state_entry = Entry(vet_update_info, textvariable=vet_state_var, font=('calibre', 10, 'normal'))
    vet_state_label.pack(side =TOP)
    vet_state_entry.pack()

    vet_zip_label = Label(vet_update_info, text='Zip Code', font=('calibre', 12, 'bold'))
    vet_zip_entry = Entry(vet_update_info, textvariable=vet_zip_var, font=('calibre', 10, 'normal'))
    vet_zip_label.pack()
    vet_zip_entry.pack()
    
    Button(vet_update_info, text='Submit', font='50', command = vet_update_account).pack()
    
def vet_update_account():
    vet_first_name_var = vet_first_name_entry.get()
    vet_last_name_var = vet_last_name_entry.get()
    vet_email_var = vet_email_entry.get()
    vet_phone_number_var = vet_phone_number_entry.get()
    vet_street_address_var = vet_street_address_entry.get()
    vet_city_var = vet_city_entry.get()
    vet_state_var = vet_state_entry.get()
    vet_zip_var = vet_zip_entry.get()
    cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?", username2, password2)
    vet_login_ID = cursor.fetchone()
    cursor.execute("SELECT VetID FROM VetAccountInfo INNER JOIN VetLoginInfo ON VetAccountInfo.VetLoginID = VetLoginInfo.VetLoginID WHERE VetAccountInfo.VetLoginID = ?", vet_login_ID)
    vet_id = cursor.fetchone()
    cursor.execute("UPDATE VetAccountInfo SET VetFirstName = ?, VetLastName = ?, VetPhoneNumber = ?, VetEmailAddress = ?, VetStreetAddress = ?, VetCity = ?, VetState = ?, VetZip = ? WHERE VetID = ?", vet_first_name_var, vet_last_name_var, vet_phone_number_var, vet_email_var, vet_street_address_var, vet_city_var, vet_state_var, vet_zip_var, vet_id[0])
    cursor.commit()
    vet_first_name_entry.delete(0,END)
    vet_last_name_entry.delete(0,END)
    vet_phone_number_entry.delete(0,END)
    vet_email_entry.delete(0,END)
    vet_street_address_entry.delete(0,END)
    vet_city_entry.delete(0,END)
    vet_state_entry.delete(0,END)
    vet_zip_entry.delete(0,END)
    Label(vet_update_info, text="Update Successful", fg="green", font=("calibri", 11)).pack()
    Button(vet_update_info, text="Return to User Menu", width=25, height=1, command = vet_menu_launch).pack()
##################################################################################################################################################

#VET UPDATE SCHEDULE

def vet_update_schedule_menu():
   global monday 
   monday= StringVar()
   global tuesday
   tuesday = StringVar()
   global wednesday
   wednesday = StringVar()
   global thursday
   thursday = StringVar()
   global friday
   friday = StringVar()
   global saturday
   saturday = StringVar()
   global sunday
   sunday = StringVar()
   global monday_entry
   global tuesday_entry
   global wednesday_entry
   global thursday_entry
   global friday_entry
   global saturday_entry
   global sunday_entry


   monday_label = Label(vet_update_schedule, text='Monday', font=('calibre', 12, 'bold'))
   monday_entry = Entry(vet_update_schedule, textvariable=monday, font=('calibre', 10, 'normal'))
   monday_label.pack()
   monday_entry.pack()

   tuesday_label = Label(vet_update_schedule, text='Tuesday', font=('calibre', 12, 'bold'))
   tuesday_entry = Entry(vet_update_schedule, textvariable=tuesday, font=('calibre', 10, 'normal'))
   tuesday_label.pack()
   tuesday_entry.pack()

   wednesday_label = Label(vet_update_schedule, text='Wednesday', font=('calibre', 12, 'bold'))
   wednesday_entry = Entry(vet_update_schedule, textvariable=wednesday, font=('calibre', 10, 'normal'))
   wednesday_label.pack()
   wednesday_entry.pack()

   thursday_label = Label(vet_update_schedule, text='Thursday', font=('calibre', 12, 'bold'))
   thursday_entry = Entry(vet_update_schedule, textvariable=thursday, font=('calibre', 10, 'normal'))
   thursday_label.pack()
   thursday_entry.pack()

   friday_label = Label(vet_update_schedule, text='Friday', font=('calibre', 12, 'bold'))
   friday_entry = Entry(vet_update_schedule, textvariable=friday, font=('calibre', 10, 'normal'))
   friday_label.pack()
   friday_entry.pack()

   saturday_label = Label(vet_update_schedule, text='Saturday', font=('calibre', 12, 'bold'))
   saturday_entry = Entry(vet_update_schedule, textvariable=saturday, font=('calibre', 10, 'normal'))
   saturday_label.pack()
   saturday_entry.pack()

   sunday_label = Label(vet_update_schedule, text='Sunday', font=('calibre', 12, 'bold'))
   sunday_entry = Entry(vet_update_schedule, textvariable=sunday, font=('calibre', 10, 'normal'))
   sunday_label.pack()
   sunday_entry.pack()    

   Button(vet_update_schedule, text='Submit', font='50', command = vet_update_schedule_info).pack()

def vet_update_schedule_info():
    monday = monday_entry.get()
    tuesday = tuesday_entry.get()
    wednesday = wednesday_entry.get()
    thursday = thursday_entry.get()
    friday = friday_entry.get()
    saturday = saturday_entry.get()
    sunday = sunday_entry.get()
    cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?", username2, password2)
    vet_login_ID = cursor.fetchone()
    cursor.execute("SELECT VetID FROM VetAccountInfo INNER JOIN VetLoginInfo ON VetAccountInfo.VetLoginID = VetLoginInfo.VetLoginID WHERE VetAccountInfo.VetLoginID = ?", vet_login_ID)
    vet_id = cursor.fetchone()
    cursor.execute("INSERT INTO VetScheduleInfo(VetID, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) VALUES(?,?,?,?,?,?,?,?)", vet_id[0], monday, tuesday, wednesday, thursday, friday, saturday, sunday);    cursor.commit()
    cursor.commit()
    monday_entry.delete(0,END)
    tuesday_entry.delete(0,END)
    wednesday_entry.delete(0,END)
    thursday_entry.delete(0,END)
    friday_entry.delete(0,END)
    saturday_entry.delete(0,END)
    sunday_entry.delete(0,END)
    Label(vet_update_schedule, text="Update Successful", fg="green", font=("calibri", 11)).pack()
    Button(vet_update_schedule, text="Return to User Menu", width=25, height=1, command = vet_menu_launch).pack()

###########################################################################################################################################################################


show_frame(account_page)
window.mainloop()

