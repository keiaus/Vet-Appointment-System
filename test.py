# #thetester
# from tkinter import *
# import tkinter as tk
# import os
# import pyodbc
# # Designing window for registration
# connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=Arthur;PWD=123;')
# cursor = connection.cursor()

# # window = tk.Tk()
# # window.state('zoomed')

# # window.rowconfigure(0, weight=1)
# # window.columnconfigure(0, weight=1)

# # after_login_frame = tk.Frame(window)
# # update_account_frame = tk.Frame(window)

# # for frame in (after_login_frame, update_account_frame):
# #     frame.grid(row=0, column=0, sticky='nsew')

# # #after login code
# # global after_login_title 
# # after_login_title = tk.TOP()

 
# def register():
#     global register_screen
#     register_screen = Toplevel(main_screen)
#     register_screen.title("Register")
#     register_screen.geometry("300x250")
 
#     global username
#     global password
#     global username_entry
#     global password_entry 
#     username = StringVar()
#     password = StringVar()
 
#     Label(register_screen, text="Please enter details below", bg="blue").pack()
#     Label(register_screen, text="").pack()
#     username_lable = Label(register_screen, text="Username * ")
#     username_lable.pack()
#     username_entry = Entry(register_screen, textvariable=username)
#     username_entry.pack()
#     password_lable = Label(register_screen, text="Password * ")
#     password_lable.pack()
#     password_entry = Entry(register_screen, textvariable=password, show='*')
#     password_entry.pack()
#     Label(register_screen, text="").pack()
#     Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()

 
# # Designing window for login 
 
# def login():
#     global login_screen
#     login_screen = Toplevel(main_screen)
#     login_screen.title("Login")
#     login_screen.geometry("300x250")
#     Label(login_screen, text="Please enter details below to login").pack()
#     Label(login_screen, text="").pack()
 
#     global username_verify
#     global password_verify
 
#     username_verify = StringVar()
#     password_verify = StringVar()
 
#     global username_login_entry
#     global password_login_entry
 
#     Label(login_screen, text="Username * ").pack()
#     username_login_entry = Entry(login_screen, textvariable=username_verify)
#     username_login_entry.pack()
#     Label(login_screen, text="").pack()
#     Label(login_screen, text="Password * ").pack()
#     password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
#     password_login_entry.pack()
#     Label(login_screen, text="").pack()
#     Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# # Implementing event on register button
 
# def register_user():
 
#     global user_login_ID 
#     username_info = username.get()
#     password_info = password.get()
    
#     user_login_ID = None
    
#     cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username_info, password_info)
#     user_login_ID = cursor.fetchone()
#     if(user_login_ID == None):
#         cursor.execute("INSERT INTO UserLoginInfo VALUES(?,?)", username_info, password_info)
#         cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username_info, password_info)
#         user_login_ID = cursor.fetchone() 
#         cursor.execute("INSERT INTO UserAccountInfo(UserLoginID) VALUES(?)", user_login_ID)
#         cursor.commit()
    
#         username_entry.delete(0, END)
#         password_entry.delete(0, END)
 
#         Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()    
#     else:
#         username_entry.delete(0, END)
#         password_entry.delete(0, END)
#         username_taken()
 
# # Implementing event on login button 
 
# def login_verify():
#     username1 = username_verify.get()
#     password1 = password_verify.get()
#     username_login_entry.delete(0, END)
#     password_login_entry.delete(0, END)
#     user_login_ID = NONE
#     cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username1, password1)
#     user_login_ID = cursor.fetchone()
#     if(user_login_ID != None):
#         login_sucess()
#         after_login_menu()
#     else:
#         invalid_login()
 
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
    
# #Logout 
 
# # def logout():
    
#     #needs to be done
    
# # Designing popup for login success
 
# def login_sucess():
#     # window = tk.Tk()
#     # window.state('zoomed')
#     global login_success_screen
#     login_success_screen = Toplevel(login_screen)
#     login_success_screen.title("Account")
#     login_success_screen.geometry("150x100")
#     Label(login_success_screen, text="Select Your Choice").pack()
#     Button(login_success_screen, text="Update Account Info", command=delete_login_success).pack()
 
# # Designing popup for login invalid password
 
# def invalid_login():
#     global invalid_login_screen
#     invalid_login_screen = Toplevel(login_screen)
#     invalid_login_screen.title("Success")
#     invalid_login_screen.geometry("150x100")
#     Label(invalid_login_screen, text="Invalid Login ").pack()
#     Button(invalid_login_screen, text="OK", command=delete_invalid_login).pack()
 
# # Designing popup for username taken

# def username_taken():
#     global username_taken_screen
#     username_taken_screen = Toplevel(register_screen)
#     username_taken_screen.title("Success")
#     username_taken_screen.geometry("150x100")
#     Label(username_taken_screen, text="Username is already taken").pack()
#     Button(username_taken_screen, text="OK", command=delete_username_taken).pack()

# # Deleting popups
 
# def delete_login_success():
#     login_success_screen.destroy()
 
 
# def delete_invalid_login():
#     invalid_login_screen.destroy()

# def delete_username_taken():
#     username_taken_screen.destroy()
 
# # Designing Main(first) window
 
# def main_account_screen():
#     global main_screen
#     main_screen = Tk()
#     main_screen.geometry("300x250")
#     main_screen.title("Account Login")
#     Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
#     Label(text="").pack()
#     Button(text="Login", height="2", width="30", command = login).pack()
#     Label(text="").pack()
#     Button(text="Register", height="2", width="30", command=register).pack()
 
#     main_screen.mainloop()
 
 
# main_account_screen()

# Page after login

from tkinter import *
import tkinter as tk
import pyodbc

connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=Arthur;PWD=123;')
cursor = connection.cursor()

def show_frame(frame):
    frame.tkraise()

def user_fill_in():
    return update_account_menu()

def update_button_clicked():
    window.title("Update Account")
    show_frame(update_account_page)

window = tk.Tk()
window.state('zoomed')
window.title("Home")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

account_page = tk.Frame(window)
update_account_page = tk.Frame(window)


for frame in (account_page, update_account_page):
    frame.grid(row=0, column=0, sticky='nsew')

# ***TRYING TO GET UPDATE BUTTON WORKING WITH DB***

# Account page
account_page_header = tk.Label(account_page, text='Welcome', font='times 50', anchor=N, pady=50)
account_page_header.pack(fill='both', expand=True)

update_button = tk.Button(account_page, text='Update Account', font='times 15', command=lambda:update_button_clicked())
update_button.pack(pady=15, side=TOP)

# Update account page
update_page = tk.Label(update_account_page)
update_page.pack(fill='both', expand=True)

submit_button = tk.Button(update_page, text='Submit', font='50', command=lambda:show_frame(update_account_page))
submit_button.pack(pady=40, anchor=S, side=BOTTOM)

def update_account_menu():
    
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
    # global update_account_info_screen
    # update_account_info_screen = Toplevel(login_screen)
    # update_account_info_screen.title = ("User Account Update")
    # update_account_info_screen.geometry("1360x764")
    
    first_name_label = Label(update_account_page, text='First Name', font=('calibre', 12, 'bold'))
    first_name_entry = Entry(update_account_page, textvariable=first_name_var, font=('calibre', 10, 'normal'))
    first_name_label.pack()
    first_name_entry.pack()

    last_name_label = Label(update_account_page, text='Last Name', font=('calibre', 12, 'bold'))
    last_name_entry = Entry(update_account_page, textvariable=last_name_var, font=('calibre', 10, 'normal'))
    last_name_label.pack()
    last_name_entry.pack()

    email_label = Label(update_account_page, text='Email', font=('calibre', 12, 'bold'))
    email_entry = Entry(update_account_page, textvariable=email_var, font=('calibre', 10, 'normal'))
    email_label.pack()
    email_entry.pack()

    phone_number_label = Label(update_account_page, text='Phone Number', font=('calibre', 12, 'bold'))
    phone_number_entry = Entry(update_account_page, textvariable=phone_number_var, font=('calibre', 10, 'normal'))
    phone_number_label.pack()
    phone_number_entry.pack()

    street_address_label = Label(update_account_page, text='Street Address', font=('calibre', 12, 'bold'))
    street_address_entry = Entry(update_account_page, textvariable=street_address_var, font=('calibre', 10, 'normal'))
    street_address_label.pack()
    street_address_entry.pack()

    city_label = Label(update_account_page, text='City', font=('calibre', 12, 'bold'))
    city_entry = Entry(update_account_page, textvariable=city_var, font=('calibre', 10, 'normal'))
    city_label.pack()
    city_entry.pack()

    state_label = Label(update_account_page, text='State', font=('calibre', 12, 'bold'))
    state_entry = Entry(update_account_page, textvariable=state_var, font=('calibre', 10, 'normal'))
    state_label.pack()
    state_entry.pack()

    zip_label = Label(update_account_page, text='Zip Code', font=('calibre', 12, 'bold'))
    zip_entry = Entry(update_account_page, textvariable=zip_var, font=('calibre', 10, 'normal'))
    zip_label.pack()
    zip_entry.pack()

show_frame(account_page)
user_fill_in()

window.mainloop()

# cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username1, password1)
# user_login_ID = cursor.fetchone() 
# cursor.execute("SELECT UserID FROM UserAccountINFO INNER JOIN UserLoginInfo ON UserAccountInfo.UserLoginID = UserLoginInfo.UserLoginID WHERE UserLoginID = ?", user_login_ID)
# user_id = cursor.fetchone()
# cursor.execute("UPDATE UserAccountInfo SET UserFirstName = ?, UserLastName = ?, UserPhoneNumber = ?, UserEmailAddress = ?, UserStreetAddress = ?, UserCity = ?, UserState = ?, UserZip = ? WHERE UserID = ?", first_name_var, last_name_var, phone_number_var, email_var, street_address_var, city_var, state_var, zip_var)
# cursor.commit()
    #needs testing and a final ok confirmation that it was updated and then closes out
