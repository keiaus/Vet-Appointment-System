from tkinter import * # gui import
import tkinter as tk # gui import
from tkinter import ttk # necessary for comboboxes
import pyodbc # necessary for aws rds sql server connection
from tkcalendar import Calendar # gui import (must install tkcalendar "pip install tkcalendar")
from datetime import datetime
from datetime import date
#Connection to AWS RDS SQL Server (required to run properly)
connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=Arthur;PWD=123;')
cursor = connection.cursor()

label = None
class user():

    def __init__(self, window, account_page, account_create, user_log_in, user_pet_menu, user_pet_add, user_menu, 
            user_update_info, user_update_pet_info, user_update_pet_dropdown, user_appointment, 
            user_calendar_frame, cancel_menu_frame, user_searchvet_frame):
        super().__init__()
        self.window = window
        self.account_page = account_page
        self.account_create = account_create
        self.user_log_in = user_log_in
        self.user_pet_menu = user_pet_menu
        self.user_pet_add = user_pet_add
        self.user_menu = user_menu
        self.user_update_info = user_update_info
        self.user_update_pet_info = user_update_pet_info
        self.user_update_pet_dropdown = user_update_pet_dropdown
        self.user_appointment = user_appointment
        self.user_calendar_frame = user_calendar_frame
        self.cancel_menu_frame = cancel_menu_frame
        self.user_searchvet_frame = user_searchvet_frame
        
    def show_frame(self,frame):
        frame.tkraise()

    def account_creation_clicked(self):
        self.window.title("Create Your Account")
        self.show_frame(self.account_create)
    
    def user_log_in_clicked(self):
        self.window.title("User Log In")
        self.show_frame(self.user_log_in)
    
    def user_update_button_clicked(self):
        self.window.title("Update Account")
        self.user_update_account_menu()
        self.show_frame(self.user_update_info)
    
    def user_pet_add_clicked(self):
        self.window.title("Add a Pet(s)")
        if (isinstance(label, Label)):
            label.destroy()
            self.pet_register()
            self.show_frame(self.user_pet_add)
        else:
            self.pet_register()
            self.show_frame(self.user_pet_add)
    
    # Opens the update pet menu on click (for users)
    def user_update_pet_button_clicked(self):
        self.window.title("Update Pet Information")
        self.user_update_pet_menu()
        self.show_frame(self.user_update_pet_info)
    
    def user_schedule_appointment(self):
        self.window.title("Schedule Appointment")
        self.user_schedule_submenu()
        self.show_frame(self.user_calendar_frame)
    
    def user_manage_appointment_clicked(self):
        self.window.title("Manage Appointments")
        self.cancel_appointment()
        self.show_frame(self.cancel_menu_frame)
    
    def user_searchvet_clicked(self):
        self.window.title("Search for Vets")
        self.user_searchvet()
        self.show_frame(self.user_searchvet_frame)


    def user_menu_launch(self):
        self.window.title("User Menu")
        if(isinstance(label,Label)):
            label.destroy()
            self.clear_user_frame()
            self.show_frame(self.user_menu)
        else:
            self.clear_user_frame()
            self.show_frame(self.user_menu)
    
    def clear_user_frame(self):
        
        for widgets in self.account_create.winfo_children():
            widgets.destroy()
        self.account_create.pack_forget()
        
        for widgets in self.user_log_in.winfo_children():
            widgets.destroy()
        self.user_log_in.pack_forget()
        
        for widgets in self.user_update_info.winfo_children():
            widgets.destroy()
        self.user_update_info.pack_forget()
        
        for widgets in self.user_pet_add.winfo_children():
            widgets.destroy()
        self.user_pet_add.pack_forget()
        
        for widgets in self.user_update_pet_info.winfo_children():
            widgets.destroy()
        self.user_update_pet_info.pack_forget()
        
        for widgets in self.user_appointment.winfo_children():
            widgets.destroy()
        self.user_appointment.pack_forget()
        
        for widgets in self.user_calendar_frame.winfo_children():
                widgets.destroy()
        self.user_calendar_frame.pack_forget()
        
        for widgets in self.cancel_menu_frame.winfo_children():
                widgets.destroy()
        self.cancel_menu_frame.pack_forget()
        
        for widgets in self.user_searchvet_frame.winfo_children():
                widgets.destroy()
        self.user_searchvet_frame.pack_forget()
        
    def return_to_main(self):
        self.window.title("Home")
        if(isinstance(label,Label)):
            label.destroy()
            self.clear_user_frame()
            self.user_register()
            self.user_login()
            self.show_frame(self.account_page)
        else:
            self.clear_user_frame()
            self.user_register()
            self.user_login()
            self.show_frame(self.account_page)

        ##################################################################################################################################################

        # Menu that appears after successful user login
        # Provides the options to update account info or log out
    def user_after_login_menu(self):
        selectlabel = Label(self.user_menu, text="Select Your Choice", font='times 50 bold', bg='SpringGreen4', anchor=N, pady=50)
        selectlabel.pack(fill = "both")

        usermenuframe = Frame(self.user_menu)
        usermenuframe.pack()

        updateaccount = Button(usermenuframe, text="Update Account Info", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command =lambda:self.user_update_button_clicked())
        addpet = Button(usermenuframe, text="Add New Pet", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command =lambda:self.user_pet_add_clicked())
        managepet = Button(usermenuframe, text="Manage Pet Info", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command =lambda:self.user_update_pet_button_clicked())
        scheduleappt = Button(usermenuframe, text="Schedule Appointment", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command =lambda:self.user_schedule_appointment())
        manageappt = Button(usermenuframe, text="Manage Appointments", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command =lambda:self.user_manage_appointment_clicked())
        searchappt = Button(usermenuframe, text="Search For Vets", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command =lambda:self.user_searchvet_clicked())
        logout = Button(usermenuframe, text="Log Out", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = self.return_to_main)

        Label(usermenuframe, text = " ", font = "times 15").grid(row = 1, column = 2)
        updateaccount.grid(row = 2, column = 1)
        Label(usermenuframe, text = " ", font = "times 15").grid(row = 3, column = 2)
        addpet.grid(row = 4, column = 1)
        Label(usermenuframe, text = " ", font = "times 15").grid(row = 5, column = 2)
        managepet.grid(row = 6, column = 1)
        Label(usermenuframe, text = " ", font = "times 15").grid(row = 1, column = 2)
        scheduleappt.grid(row = 2, column = 3)
        Label(usermenuframe, text = " ", font = "times 15").grid(row = 3, column = 2)
        manageappt.grid(row = 4, column = 3)
        Label(usermenuframe, text = " ", font = "times 15").grid(row = 5, column = 2)
        searchappt.grid(row = 6, column = 3)
        Label(usermenuframe, text = " ", font = "times 15").grid(row = 7, column = 2)
        logout.grid(row = 8, column = 2)

        usermenuframe.grid_columnconfigure(0, weight = 1)
        usermenuframe.grid_columnconfigure(4, weight = 1)

        ######################################################################################################################################
    
    def user_register(self):
        global username
        global password
        global username_entry
        global password_entry 
        username = StringVar()
        password = StringVar()

        Label(self.account_create, text="Please enter details below", font='times 50 bold', bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
        Label(self.account_create, text="").pack()
        username_lable = Label(self.account_create, font='times 20', text="Username")
        username_lable.pack()
        username_entry = Entry(self.account_create, font='times 20', textvariable=username)
        username_entry.pack()
        password_lable = Label(self.account_create, font='times 20', text="Password")
        password_lable.pack()
        password_entry = Entry(self.account_create, font='times 20', textvariable=password, show='*')
        password_entry.pack()
        Label(self.account_create, text="").pack()
        Button(self.account_create, text="Register", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = self.register_user).pack()
        Label(self.account_create, text="").pack()
        Button(self.account_create, text="Return to Main Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = self.return_to_main).pack()

        # Registered user login menu
    def register_user(self):
        global label
        global user_login_ID 
        username_info = username.get()
        password_info = password.get()

        user_login_ID = None
        if(username_info == "" or password_info == ""):
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            self.empty_login_info()
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

                label = Label(self.account_create, text="Registration Successful", fg="green", font="times 15")
                label.pack() 
            else:
                username_entry.delete(0, END)
                password_entry.delete(0, END)
                self.username_taken()

        # Tells the user that the username they're trying to register with was taken
    def username_taken(self):
        global username_taken_screen
        username_taken_screen = Toplevel(self.window)
        username_taken_screen.title("Alerts")
        username_taken_screen.geometry("300x150")
        Label(username_taken_screen, text="Username is already taken").pack()
        Button(username_taken_screen, text="OK", command=self.delete_username_taken).pack()

        # Closes the username_taken() pop-up
    def delete_username_taken(self):
        username_taken_screen.destroy()

        # Tells the user that a required field was empty
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
        ###########################################################################################################################

        # Registered user login (prompts the user to enter their login info, passes info to user_login_verify for verification)
    def user_login(self):
        Label(self.user_log_in, text="Please enter details below to login", font="times 50 bold", bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
        Label(self.user_log_in, text="").pack()

        global username_verify
        global password_verify

        username_verify = StringVar()
        password_verify = StringVar()

        global username_login_entry
        global password_login_entry

        Label(self.user_log_in, font="times 20", text="Username").pack()
        username_login_entry = Entry(self.user_log_in, font="times 20", textvariable=username_verify)
        username_login_entry.pack()
        Label(self.user_log_in, text="").pack()
        Label(self.user_log_in, font="times 20", text="Password").pack()
        password_login_entry = Entry(self.user_log_in, font="times 20", textvariable=password_verify, show= '*')
        password_login_entry.pack()
        Label(self.user_log_in, text="").pack()
        Button(self.user_log_in, text="Login", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = self.user_login_verify).pack()
        Label(self.user_log_in, text="").pack()
        Button(self.user_log_in, text="Return to Main Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = self.return_to_main).pack()

    #user_id1 = NONE
    # User login verification (checks that the entered user information matches a record in the UserLoginInfo table)
    def user_login_verify(self):
        global label
        global username1
        global password1
        username1 = username_verify.get()
        password1 = password_verify.get() 
        user_login_ID = NONE
        if(username1 == "" or password1 == ""): 
            self.user_invalid_login()
        else: 
            user_login_ID = user.getUserLoginID(self)
            if(user_login_ID != None): 
                self.user_menu_launch() 
            else:
                self.user_invalid_login()


    def getUserID(self):
        #global user_id1

        user_login_ID = user.getUserLoginID(self)

        cursor.execute("select UserID from UserAccountInfo where UserLoginID = ?", user_login_ID)
        user_id1 = cursor.fetchone()

        return user_id1

    def getUserLoginID(self):
        global user_login_ID

        username1 = username_verify.get()
        password1 = password_verify.get()

        cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username1, password1)
        user_login_ID = cursor.fetchone()

        return user_login_ID

        # Tells the user that their login was invalid (whatever they entered didn't match anything in the UserLoginInfo table)
    def user_invalid_login(self):
        global invalid_login_screen
        invalid_login_screen = Toplevel(self.window)
        invalid_login_screen.title("Alert")
        invalid_login_screen.geometry("300x150")
        Label(invalid_login_screen, text="Invalid Login ").pack()
        Button(invalid_login_screen, text="OK", command=self.delete_user_invalid_login).pack()

        # Removes the user_invalid_login() pop-up on click
    def delete_user_invalid_login(self):
        invalid_login_screen.destroy()
        ###################################################################################################################################################

        # Menu that appears when the registered user clicks the update account info button
        # Takes in user's inputs and sends it to the user_update_account() function for processing
    def user_update_account_menu(self):
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

        
        temp_user_id =  user.getUserID(self)
        my_data = cursor.execute("SELECT Concat(UserFirstName, ', ', UserLastName, ', ', UserEmailAddress, ', ', UserPhoneNumber, ', ', UserStreetAddress, ', ', UserCity, ', ', UserState, ', ', UserZip) FROM USERACCOUNTINFO WHERE USERID = ?", temp_user_id) # SQLAlchem engine result
        my_list = [r for r, in my_data] # create a  list 
        sel = my_list[0].split(", ")
        
        Label(self.user_update_info, text="").pack()
        first_name_label = Label(self.user_update_info, text='First Name', font="times 15")
        first_name_entry = Entry(self.user_update_info, font="times 15", width=20, textvariable=first_name_var)
        first_name_entry.insert(0, sel[0])
        first_name_label.pack()
        first_name_entry.pack()

        last_name_label = Label(self.user_update_info, text='Last Name', font="times 15")
        last_name_entry = Entry(self.user_update_info, textvariable=last_name_var, font="times 15", width=20)
        last_name_entry.insert(0, sel[1])
        last_name_label.pack()
        last_name_entry.pack()

        email_label = Label(self.user_update_info, text='Email', font="times 15")
        email_entry = Entry(self.user_update_info, textvariable=email_var, font="times 15")
        email_entry.insert(0, sel[2])
        email_label.pack()
        email_entry.pack()

        phone_number_label = Label(self.user_update_info, text='Phone Number', font="times 15")
        phone_number_entry = Entry(self.user_update_info, textvariable=phone_number_var, font="times 15")
        phone_number_entry.insert(0, sel[3])
        phone_number_label.pack()
        phone_number_entry.pack()

        street_address_label = Label(self.user_update_info, text='Street Address', font="times 15")
        street_address_entry = Entry(self.user_update_info, textvariable=street_address_var, font="times 15")
        street_address_entry.insert(0, sel[4])
        street_address_label.pack()
        street_address_entry.pack()

        city_label = Label(self.user_update_info, text='City', font="times 15")
        city_entry = Entry(self.user_update_info, textvariable=city_var, font="times 15")
        city_entry.insert(0, sel[5])
        city_label.pack()
        city_entry.pack()

        state_label = Label(self.user_update_info, text='State', font="times 15")
        state_entry = Entry(self.user_update_info, textvariable=state_var, font="times 15")
        state_entry.insert(0, sel[6])
        state_label.pack()
        state_entry.pack()

        zip_label = Label(self.user_update_info, text='Zip Code', font="times 15")
        zip_entry = Entry(self.user_update_info, textvariable=zip_var, font="times 15")
        zip_entry.insert(0, sel[7])
        zip_label.pack()
        zip_entry.pack()

        Label(self.user_update_info, text="").pack()
        Button(self.user_update_info, text='Submit', width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = self.user_update_account).pack()
        Label(self.user_update_info, text="").pack()
        Button(self.user_update_info, text="Return to User Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = self.user_menu_launch).pack()
        ####################################################################################################################################################################

        # Menu that appears when the registered user clicks the update pet info button
        # Allows the user to view pet(s) on file 
        # Takes in user's inputs and sends it to the user_update_pet() function for processing
    def user_update_pet_menu(self):
        global pet_name_var
        pet_name_var= StringVar()
        global pet_type_var
        pet_type_var = StringVar()
        global pet_breed_var
        pet_breed_var = StringVar()
        global pet_color_var
        pet_color_var = StringVar()

        global pet_name_entry1
        global pet_type_entry1
        global pet_breed_entry1
        global pet_color_entry1
        global pet_info_query
        global pet_info_query_data
        global pet_info_dictionary
        global pet_info_list
        global pet_info_selection
        global pet_info_combobox
        global pet_info_display

        #list of pets and their info from the query
        #user_id1 = getUserID()

        user_id1 = self.getUserID()
        pet_info_query_data = list(cursor.execute("select * from PetInfo where UserID =?", user_id1))
        pet_info_dictionary = {}
        pet_info_list = []

        #Label(user_update_pet_info, text=str(user_id1)).pack()
        #creates a dictionary list of the pets selected from the table and appends their id and name data
        for tablerow in pet_info_query_data:
            pet_info_dictionary[[tablerow][0][0]] = tablerow
            pet_info_list.append(tablerow[1]) #appends index 1 to the list
        Label(self.user_update_pet_info, text="Update Pet(s)", font='times 50 bold', bg="SpringGreen4", anchor=N).pack(fill=BOTH)
        
        Label(self.user_update_pet_info, text="").pack()

        #combobox creation and configuration
        pet_info_selection = tk.StringVar()
        Label(self.user_update_pet_info, text="Select a Pet", font="times 15 bold").pack()
        pet_info_combobox = ttk.Combobox(self.user_update_pet_info, textvariable = pet_info_selection, values = pet_info_list)
        pet_info_combobox.pack(pady = 20)
        pet_info_display = Label(self.user_update_pet_info, text = "Pet Info:", bg = "SpringGreen4")
        pet_info_display.pack()
        pet_info_selection.trace("w", self.pet_selection_display)

        pet_name_label = Label(self.user_update_pet_info, text='Pet Name', font="times 15")
        pet_name_entry1 = Entry(self.user_update_pet_info, font="times 15", width=20, textvariable=pet_name_var)
        pet_name_label.pack()
        pet_name_entry1.pack()

        pet_type_label = Label(self.user_update_pet_info, text='Pet Type', font="times 15")
        pet_type_entry1 = Entry(self.user_update_pet_info, textvariable=pet_type_var, font="times 15", width=20)
        pet_type_label.pack()
        pet_type_entry1.pack()

        pet_breed_label = Label(self.user_update_pet_info, text='Pet Breed', font="times 15")
        pet_breed_entry1 = Entry(self.user_update_pet_info, textvariable=pet_breed_var, font="times 15")
        pet_breed_label.pack()
        pet_breed_entry1.pack()

        pet_color_label = Label(self.user_update_pet_info, text='Pet Color', font="times 15")
        pet_color_entry1 = Entry(self.user_update_pet_info, textvariable=pet_color_var, font="times 15")
        pet_color_label.pack()
        pet_color_entry1.pack()

        Label(self.user_update_pet_info, text="").pack()

        Button(self.user_update_pet_info, text='Update Pet', width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = self.pet_confirmation_popup).pack()
        Label(self.user_update_pet_info, text="").pack()
        Button(self.user_update_pet_info, text='Delete Pet', width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = self.pet_del_confirmation_popup).pack()
        Label(self.user_update_pet_info, text="").pack()
        Button(self.user_update_pet_info, text="Return to User Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = self.user_menu_launch).pack()
        #creates a display for pet info based on selection
        
    def pet_selection_display(*args):
        pet_info_display.config(text = "")

        for i, j in pet_info_dictionary.items():
            if j[1] == pet_info_selection.get():
                pet_info_display.config(text = str(j[0]) + ", " + j[1] + ", " + j[2] + ", " + j[3] + "," + j[4])
                global user_pet_id 
                global user_id 
                user_pet_id =  j[0] # stores the users selecion for update
                user_id = j[5] # stores the user selection for update

    def pet_confirmation_popup(self):
        global pet_confirmation
        pet_confirmation = Toplevel(self.window)
        pet_confirmation.title("Alert")
        pet_confirmation.geometry("300x150")
        Label(pet_confirmation, text=f'You selected {pet_info_selection.get()}.').pack()
        Button(pet_confirmation, text="Update", command=self.pet_confirmation_update).pack()
        Button(pet_confirmation, text="No", command=self.pet_confirmation_des).pack()

    def pet_confirmation_update(self):
        pet_name_var = pet_name_entry1.get()
        pet_type_var = pet_type_entry1.get()
        pet_breed_var = pet_breed_entry1.get()
        pet_color_var = pet_color_entry1.get()

        cursor.execute("UPDATE PetInfo SET PetName = ?, PetType = ?, PetBreed = ?, PetColor = ? WHERE PetID = ?", pet_name_var, pet_type_var, pet_breed_var, pet_color_var, user_pet_id)
        cursor.commit()
        pet_name_entry1.delete(0, END)
        pet_type_entry1.delete(0, END)
        pet_breed_entry1.delete(0, END)
        pet_color_entry1.delete(0, END)
        label = Label(self.user_update_pet_info, text ="Update Successful")
        label.pack()
        self.pet_confirmation_des()

    def pet_confirmation_des(self):
        pet_confirmation.destroy()

    
    def pet_del_confirmation_popup(self):
        global pet_del_confirmation
        pet_del_confirmation = Toplevel(self.window)
        pet_del_confirmation.title("Alert")
        pet_del_confirmation.geometry("300x150")
        Label(pet_del_confirmation, text=f'You selected {pet_info_selection.get()}.').pack()
        Button(pet_del_confirmation, text="Delete", command=self.pet_del_confirmation_update).pack()
        Button(pet_del_confirmation, text="No", command=self.pet_del_confirmation_des).pack()

    def pet_del_confirmation_update(self):

        cursor.execute("DELETE FROM PetInfo WHERE PetID = ?", user_pet_id)
        cursor.commit()
        pet_name_entry1.delete(0, END)
        pet_type_entry1.delete(0, END)
        pet_breed_entry1.delete(0, END)
        pet_color_entry1.delete(0, END)
        label = Label(self.user_update_pet_info, text ="Deletion Successful")
        label.pack()
        self.pet_del_confirmation_des()

    def pet_del_confirmation_des(self):
        pet_del_confirmation.destroy()
    

        ####################################################################################################################################################################

        # Takes inputs from user_update_account_menu() and finds user's LoginID from the UserLoginInfo table
        # to update the correct records in the UserAccountInfo table
    def user_update_account(self):
        global label
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
        Label(self.user_update_info, text="").pack()
        label = Label(self.user_update_info, text="Update Successful", fg="green", font="times 15")
        label.pack()

        ##################################################################################################################################################

        # Takes inputs from user_update_pet_menu() and finds user's LoginID from the UserLoginInfo table
        # to update the correct records in the UserAccountInfo table
    def user_update_pet(self):
        global label
        pet_name_var = pet_name_entry1.get()
        pet_type_var = pet_type_entry1.get()
        pet_breed_var = pet_breed_entry1.get()
        pet_color_var = pet_color_entry1.get()

        cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username1, password1)
        user_login_ID = cursor.fetchone()
        cursor.execute("SELECT PetID FROM PetInfo INNER JOIN UserLoginInfo ON PetInfo.UserLoginID = UserLoginInfo.UserLoginID WHERE PetInfo.UserLoginID = ?", user_login_ID)
        user_id = cursor.fetchone()
        cursor.execute("UPDATE PetInfo SET PetName = ?, PetType = ?, PetBreed = ?, PetColor = ? WHERE PetID = ?", pet_name_var, pet_type_var, pet_breed_var, pet_color_var, user_id[0])
        cursor.commit()
        pet_name_entry1.delete(0,END)
        pet_type_entry1.delete(0,END)
        pet_breed_entry1.delete(0,END)
        pet_color_entry1.delete(0,END)

        label = Label(self.user_update_info, text="Update Successful", fg="green", font="times 15")
        label.pack()


        # Pet registration menu
    def pet_register(self):
        global pet_name_var
        pet_name_var= StringVar()
        global pet_type_var
        pet_type_var = StringVar()
        global pet_breed_var
        pet_breed_var = StringVar()
        global pet_color_var
        pet_color_var = StringVar()

        global pet_name_entry
        global pet_type_entry
        global pet_breed_entry
        global pet_color_entry

        Label(self.user_pet_add, text="Add a Pet(s)", font='times 50 bold', bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
        Label(self.user_pet_add, text="").pack()

        pet_name_label = Label(self.user_pet_add, text='Pet Name', font="times 15")
        pet_name_entry = Entry(self.user_pet_add, font="times 15", width=20, textvariable=pet_name_var)
        pet_name_label.pack()
        pet_name_entry.pack()

        pet_type_label = Label(self.user_pet_add, text='Pet Type', font="times 15")
        pet_type_entry = Entry(self.user_pet_add, textvariable=pet_type_var, font="times 15", width=20)
        pet_type_label.pack()
        pet_type_entry.pack()

        pet_breed_label = Label(self.user_pet_add, text='Pet Breed', font="times 15")
        pet_breed_entry = Entry(self.user_pet_add, textvariable=pet_breed_var, font="times 15")
        pet_breed_label.pack()
        pet_breed_entry.pack()

        pet_color_label = Label(self.user_pet_add, text='Pet Color', font="times 15")
        pet_color_entry = Entry(self.user_pet_add, textvariable=pet_color_var, font="times 15")
        pet_color_label.pack()
        pet_color_entry.pack()

        Label(self.user_pet_add, text="").pack()
        Button(self.user_pet_add, text='Register Pet', width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = self.register_pet).pack()
        Label(self.user_pet_add, text="").pack()
        Button(self.user_pet_add, text="Return to User Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = self.user_menu_launch).pack()

        ######################################################################################################################################

        # Registered pet menu
    def register_pet(self):
        global label
        global pet_id 
        pet_name_info = pet_name_entry.get()
        pet_type_info = pet_type_entry.get()
        pet_breed_info = pet_breed_entry.get()
        pet_color_info = pet_color_entry.get()

        user_login_ID = None
        pet_id = None
        if(pet_name_info == "" or pet_type_info == "" or pet_breed_info == "" or pet_color_info == ""):
            pet_name_entry.delete(0, END)
            pet_type_entry.delete(0, END)
            pet_breed_entry.delete(0, END)
            pet_color_entry.delete(0, END)
            self.empty_login_info()
        else:
            cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username1, password1)
            user_login_ID = cursor.fetchone()
            cursor.execute("SELECT UserID FROM UserAccountInfo INNER JOIN UserLoginInfo ON UserAccountInfo.UserLoginID = UserLoginInfo.UserLoginID WHERE UserAccountInfo.UserLoginID = ?", user_login_ID)
            user_id = cursor.fetchone()
            cursor.execute("INSERT INTO PetInfo VALUES(?,?,?,?,?)", pet_name_info, pet_type_info, pet_breed_info, pet_color_info, user_id[0])
            cursor.execute("SELECT PetID FROM PetInfo WHERE PetName = ? AND PetType = ? AND PetBreed = ? AND PetColor = ?", pet_name_info, pet_type_info, pet_breed_info, pet_color_info)
            pet_id = cursor.fetchone() 
            cursor.commit()

        pet_name_entry.delete(0, END)
        pet_type_entry.delete(0, END)
        pet_breed_entry.delete(0, END)
        pet_color_entry.delete(0, END)

        Label(self.user_pet_add, text="").pack()

        label = Label(self.user_pet_add, text="Registration Successful", fg="green", font="times 15")
        label.pack() 

    def user_schedule_submenu(self):
        
        global schedule_label
        global button_frame
        global command_button
        #Calendar
        calendar_display_frame = tk.Frame(self.user_calendar_frame)
        calendar_display_frame.pack(anchor = "nw", side=LEFT, expand=False, fill = "both")
        cal = Calendar(calendar_display_frame, selectmode = 'day', year = 2023, month = 4, day = 17)

        cal.grid(row=0, column = 1)

        calendar_display_frame.grid_columnconfigure(0, weight=1)
        calendar_display_frame.grid_columnconfigure(6, weight=1)
        
        schedule_label = Frame(self.user_calendar_frame)
        schedule_label.pack(side=LEFT, anchor="ne")
        schedule_label.grid_columnconfigure(0, weight=1)
        schedule_label.grid_columnconfigure(6, weight=1)
        
        command_button = Frame(self.user_calendar_frame)
        command_button.pack(side = LEFT, anchor="se")
        command_button.grid_columnconfigure(0, weight = 1)
        command_button.grid_columnconfigure(2, weight = 1)

        button_frame = Frame(self.user_calendar_frame, highlightbackground="SpringGreen4", highlightthickness=2)
        button_frame.pack(side=LEFT, anchor="center")
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(6, weight=1)
        
        
        query = "SELECT Concat(VetID, ', ', VetFirstName, ', ', VetLastName, ', ', Specialization) FROM VETACCOUNTINFO"
        
        ##drop down for vets
        global cal_view_vet_menu_label
        cal_view_vet_menu_label = Label(calendar_display_frame, text = "Select a Vet", font = "times 15 bold")
        cal_view_vet_menu_label.grid(row=1, column=1)
        my_data = cursor.execute(query) # SQLAlchem engine result
        global vetlist
        vetlist = [r for r, in my_data] # create a list 

        sel=tk.StringVar()
        global vetsel
        vetsel = ttk.Combobox(calendar_display_frame, values=vetlist,width=25,textvariable = sel)
        vetsel.grid(row=2, column=1)


        but = Button(calendar_display_frame, text="Generate Time Slots", width=20, height=1, font='times 10', bd=20, bg='SpringGreen4', command = lambda:createScheduleButtons())
        but.grid(row=7, column = 1)
        Button(calendar_display_frame, text="Return to User Menu", width=20, height=1, font='times 10 bold', bd=20, bg='SpringGreen4', command = self.user_menu_launch).grid(row=8, column=1)
        
        def schedule_retrieval(event):
            global schedule_label
            for widget in schedule_label.winfo_children():
                widget.destroy()

            sel = vetsel.get().split(",")

            my_list1 = list()
            my_list2 = list()
            my_list3 = list()
            my_list4 = list()
            my_list5 = list()
            my_list6 = list()
            my_list7 = list()
            
            my_list8 = list()
            my_list9 = list()
            my_list10 = list()
            my_list11 = list()
            my_list12 = list()
            my_list13 = list()
            my_list14 = list()
            my_list15 = list()
            
            Label(schedule_label, text="Vet Schedule", font="Times 10 bold").grid(row=0, column=2)

            Label(schedule_label, text="Monday", font="Times 10 bold").grid(row=1, column=1)
            monday_vet_id = cursor.execute("SELECT Monday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list1.append([r for r, in monday_vet_id])
            monday_label = Label(schedule_label, text=my_list1[0], font="times 10 bold")
            monday_label.grid(row=1, column=3)

            Label(schedule_label, text="Tuesday", font="Times 10 bold").grid(row=2, column=1)
            tuesday_vet_id = cursor.execute("SELECT Tuesday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list2.append([r for r, in tuesday_vet_id])
            tuesday_label = Label(schedule_label, text=my_list2[0], font="times 10 bold")
            tuesday_label.grid(row=2, column=3)

            Label(schedule_label, text="Wednesday", font="Times 10 bold").grid(row=3, column=1)
            wednesday_vet_id = cursor.execute("SELECT Wednesday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list3.append([r for r, in wednesday_vet_id])
            wednesday_label = Label(schedule_label, text=my_list3[0], font="times 10 bold")
            wednesday_label.grid(row=3, column=3)

            Label(schedule_label, text="Thursday", font="Times 10 bold").grid(row=4, column=1)
            thursday_vet_id = cursor.execute("SELECT Thursday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list4.append([r for r, in thursday_vet_id])
            thursday_label = Label(schedule_label, text=my_list4[0], font="times 10 bold")
            thursday_label.grid(row=4, column=3)

            Label(schedule_label, text="Friday", font="Times 10 bold").grid(row=5, column=1)
            friday_vet_id = cursor.execute("SELECT Friday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list5.append([r for r, in friday_vet_id])
            friday_label = Label(schedule_label, text=my_list5[0], font="times 10 bold")
            friday_label.grid(row=5, column=3)

            Label(schedule_label, text="Saturday", font="Times 10 bold").grid(row=6, column=1)
            saturday_vet_id = cursor.execute("SELECT Saturday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list6.append([r for r, in saturday_vet_id])
            saturday_label = Label(schedule_label, text=my_list6[0], font="times 10 bold")
            saturday_label.grid(row=6, column=3)

            Label(schedule_label, text="Sunday", font="Times 10 bold").grid(row=7, column=1)
            sunday_vet_id = cursor.execute("SELECT Sunday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
            my_list7.append([r for r, in sunday_vet_id])
            sunday_label = Label(schedule_label, text=my_list7[0], font="times 10 bold")
            sunday_label.grid(row=7, column=3)


            Label(schedule_label, text="Vet Information", font="Times 10 bold").grid(row=0, column=6)
            
            Label(schedule_label, text="First Name", font="Times 10 bold").grid(row=1, column=5)
            first_name = cursor.execute("SELECT VetFirstName FROM VETAccountINFO WHERE VETID = ?", sel[0])
            my_list8.append([r for r, in first_name])
            first_name_label = Label(schedule_label, text=my_list8[0], font="times 10 bold")
            first_name_label.grid(row=1, column=7)

            Label(schedule_label, text="Last Name", font="Times 10 bold").grid(row=2, column=5)
            last_name = cursor.execute("SELECT VetLastName FROM VETAccountINFO WHERE VETID = ?", sel[0])
            my_list9.append([r for r, in last_name])
            last_name_label = Label(schedule_label, text=my_list9[0], font="times 10 bold")
            last_name_label.grid(row=2, column=7)

            Label(schedule_label, text="Phone Number", font="Times 10 bold").grid(row=3, column=5)
            phone_number = cursor.execute("SELECT VetPhoneNumber FROM VETAccountINFO WHERE VETID = ?", sel[0])
            my_list10.append([r for r, in phone_number])
            phone_number_label = Label(schedule_label, text=my_list10[0], font="times 10 bold")
            phone_number_label.grid(row=3, column=7)

            Label(schedule_label, text="Email Address", font="Times 10 bold").grid(row=4, column=5)
            email_address  = cursor.execute("SELECT VetEmailAddress FROM VETAccountINFO WHERE VETID = ?", sel[0])
            my_list11.append([r for r, in email_address])
            email_address_label = Label(schedule_label, text=my_list11[0], font="times 10 bold")
            email_address_label.grid(row=4, column=7)

            Label(schedule_label, text="Street Address", font="Times 10 bold").grid(row=5, column=5)
            street_address  = cursor.execute("SELECT VetStreetAddress FROM VETAccountINFO WHERE VETID = ?", sel[0])
            my_list12.append([r for r, in street_address])
            street_address_label = Label(schedule_label, text=my_list12[0], font="times 10 bold")
            street_address_label.grid(row=5, column=7)

            Label(schedule_label, text="City", font="Times 10 bold").grid(row=6, column=5)
            city  = cursor.execute("SELECT VetCity FROM VETAccountINFO WHERE VETID = ?", sel[0])
            my_list13.append([r for r, in city])
            city_label = Label(schedule_label, text=my_list13[0], font="times 10 bold")
            city_label.grid(row=6, column=7)

            Label(schedule_label, text="State", font="Times 10 bold").grid(row=7, column=5)
            state  = cursor.execute("SELECT VetState FROM VETAccountINFO WHERE VETID = ?", sel[0])
            my_list14.append([r for r, in state])
            state_label = Label(schedule_label, text=my_list14[0], font="times 10 bold")
            state_label.grid(row=7, column=7)
            
            Label(schedule_label, text="Zip", font="Times 10 bold").grid(row=8, column=5)
            zip  = cursor.execute("SELECT VetZip FROM VETAccountINFO WHERE VETID = ?", sel[0])
            my_list15.append([r for r, in zip])
            zip_label = Label(schedule_label, text=my_list15[0], font="times 10 bold")
            zip_label.grid(row=8, column=7)
            
            
        vetsel.bind("<<ComboboxSelected>>", schedule_retrieval)
        
        pet_label = Frame(self.user_calendar_frame)
        pet_label.pack(fill="x", anchor="n")
        global label
        label = Label(calendar_display_frame, text='Select your Pet', font="times 15")
        label.grid(row = 3, column = 1)
        user_id1 = self.getUserID()        
        my_data = cursor.execute("SELECT Concat(PetID, ', ', PetName) FROM PetInfo Where UserID = ?", user_id1) # SQLAlchem engine result
        my_list = [r for r, in my_data] # create a  list 

        sel=tk.StringVar()

        cb2 = ttk.Combobox(calendar_display_frame, values=my_list,width=25,textvariable = sel)
        cb2.grid(row = 4, column = 1)
        
        label1 = Label(calendar_display_frame, text='Enter Reason for Appointment', font="times 15")
        label1.grid(row = 5, column = 1)
        
        appoint_desc = Text(calendar_display_frame,height=10, width=45, font="times 15")
        appoint_desc.grid(row = 6, column = 1)
        
        pet_label.grid_columnconfigure(0, weight = 1)
        pet_label.grid_columnconfigure(2, weight = 1)
        #Creates dropdown of vet's schedule based on id, and displays each day as a option
        ###################################################################################
        def createScheduleButtons():
            global time_interval
            global date_str
            sel = vetsel.get().split(",")
            my_list2 = list()
            
            date_str  = cal.get_date()
            dateObj = datetime.strptime(date_str,'%m/%d/%y')
            date = dateObj.weekday()
            match date:
                case 0:
                    my_data2 = cursor.execute("SELECT Monday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
                    my_list2.append([r for r, in my_data2])
                    time_interval = findTimeInterval(my_list2)
                case 1:
                    my_data2 = cursor.execute("SELECT Tuesday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
                    my_list2.append([r for r, in my_data2])
                    time_interval = findTimeInterval(my_list2) 
                case 2:
                    my_data2 = cursor.execute("SELECT Wednesday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
                    my_list2.append([r for r, in my_data2])
                    time_interval = findTimeInterval(my_list2) 
                case 3:
                    my_data2 = cursor.execute("SELECT Thursday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
                    my_list2.append([r for r, in my_data2])
                    time_interval = findTimeInterval(my_list2) 
                case 4:
                    my_data2 = cursor.execute("SELECT Friday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
                    my_list2.append([r for r, in my_data2])
                    time_interval = findTimeInterval(my_list2) 
                case 5:
                    my_data2 = cursor.execute("SELECT Saturday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
                    my_list2.append([r for r, in my_data2])
                    time_interval = findTimeInterval(my_list2) 
                case 6:
                    my_data2 = cursor.execute("SELECT Sunday FROM VETSCHEDULEINFO WHERE VETID = ?", sel[0])
                    my_list2.append([r for r, in my_data2])
                    time_interval = findTimeInterval(my_list2)
            global button_frame
            for widget in button_frame.winfo_children():
                widget.destroy()
            my_list2 = [r for r, in my_list2]
            temp = my_list2[0].split(":")
            counter_start = int(temp[0])
            counter_end = int(temp[0]) + 1
            if(counter_end == 13):
                    temp[3] = 'pm'
                    counter_end = 1
            counter_column = 0
            global butt
            Label(button_frame, text='Time Slots', font="times 15").grid(row = 0, column = 0)
            for i in range(time_interval):
                if(counter_start == 12):
                        temp[1] = 'pm'
                if((temp[1] == 'pm' and counter_end < 12) or counter_end == 12):
                        temp[3] = 'pm'
                else:
                        temp[3] = 'am'
                if(counter_end == 13):
                        temp[3] = 'pm'
                        counter_end = 1
                strung = str(counter_start) + " " + temp[1] + " - " + str(counter_end) + " " + temp[3]
                cursor.execute("SELECT Date, Time FROM APPOINTMENTINFO WHERE Date = ? AND Time = ?",date_str, strung) # Needs date also
                cursor.commit()
                if(cursor.rowcount != 0):
                        if(counter_start == 12):
                            counter_start = 0
                        if(counter_end == 13):
                            counter_end = 1
                        counter_start+=1
                        counter_end+=1
                        counter_column+=1
                        continue
                else:
                        if(counter_start == 12):
                            counter_start = 0
                        if(counter_end == 13):
                            counter_end = 1
                        butt = Button(button_frame,text=strung, width=10, height = 1, font = 'times 10', bd=20, bg='SpringGreen4', command = lambda button_text = strung : createAppointmentPopUp(button_text))
                        butt.grid(row = 10, column = counter_column)
                        counter_start+=1
                        counter_end+=1
                        counter_column+=1
        
        #Finds the time interval of the list of schedule hours
        #####################################################################################################    
        def findTimeInterval(my_list2):
            my_list2 = [r for r, in my_list2]
            temp = my_list2[0].split(":")
            if(temp[1] == "am" and temp[3] == "am"):
                time_interval = int(temp[2]) - int(temp[0])
            elif(temp[1] == "pm" and temp[3] == "pm"):
                time_interval = int(temp[2]) - int(temp[0])
            elif(temp[1] == "am" and temp[3] == "pm"):
                if(int(temp[2]) == 12):
                    x = int(temp[2])
                    time_interval = x - int(temp[0])
                else:
                    x = int(temp[2]) + 12
                    time_interval = x - int(temp[0])
            elif(temp[1] == "pm" and temp[3] == "am"):
                if(int(temp[0]) == 12):
                    x = int(temp[0])
                    time_interval = x - int(temp[2])
                else:
                    x = int(temp[0]) + 12
                    time_interval = x - int(temp[2])
            return  time_interval   
        
        ################################################################################################################################################   

        def createAppointmentPopUp(button_text):
            global appointmentPopUp
            appointmentPopUp = Toplevel(self.user_calendar_frame)
            global reason
            reason = appoint_desc.get('1.0','end-1c')
            Label(appointmentPopUp, text = "You are about to create an appointment with the following information:", font = "times 10").pack()
            Label(appointmentPopUp, text = f'Vet: {vetsel.get()}', font = "times 10").pack()
            Label(appointmentPopUp, text = f'Pet: {cb2.get()}', font = "times 10").pack()
            Label(appointmentPopUp, text = f'Reason: {reason}', font = "times 10").pack()
            Label(appointmentPopUp, text = f'Date: {date_str}', font = "times 10").pack()
            Label(appointmentPopUp, text = f'Time: {button_text}', font = "times 10").pack()
            Button(appointmentPopUp, text = "Schedule Appointment", font = "times 10", command = lambda : createAppointment(button_text)).pack()
            Button(appointmentPopUp, text = "Cancel", font = "times 10", command = destroyAppointmentPopup).pack()
        
        def destroyAppointmentPopup():
            appointmentPopUp.destroy()
            
        def createAppointment(button_text):
            user_id1 = self.getUserID()
            sel = vetsel.get().split(", ")
            sel2 = cb2.get().split(", ")
            cursor.execute("INSERT INTO APPOINTMENTINFO (DATE, TIME, VETID, USERID, PETID, APPOINTDESC) VALUES(?,?,?,?,?,?)",str(date_str), str(button_text), int(sel[0]), int(user_id1[0]), int(sel2[0]), str(reason))
            cursor.commit()
            for widgets in button_frame.winfo_children():
                widgets.destroy()
            destroyAppointmentPopup()
            
    def cancel_appointment(self):

        global cancel_true
        global cancel_false
        cancel_true = 1
        cancel_false = 0

        user_id1 = self.getUserID()

        apptData = cursor.execute("select concat(AppointmentID, ', ', Date, ', ', Time, ', ', VetAccountInfo.VetFirstName, ', ', VetAccountInfo.VetLastName, ', ', AppointmentInfo.PetID, ', ', PetInfo.PetName) from AppointmentInfo join VetAccountInfo on AppointmentInfo.VetID = VetAccountInfo.VetID join UserAccountInfo on AppointmentInfo.UserID = UserAccountInfo.UserID join PetInfo on AppointmentInfo.PetID = PetInfo.PetID where AppointmentInfo.UserID = ? AND AppointmentInfo.Cancelled = ?", user_id1[0], cancel_false)
        apptList = [r for r, in apptData]
        
        #combobox and entrybox variables
        global cancel_combobox
        global cancel_entrybox

        #textvariable for cancel_combobox and cancel_entrybox
        global cancel_cb_sel
        cancel_cb_sel = tk.StringVar()
        global cancel_eb_input
        cancel_eb_input = tk.StringVar()

        #label and frame creation and packing - combobox frame
        label_select_appt = tk.Label(self.cancel_menu_frame, text = "Select an Appointment to Cancel", font = "times 15")
        cancel_frame = tk.Frame(self.cancel_menu_frame)
        label_select_appt.pack(side = "top", fill = "both", expand = False)
        cancel_frame.pack(side = "top", fill = "x")

        #Creation of the combobox and entrybox and related labels
        combo_label = tk.Label(cancel_frame, text = "Appointments:", font='times 15')
        cancel_combobox = ttk.Combobox(cancel_frame, values = apptList, font = "times 15", textvariable = cancel_cb_sel, width = 30)
        entry_label = tk.Label(cancel_frame, text = "Enter a reason:", font='times 15')
        cancel_entrybox = tk.Entry(cancel_frame, textvariable = cancel_eb_input, width = 30, font = "times 15")
        blank_label = tk.Label(cancel_frame, text = "", font='times 15')
        #Grid
        combo_label.grid(row = 0, column = 1)
        cancel_combobox.grid(row = 1, column = 1)
        entry_label.grid(row = 2, column = 1)
        cancel_entrybox.grid(row = 3, column = 1)
        blank_label.grid(row = 4, column = 1)

        #Grid columnconfigure
        cancel_frame.grid_columnconfigure(0, weight = 1)
        cancel_frame.grid_columnconfigure(2, weight = 1)
        
        #Buttons
        Button(self.cancel_menu_frame, text="OK", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = lambda : cancelApptQuery()).pack()
        Button(self.cancel_menu_frame, text="Return to User Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = self.user_menu_launch).pack()

        def cancelApptQuery():
            global label
            sel = cancel_combobox.get().split(", ")
            cursor.execute("insert into CancellationInfo values (?,?)", sel[0], cancel_entrybox.get())
            cursor.execute("update AppointmentInfo set Cancelled = ? where AppointmentID = ?", cancel_true, sel[0])
            cursor.commit()
            label = Label(self.cancel_menu_frame, text = "Cancellation Success!", font = 'times 10').pack()      

    ########################################
    #user_searchvet allows registered users to search for vets based on a day of the week, specialization, and zip code
    global j
    j=0
    def user_searchvet(self):
        selectlabel = Label(self.user_searchvet_frame, text="Search for a Vet", font='times 25 bold', bg='SpringGreen4', anchor=N, pady=25)
        selectlabel.pack(fill = "both")
        
        #combobox and entrybox textvariables
        global day_tv
        day_tv = StringVar()
        global specialization_tv
        specialization_tv = StringVar()
        global zipcode_tv
        zipcode_tv = StringVar()

        #frames
        entryframe = Frame(self.user_searchvet_frame)
        entryframe.pack(side = "left", fill = "x", expand = False)

        global displayvetsframe
        displayvetsframe = Frame(self.user_searchvet_frame, highlightbackground="SpringGreen4", highlightthickness=2)
        displayvetsframe.pack(side = "right", anchor = "n")

        #ENTRYFRAME:
        #day of the week combobox
        day_label = Label(entryframe, text = 'Day of the Week', font = "times 15")
        day_cb = ttk.Combobox(entryframe, textvariable = day_tv, font="times 15")
        day_cb['values'] = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

        #specialization combobox
        special_label = Label(entryframe, text='Specialization', font="times 15")
        special_cb = ttk.Combobox(entryframe, textvariable = specialization_tv, font="times 15")
        special_cb['values'] = ('Check Ups', 'Surgery', 'Dentistry', 'Other')

        #zip code entrybox
        zipcode_label = Label(entryframe, text = 'Zip Code', font = "times 15")
        zipcode_entry = Entry(entryframe, textvariable = zipcode_tv, font = "times 15")

        #buttons
        searchbutton = Button(entryframe, text = "Search", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = lambda : display_vets())
        returntomenu = Button(entryframe, text="Return to User Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = self.user_menu_launch)

        #the griddy
        day_label.grid(row = 1, column = 2)
        day_cb.grid(row = 2, column = 2)
        Label(entryframe, text = " ", font = "times 15").grid(row = 3, column = 2)
        special_label.grid(row = 4, column = 2)
        special_cb.grid(row = 5, column = 2)
        Label(entryframe, text = " ", font = "times 15").grid(row = 6, column = 2)
        zipcode_label.grid(row = 7, column = 2)
        zipcode_entry.grid(row = 8, column = 2)
        Label(entryframe, text = " ", font = "times 15").grid(row = 9, column = 2)
        searchbutton.grid(row = 10, column = 2)
        Label(entryframe, text = " ", font = "times 15").grid(row = 11, column = 2)
        returntomenu.grid(row = 12, column = 2)
        
        #LABELFRAME:
        def display_vets():
            for widget in displayvetsframe.winfo_children():
                widget.destroy()

            day_cb_get = day_cb.get()
            special_cb_get = special_cb.get()
            zipcode_entry_get = zipcode_entry.get()


            cursor.execute("select Concat(VetAccountInfo.VetID, ',', 'Forename: ', VetAccountInfo.VetFirstName, ',', ' Surname: ', VetAccountInfo.VetLastName, ',', ' Phone: ', VetAccountInfo.VetPhoneNumber, ',', ' Email: ', VetAccountInfo.VetEmailAddress, ',', ' Street: ', VetAccountInfo.VetStreetAddress, ',', ' City: ', VetAccountInfo.VetCity, ',', ' State: ', VetAccountInfo.VetState, ',', ' Zip: ', VetAccountInfo.VetZip, ',', ' Specialization: ', VetAccountInfo.Specialization, ',', ' Day/Time: ', VetScheduleInfo.[{}], '\n------\n\n') from VetAccountInfo join VetScheduleInfo on VetScheduleInfo.VetID = VetAccountInfo.VetID where VetAccountInfo.Specialization = ? and VetAccountInfo.VetZip = ? and VetScheduleInfo.[{}] is not null and VetScheduleInfo.[{}] != ':::'".format(day_cb_get, day_cb_get, day_cb_get), special_cb_get, zipcode_entry_get)
            my_data = cursor.fetchall()
            my_list = [r for r, in my_data]

            #button after each vet:

            if(len(my_list) == 0):
                label = Label(displayvetsframe, text = 'No veterinarians found with those criteria.', font = "times 15")
                label.grid(row=0, column = 1)
                
            for i in range(len(my_list)):
                global j
                y = j + 10
                x = 1
                list_2 = my_list[i-1].split(',')
                while (j < y):
                    label = Label(displayvetsframe, text = list_2[x], font = "times 15")
                    label.grid(row=j, column = 1)
                    str = list_2[0]
                    x+=1
                    j=j+1
                Button(displayvetsframe, text="Schedule Appointment", width=20, height=1, font='times 5', bd=20, bg='SpringGreen4', command = lambda vet_default = str : defaultvet(vet_default)).grid(row=j-1, column=1)
                                                                                                        #parameter = str aka (vetid) : calendar function command with parameter
                #butt = Button(button_frame,text=strung, width=10, height = 1, font = 'times 10', bd=20, bg='SpringGreen4', command = lambda button_text = strung : createAppointmentPopUp(button_text))

        #the griddy configs
        entryframe.grid_columnconfigure(0, weight = 1)
        entryframe.grid_columnconfigure(3, weight = 1)

        displayvetsframe.grid_columnconfigure(0, weight = 1)
        displayvetsframe.grid_columnconfigure(3, weight = 1)
        #function for setting default vet in the user calendar vet combobox
        def defaultvet(vet_default):
            global vetsel
            global vetlist
            self.user_schedule_appointment()
            for i in range(len(vetlist)):
                vetlist2 = vetlist[i].split(",")
                if(vetlist2[0] == vet_default):
                    str = vetlist[i]
            vetsel.set(str)