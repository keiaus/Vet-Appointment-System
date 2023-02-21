from tkinter import *
import os
import pyodbc

# Designing window for registration
connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=Keith;PWD=ssmsblue10;')
cursor = connection.cursor()
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("1300x764")
 
    global username
    global password
    global username_entry
    global password_entry 
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("1300x764")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

#     # Designing window for vet login 
 
# def vet_login():
#     global vet_login_screen
#     vet_login_screen = Toplevel(main_screen)
#     vet_login_screen.title("Vet Login")
#     vet_login_screen.geometry("1300x764")
#     Label(vet_login_screen, text="Please enter details below to login").pack()
#     Label(vet_login_screen, text="").pack()
 
#     global vet_username_verify
#     global vet_password_verify
 
#     vet_username_verify = StringVar()
#     vet_password_verify = StringVar()
 
#     global vet_username_login_entry
#     global vet_password_login_entry
 
#     Label(vet_login_screen, text="Username").pack()
#     vet_username_login_entry = Entry(vet_login_screen, textvariable=vet_username_verify)
#     vet_username_login_entry.pack()
#     Label(vet_login_screen, text="").pack()
#     Label(vet_login_screen, text="Password").pack()
#     vet_password_login_entry = Entry(vet_login_screen, textvariable=vet_password_verify, show= '*')
#     vet_password_login_entry.pack()
#     Label(vet_login_screen, text="").pack()
#     Button(vet_login_screen, text="Login", width=10, height=1, command = vet_login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    global user_login_ID 
    username_info = username.get()
    password_info = password.get()
    
    cursor.execute("INSERT INTO UserLoginInfo VALUES(?,?)", username_info, password_info)
    cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username_info, password_info)
    user_login_ID = cursor.fetchone() 
    cursor.execute("INSERT INTO UserAccountInfo(UserLoginID) VALUES(?)", user_login_ID)
    cursor.commit()
    
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Successful", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    user_login_ID = NONE
    cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username1, password1)
    user_login_ID = cursor.fetchone()
    if(user_login_ID != None):
            login_success()
    else:
            invalid_login()

# # Implementing event on vet login button 

# def vet_login_verify():
#     vet_username1 = vet_username_verify.get()
#     vet_password1 = vet_password_verify.get()
#     vet_username_login_entry.delete(0, END)
#     vet_password_login_entry.delete(0, END)
#     vet_user_login_ID = NONE
#     cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?", vet_username1, vet_password1)
#     vet_user_login_ID = cursor.fetchone()
#     if(vet_user_login_ID != None):
#             login_success()
#     else:
#             invalid_login()
 
# Designing popup for login success
 
def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("1300x764")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="Ok", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def invalid_login():
    global invalid_login_screen
    invalid_login_screen = Toplevel(login_screen)
    invalid_login_screen.title("Invalid Login")
    invalid_login_screen.geometry("1300x764")
    Label(invalid_login_screen, text="Invalid Login").pack()
    Button(invalid_login_screen, text="Ok", command=delete_invalid_login).pack()
 
# Designing popup for user not found

# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_invalid_login():
    invalid_login_screen.destroy()

 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("1300x764")
    main_screen.title("Account Login")
    Label(text="Veterinarian Appointment System", bg="SpringGreen4", width="300", height="2", font=("Calibri bold", 20)).pack()
    Label(text="").pack()
    Button(text="Login", height="5", width="30", command = login, font=20).pack()
    Label(text="").pack()
    Button(text="Register", height="5", width="30", command=register, font=20).pack()
    # Label(text="").pack()
    # Button(text="Vet Login", height="5", width="30", command=vet_login, font=20).pack()
    
    main_screen.mainloop()
 
main_account_screen()