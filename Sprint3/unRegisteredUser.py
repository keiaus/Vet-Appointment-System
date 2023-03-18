from tkinter import * # gui import
import tkinter as tk # gui import
from tkcalendar import Calendar # gui import (must install tkcalendar "pip install tkcalendar")
from tkinter import ttk # necessary for comboboxes
from main import account_create, username_taken, connection, cursor

class UnRegisteredUser(Tk):
    
    # This function passes in one parameter and is used as our main method to call each function 
    # in our system
    def __init__(self):
        super().__init__()

    # User registration menu
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
        Button(account_create, text="Register", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = UnRegisteredUser.register_user).pack()
        Label(account_create, text="").pack()
        Button(account_create, text="Return to Main Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = main.GUI.return_to_main).pack()

    # Registered user login menu
    def register_user():
        global label
        global user_login_ID 
        username_info = username.get()
        password_info = password.get()
        
        user_login_ID = None
        if(username_info == "" or password_info == ""):
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            empty_info()
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
    
                label = Label(account_create, text="Registration Successful", fg="green", font="times 20")
                label.pack() 
            else:
                username_entry.delete(0, END)
                password_entry.delete(0, END)
                username_taken()
    