from tkinter import * # gui import
import tkinter as tk # gui import
from tkcalendar import Calendar # gui import (must install tkcalendar "pip install tkcalendar")
from tkinter import ttk # necessary for comboboxes
import main

class AdminUtils(Tk):
    
    #Admin Log In
    def admin_login():
        Label(main.GUI.admin_log_in, text="Please enter details below to login", font="times 50 bold", bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
        Label(main.GUI.admin_log_in, text="").pack()
    
        global admin_username_verify
        global admin_password_verify
    
        admin_username_verify = StringVar()
        admin_password_verify = StringVar()
    
        global admin_username_login_entry
        global admin_password_login_entry
    
        Label(main.GUI.admin_log_in, font="times 30", text="Username").pack()
        admin_username_login_entry = Entry(main.GUI.admin_log_in, font="times 30", textvariable=admin_username_verify)
        admin_username_login_entry.pack()
        Label(main.GUI.admin_log_in, text="").pack()
        Label(main.GUI.admin_log_in, font="times 30", text="Password").pack()
        admin_password_login_entry = Entry(main.GUI.admin_log_in, font="times 30", textvariable=admin_password_verify, show= '*')
        admin_password_login_entry.pack()
        Label(main.GUI.admin_log_in, text="").pack()
        Button(main.GUI.admin_log_in, text="Login", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = AdminUtils.admin_login_verify).pack()
        Label(main.GUI.admin_log_in, text="").pack()
        Button(main.GUI.admin_log_in, text="Return to Main Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = main.GUI.return_to_main).pack()

    ###################################################################################################################################################################################
    # Admin Log In Verification
    def admin_login_verify():
        global admin_login_ID
        global label
        global username3
        global password3
        username3 = admin_username_verify.get()
        password3 = admin_password_verify.get()
        admin_username_login_entry.delete(0, END)
        admin_password_login_entry.delete(0, END)
        admin_login_ID = NONE
        if(username3 == "" or password3 == ""):
            AdminUtils.admin_invalid_login()
        else:
            main.GUI.cursor.execute("SELECT AdminLoginID FROM AdminLoginInfo WHERE AdminUserName = ? AND AdminPassword = ?",username3, password3)
            admin_login_ID = main.GUI.cursor.fetchone()
            if(admin_login_ID != None):
                main.GUI.admin_menu_launch()
            else:
                AdminUtils.admin_invalid_login()

    ###################################################################################################################################################################################

    # admin invalid login
    def admin_invalid_login():
        global invalid_login_screen
        invalid_login_screen = Toplevel(main.GUI.window)
        invalid_login_screen.title("Alert")
        invalid_login_screen.geometry("300x150")
        Label(invalid_login_screen, text="Invalid Login ").pack()
        Button(invalid_login_screen, text="OK", command=AdminUtils.delete_admin_invalid_login).pack()

    # Removes the admin_invalid_login() pop-up on click
    def delete_admin_invalid_login():
        invalid_login_screen.destroy()

    ######################################################################################################################################

    # Menu that appears after successful admin login
    #NEEEDS BUTTON REPLACEMENT
    def admin_after_login_menu():
        Label(main.GUI.admin_menu, text="Select Your Choice", font='times 50 bold', bg='SpringGreen4', anchor=N, pady=50).pack(fill=BOTH)
        Label(main.GUI.admin_menu,text="").pack()
        Button(main.GUI.admin_menu,text="Create a Vet Login", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command =lambda:main.GUI.admin_vet_create_clicked()).pack()
        Label(main.GUI.admin_menu,text="").pack()
        Button(main.GUI.admin_menu,text="Delete a Vet", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = lambda:main.GUI.admin_dropdown_clicked()).pack()
        Label(main.GUI.admin_menu,text="").pack()
        Button(main.GUI.admin_menu,text="Log Out", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = main.GUI.return_to_main).pack()
        
    ################################################################################################################################################

    def admin_register():
        global username4
        global password4
        global username_entry1
        global password_entry1 
        username4 = StringVar()
        password4 = StringVar()
    
        Label(main.GUI.admin_create_vet, text="Please enter details below", font='times 50 bold', bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
        Label(main.GUI.admin_create_vet, text="").pack()
        username_label = Label(main.GUI.admin_create_vet, font='times 30', text="Username")
        username_label.pack()
        username_entry1 = Entry(main.GUI.admin_create_vet, font='times 30', textvariable=username4)
        username_entry1.pack()
        password_label = Label(main.GUI.admin_create_vet, font='times 30', text="Password")
        password_label.pack()
        password_entry1 = Entry(main.GUI.admin_create_vet, font='times 30', textvariable=password4, show='*')
        password_entry1.pack()
        Label(main.GUI.admin_create_vet, text="").pack()
        Button(main.GUI.admin_create_vet, text="Register", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = AdminUtils.add_vet_creation).pack()
        Label(main.GUI.admin_create_vet, text="").pack()
        Button(main.GUI.admin_create_vet, text="Return to Admin Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = main.GUI.admin_menu_launch).pack()

    # Admin Vet Account Creation
    def add_vet_creation():
        global label
        global vet_login_ID
        global vet_ID
        username_info = username4.get()
        password_info = password4.get()
        
        vet_login_ID = None
        vet_ID = None
        if(username_info == "" or password_info == ""):
            username_entry1.delete(0, END)
            password_entry1.delete(0, END)
            main.GUI.empty_info()
        else:
            main.GUI.cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?", username_info, password_info)
            vet_login_ID = main.GUI.cursor.fetchone()
            if(vet_login_ID == None):
                main.GUI.cursor.execute("INSERT INTO VetLoginInfo VALUES(?,?)", username_info, password_info)
                main.GUI.cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?", username_info, password_info)
                vet_login_ID = main.GUI.cursor.fetchone() 
                main.GUI.cursor.execute("INSERT INTO VetAccountInfo(VetLoginID) VALUES(?)", vet_login_ID)
                main.GUI.cursor.execute("SELECT VetID FROM VetAccountInfo WHERE VetLoginID =?", vet_login_ID)
                vet_ID = main.GUI.cursor.fetchone()
                main.GUI.cursor.execute("INSERT INTO VetScheduleInfo(VetID) VALUES(?)", vet_ID)
                main.GUI.cursor.commit()
                username_entry1.delete(0, END)
                password_entry1.delete(0, END)
    
                label = Label(main.GUI.admin_create_vet, text="Registration Successful", fg="green", font="times 20")
                label.pack() 
            else:
                username_entry1.delete(0, END)
                password_entry1.delete(0, END)
                main.GUI.username_taken()    

    # Menu that appears after View Veterinarians is clicked by an admin
    def admin_vet_dropdown_menu():
        global admin_view_vet_menu_label
        
        Label(main.GUI.admin_vet_dropdown, text = "").pack()
        admin_view_vet_menu_label = Label(main.GUI.admin_vet_dropdown, text = "View/Delete Veterinarians Menu", font = "times 15")
        admin_view_vet_menu_label.pack()

        query= "SELECT Concat(VetID, ', ', VetLoginID, ', ', VetFirstName, ', ', VetLastName) FROM VETACCOUNTINFO"
                    
        my_data = main.GUI.cursor.execute(query) # SQLAlchem engine result
        my_list = [r for r, in my_data] # create a  list 
    
        sel=tk.StringVar()

        cb1 = ttk.Combobox(main.GUI.admin_vet_dropdown, values=my_list,width=15,textvariable = sel)
        cb1.pack(padx=30,pady=30)

        def admin_confirmation_popup():
            global admin_confirmation
            admin_confirmation = Toplevel(main.GUI.window)
            admin_confirmation.title("Alert")
            admin_confirmation.geometry("300x150")
            Label(admin_confirmation, text=f'You selected {cb1.get()}.').pack()
            Button(admin_confirmation, text="Delete", command=admin_confirmation_del).pack()
            Button(admin_confirmation, text="No", command=admin_confirmation_des).pack()

        def admin_confirmation_del():
            global label
            sel = cb1.get().split(", ")
            main.GUI.cursor.execute("DELETE FROM VetScheduleInfo where VetID=?", sel[0])
            main.GUI.cursor.execute("DELETE FROM VetAccountInfo WHERE VetID=?", sel[0]) 
            main.GUI.cursor.execute("DELETE FROM VetLoginInfo WHERE VetLoginID=?", sel[1])
            main.GUI.cursor.commit()
            label = Label(main.GUI.admin_vet_dropdown, text ="Successfully deleted!")
            label.pack()
            cb1.set('')
            admin_confirmation_des()
        
        def admin_confirmation_des():
            admin_confirmation.destroy()
        
        #buttons
        Label(main.GUI.admin_vet_dropdown, text = "").pack()
        Button(main.GUI.admin_vet_dropdown, text="Delete Vet", width = 20, height = 1, font = 'times 20', bd = 20, bg = 'SpringGreen4', command = admin_confirmation_popup).pack()
        Label(main.GUI.admin_vet_dropdown, text = "").pack()
        Button(main.GUI.admin_vet_dropdown, text="Return to Admin Menu", width = 20, height = 1, font = 'times 20', bd = 20, bg = 'SpringGreen4', command = main.GUI.admin_menu_launch).pack()