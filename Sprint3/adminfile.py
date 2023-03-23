from tkinter import * # gui import
import tkinter as tk # gui import
from tkinter import ttk # necessary for comboboxes
import pyodbc # necessary for aws rds sql server connection

#Connection to AWS RDS SQL Server (required to run properly)
connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=Arthur;PWD=123;')
cursor = connection.cursor()

label = None
class AdminUtils():

    def __init__(self, window, account_page, admin_log_in, admin_menu, admin_update_info, admin_create_vet, admin_delete_vet, admin_vet_dropdown):
        super().__init__()
        self.window = window
        self.account_page = account_page
        self.admin_log_in = admin_log_in
        self.admin_menu = admin_menu
        self.admin_update_info = admin_update_info
        self.admin_create_vet = admin_create_vet
        self.admin_delete_vet = admin_delete_vet
        self.admin_vet_dropdown = admin_vet_dropdown
    
    def show_frame(self,frame):
        frame.tkraise()
              
    def clear_admin_frame(self):
        for widgets in self.admin_vet_dropdown.winfo_children():
            widgets.destroy()
        self.admin_vet_dropdown.pack_forget()
    
    def admin_log_in_clicked(self):
        self.window.title("Admin Log In")
        self.show_frame(self.admin_log_in)

    def admin_menu_launch(self):
        self.window.title("Admin Menu")
        if(isinstance(label,Label)):
            label.destroy()
            self.clear_admin_frame()
            self.admin_vet_dropdown_menu()
            self.show_frame(self.admin_menu)
        else:
            self.clear_admin_frame()
            self.admin_vet_dropdown_menu()
            self.show_frame(self.admin_menu)

    def admin_dropdown_clicked(self):
        self.window.title("Admin Vet Delete")
        if(isinstance(label,Label)):
            label.destroy()
            self.show_frame(self.admin_vet_dropdown)
        else:
            self.show_frame(self.admin_vet_dropdown)

    def admin_vet_create_clicked(self):
        self.window.title("Create a Vet")
        self.show_frame(self.admin_create_vet)
    
    def empty_login_info(self):
        global empty_login_info_screen
        empty_login_info_screen = Toplevel(self.window)
        empty_login_info_screen.title("Alert")
        empty_login_info_screen.geometry("300x150")
        Label(empty_login_info_screen, text="A field was empty, please try again.").pack()
        Button(empty_login_info_screen, text="OK", command=self.delete_empty_login_info).pack()    

        # Closes the empty_login_info() pop-up on click
    def delete_empty_login_info(self):
        empty_login_info_screen.destroy()
        
    def return_to_main(self):
        self.window.title("Home")
        if(isinstance(label,Label)):
            label.destroy()
            self.clear_admin_frame()
            self.show_frame(self.account_page)
        else:
            self.clear_admin_frame()
            self.show_frame(self.account_page)             
# ###########################################################################################################################################################################
    
    #Admin Log In
    def admin_login(self):
        Label(self.admin_log_in, text="Please enter details below to login", font="times 50 bold", bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
        Label(self.admin_log_in, text="").pack()
    
        global admin_username_verify
        global admin_password_verify
    
        admin_username_verify = StringVar()
        admin_password_verify = StringVar()
    
        global admin_username_login_entry
        global admin_password_login_entry
    
        Label(self.admin_log_in, font="times 30", text="Username").pack()
        admin_username_login_entry = Entry(self.admin_log_in, font="times 30", textvariable=admin_username_verify)
        admin_username_login_entry.pack()
        Label(self.admin_log_in, text="").pack()
        Label(self.admin_log_in, font="times 30", text="Password").pack()
        admin_password_login_entry = Entry(self.admin_log_in, font="times 30", textvariable=admin_password_verify, show= '*')
        admin_password_login_entry.pack()
        Label(self.admin_log_in, text="").pack()
        Button(self.admin_log_in, text="Login", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = self.admin_login_verify).pack()
        Label(self.admin_log_in, text="").pack()
        Button(self.admin_log_in, text="Return to Main Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = self.return_to_main).pack()

    ###################################################################################################################################################################################
    # Admin Log In Verification
    def admin_login_verify(self):
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
            self.admin_invalid_login()
        else:
            cursor.execute("SELECT AdminLoginID FROM AdminLoginInfo WHERE AdminUserName = ? AND AdminPassword = ?",username3, password3)
            admin_login_ID = cursor.fetchone()
            if(admin_login_ID != None):
                self.admin_menu_launch()
            else:
                self.admin_invalid_login()

    ###################################################################################################################################################################################

    # admin invalid login
    def admin_invalid_login(self):
        global invalid_login_screen
        invalid_login_screen = Toplevel(self.window)
        invalid_login_screen.title("Alert")
        invalid_login_screen.geometry("300x150")
        Label(invalid_login_screen, text="Invalid Login ").pack()
        Button(invalid_login_screen, text="OK", command=self.delete_admin_invalid_login).pack()

    # Removes the admin_invalid_login() pop-up on click
    def delete_admin_invalid_login(self):
        invalid_login_screen.destroy()

    ######################################################################################################################################

    # Menu that appears after successful admin login
    #NEEEDS BUTTON REPLACEMENT
    def admin_after_login_menu(self):
        Label(self.admin_menu, text="Select Your Choice", font='times 50 bold', bg='SpringGreen4', anchor=N, pady=50).pack(fill=BOTH)
        Label(self.admin_menu,text="").pack()
        Button(self.admin_menu,text="Create a Vet Login", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command =lambda:self.admin_vet_create_clicked()).pack()
        Label(self.admin_menu,text="").pack()
        Button(self.admin_menu,text="Delete a Vet", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = lambda:self.admin_dropdown_clicked()).pack()
        Label(self.admin_menu,text="").pack()
        Button(self.admin_menu,text="Log Out", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = self.return_to_main).pack()
        
    ################################################################################################################################################

    def admin_register(self):
        global username4
        global password4
        global username_entry1
        global password_entry1 
        username4 = StringVar()
        password4 = StringVar()
    
        Label(self.admin_create_vet, text="Please enter details below", font='times 50 bold', bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
        Label(self.admin_create_vet, text="").pack()
        username_label = Label(self.admin_create_vet, font='times 30', text="Username")
        username_label.pack()
        username_entry1 = Entry(self.admin_create_vet, font='times 30', textvariable=username4)
        username_entry1.pack()
        password_label = Label(self.admin_create_vet, font='times 30', text="Password")
        password_label.pack()
        password_entry1 = Entry(self.admin_create_vet, font='times 30', textvariable=password4, show='*')
        password_entry1.pack()
        Label(self.admin_create_vet, text="").pack()
        Button(self.admin_create_vet, text="Register", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = self.add_vet_creation).pack()
        Label(self.admin_create_vet, text="").pack()
        Button(self.admin_create_vet, text="Return to Admin Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = self.admin_menu_launch).pack()

    # Admin Vet Account Creation
    def add_vet_creation(self):
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
            self.empty_login_info()
        else:
            cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?", username_info, password_info)
            vet_login_ID = cursor.fetchone()
            if(vet_login_ID == None):
                cursor.execute("INSERT INTO VetLoginInfo VALUES(?,?)", username_info, password_info)
                cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?", username_info, password_info)
                vet_login_ID = cursor.fetchone() 
                cursor.execute("INSERT INTO VetAccountInfo(VetLoginID) VALUES(?)", vet_login_ID)
                cursor.execute("SELECT VetID FROM VetAccountInfo WHERE VetLoginID =?", vet_login_ID)
                vet_ID = cursor.fetchone()
                cursor.execute("INSERT INTO VetScheduleInfo(VetID) VALUES(?)", vet_ID)
                cursor.commit()
                username_entry1.delete(0, END)
                password_entry1.delete(0, END)
    
                label = Label(self.admin_create_vet, text="Registration Successful", fg="green", font="times 20")
                label.pack() 
            else:
                username_entry1.delete(0, END)
                password_entry1.delete(0, END)
                self.username_taken()    

    # Menu that appears after View Veterinarians is clicked by an admin
    def admin_vet_dropdown_menu(self):
        global admin_view_vet_menu_label
        
        Label(self.admin_vet_dropdown, text = "").pack()
        admin_view_vet_menu_label = Label(self.admin_vet_dropdown, text = "View/Delete Veterinarians Menu", font = "times 15")
        admin_view_vet_menu_label.pack()

        query= "SELECT Concat(VetID, ', ', VetLoginID, ', ', VetFirstName, ', ', VetLastName) FROM VETACCOUNTINFO"
                    
        my_data = cursor.execute(query) # SQLAlchem engine result
        my_list = [r for r, in my_data] # create a  list 
    
        sel=tk.StringVar()

        cb1 = ttk.Combobox(self.admin_vet_dropdown, values=my_list,width=15,textvariable = sel)
        cb1.pack(padx=30,pady=30)

        def admin_confirmation_popup():
            global admin_confirmation
            admin_confirmation = Toplevel(self.window)
            admin_confirmation.title("Alert")
            admin_confirmation.geometry("300x150")
            Label(admin_confirmation, text=f'You selected {cb1.get()}.').pack()
            Button(admin_confirmation, text="Delete", command=admin_confirmation_del).pack()
            Button(admin_confirmation, text="No", command=admin_confirmation_des).pack()

        def admin_confirmation_del():
            global label
            sel = cb1.get().split(", ")
            cursor.execute("DELETE FROM VetScheduleInfo where VetID=?", sel[0])
            cursor.execute("DELETE FROM VetAccountInfo WHERE VetID=?", sel[0]) 
            cursor.execute("DELETE FROM VetLoginInfo WHERE VetLoginID=?", sel[1])
            cursor.commit()
            label = Label(self.admin_vet_dropdown, text ="Successfully deleted!")
            label.pack()
            cb1.set('')
            admin_confirmation_des()
        
        def admin_confirmation_des():
            admin_confirmation.destroy()
        
        #buttons
        Label(self.admin_vet_dropdown, text = "").pack()
        Button(self.admin_vet_dropdown, text="Delete Vet", width = 20, height = 1, font = 'times 20', bd = 20, bg = 'SpringGreen4', command = admin_confirmation_popup).pack()
        Label(self.admin_vet_dropdown, text = "").pack()
        Button(self.admin_vet_dropdown, text="Return to Admin Menu", width = 20, height = 1, font = 'times 20', bd = 20, bg = 'SpringGreen4', command = self.admin_menu_launch).pack()

####################################################################################################################################################################
