from tkinter import * # gui import
import tkinter as tk # gui import
from tkinter import ttk # necessary for comboboxes
import pyodbc # necessary for aws rds sql server connection

#Connection to AWS RDS SQL Server (required to run properly)
connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=Arthur;PWD=123;')
cursor = connection.cursor()

label = None
class user():
    
    def __init__(self, window, account_page, account_create, user_log_in, user_pet_menu, user_pet_add,  user_menu, user_update_info, user_update_pet_info, user_update_pet_dropdown):
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

    def show_frame(self,frame):
        frame.tkraise()

    def user_update_button_clicked(self):
        self.window.title("Update Account")
        self.show_frame(self.user_update_info)

    def user_pet_add_clicked(self):
        self.window.title("Add a Pet(s)")
        if (isinstance(label, Label)):
            label.destroy()
            self.show_frame(self.user_pet_add)
        else:
            self.show_frame(self.user_pet_add)

    def user_menu_launch(self):
        self.window.title("User Menu")
        if(isinstance(label,Label)):
            label.destroy()
            self.clear_user_frame()
            self.user_update_pet_menu()
            self.show_frame(self.user_menu)
        else:
            self.clear_user_frame()
            self.user_update_pet_menu()
            self.show_frame(self.user_menu)

    # Opens the update pet menu on click (for users)
    def user_update_pet_button_clicked(self):
        self.window.title("Update Pet Information")
        self.show_frame(self.user_update_pet_info)
    
    def clear_user_frame(self):
        for widgets in self.user_update_pet_info.winfo_children():
            widgets.destroy()
        self.user_update_pet_info.pack_forget()

    def return_to_main(self):
        self.window.title("Home")
        if(isinstance(label,Label)):
            label.destroy()
            self.clear_user_frame()
            self.show_frame(self.account_page)
        else:
            self.clear_user_frame()
            self.show_frame(self.account_page)
    
    def user_register(self):
        global username
        global password
        global username_entry
        global password_entry 
        username = StringVar()
        password = StringVar()

        Label(self.account_create, text="Please enter details below", font='times 50 bold', bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
        Label(self.account_create, text="").pack()
        username_lable = Label(self.account_create, font='times 30', text="Username")
        username_lable.pack()
        username_entry = Entry(self.account_create, font='times 30', textvariable=username)
        username_entry.pack()
        password_lable = Label(self.account_create, font='times 30', text="Password")
        password_lable.pack()
        password_entry = Entry(self.account_create, font='times 30', textvariable=password, show='*')
        password_entry.pack()
        Label(self.account_create, text="").pack()
        Button(self.account_create, text="Register", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = self.register_user).pack()
        Label(self.account_create, text="").pack()
        Button(self.account_create, text="Return to Main Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = self.return_to_main).pack()

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

                label = Label(self.account_create, text="Registration Successful", fg="green", font="times 20")
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

        Label(self.user_log_in, font="times 30", text="Username").pack()
        username_login_entry = Entry(self.user_log_in, font="times 30", textvariable=username_verify)
        username_login_entry.pack()
        Label(self.user_log_in, text="").pack()
        Label(self.user_log_in, font="times 30", text="Password").pack()
        password_login_entry = Entry(self.user_log_in, font="times 30", textvariable=password_verify, show= '*')
        password_login_entry.pack()
        Label(self.user_log_in, text="").pack()
        Button(self.user_log_in, text="Login", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = self.user_login_verify).pack()
        Label(self.user_log_in, text="").pack()
        Button(self.user_log_in, text="Return to Main Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = self.return_to_main).pack()

        #user_id1 = NONE
        # User login verification (checks that the entered user information matches a record in the UserLoginInfo table)
        counter = 0
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

        #username_login_entry.delete(0, END)
        #password_login_entry.delete(0, END)

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

        Label(self.user_update_info, text="").pack()

        first_name_label = Label(self.user_update_info, text='First Name', font="times 15")
        first_name_entry = Entry(self.user_update_info, font="times 20", width=20, textvariable=first_name_var)
        first_name_label.pack()
        first_name_entry.pack()

        last_name_label = Label(self.user_update_info, text='Last Name', font="times 15")
        last_name_entry = Entry(self.user_update_info, textvariable=last_name_var, font="times 20", width=20)
        last_name_label.pack()
        last_name_entry.pack()

        email_label = Label(self.user_update_info, text='Email', font="times 15")
        email_entry = Entry(self.user_update_info, textvariable=email_var, font="times 20")
        email_label.pack()
        email_entry.pack()

        phone_number_label = Label(self.user_update_info, text='Phone Number', font="times 15")
        phone_number_entry = Entry(self.user_update_info, textvariable=phone_number_var, font="times 20")
        phone_number_label.pack()
        phone_number_entry.pack()

        street_address_label = Label(self.user_update_info, text='Street Address', font="times 15")
        street_address_entry = Entry(self.user_update_info, textvariable=street_address_var, font="times 20")
        street_address_label.pack()
        street_address_entry.pack()

        city_label = Label(self.user_update_info, text='City', font="times 15")
        city_entry = Entry(self.user_update_info, textvariable=city_var, font="times 20")
        city_label.pack()
        city_entry.pack()

        state_label = Label(self.user_update_info, text='State', font="times 15")
        state_entry = Entry(self.user_update_info, textvariable=state_var, font="times 20")
        state_label.pack(side =TOP)
        state_entry.pack()

        zip_label = Label(self.user_update_info, text='Zip Code', font="times 15")
        zip_entry = Entry(self.user_update_info, textvariable=zip_var, font="times 20")
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
        Label(self.user_update_pet_info, text="Select a Pet", font="times 20 bold").pack()
        pet_info_combobox = ttk.Combobox(self.user_update_pet_info, textvariable = pet_info_selection, values = pet_info_list)
        pet_info_combobox.pack(pady = 20)
        pet_info_display = Label(self.user_update_pet_info, text = "Pet Info:", bg = "SpringGreen4")
        pet_info_display.pack()
        pet_info_selection.trace("w", self.pet_selection_display)

        pet_name_label = Label(self.user_update_pet_info, text='Pet Name', font="times 15")
        pet_name_entry1 = Entry(self.user_update_pet_info, font="times 20", width=20, textvariable=pet_name_var)
        pet_name_label.pack()
        pet_name_entry1.pack()

        pet_type_label = Label(self.user_update_pet_info, text='Pet Type', font="times 15")
        pet_type_entry1 = Entry(self.user_update_pet_info, textvariable=pet_type_var, font="times 20", width=20)
        pet_type_label.pack()
        pet_type_entry1.pack()

        pet_breed_label = Label(self.user_update_pet_info, text='Pet Breed', font="times 15")
        pet_breed_entry1 = Entry(self.user_update_pet_info, textvariable=pet_breed_var, font="times 20")
        pet_breed_label.pack()
        pet_breed_entry1.pack()

        pet_color_label = Label(self.user_update_pet_info, text='Pet Color', font="times 15")
        pet_color_entry1 = Entry(self.user_update_pet_info, textvariable=pet_color_var, font="times 20")
        pet_color_label.pack()
        pet_color_entry1.pack()

        Label(self.user_update_pet_info, text="").pack()

        Button(self.user_update_pet_info, text='Update Pet', width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = self.pet_confirmation_popup).pack()
        Label(self.user_update_pet_info, text="").pack()
        Button(self.user_update_pet_info, text="Return to User Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = self.user_menu_launch).pack()
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

        label = Label(self.user_update_info, text="Update Successful", fg="green", font="times 20")
        label.pack()


        ##################################################################################################################################################

        # Menu that appears after successful user login
        # Provides the options to update account info or log out
    def user_after_login_menu(self):
        Label(self.user_menu, text="Select Your Choice", font='times 50 bold', bg='SpringGreen4', anchor=N, pady=50).pack(fill=BOTH)
        Label(self.user_menu, text="").pack()
        Button(self.user_menu, text="Update Account Info", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command =lambda:self.user_update_button_clicked()).pack()
        Label(self.user_menu, text="").pack()
        Button(self.user_menu, text="Add New Pet", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command =lambda:self.user_pet_add_clicked()).pack()
        Label(self.user_menu, text="").pack()
        Button(self.user_menu, text="Update Pet Info", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command =lambda:self.user_update_pet_button_clicked()).pack()
        Label(self.user_menu, text="").pack()
        Button(self.user_menu, text="Log Out", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = self.return_to_main).pack()

        ######################################################################################################################################


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
        pet_name_entry = Entry(self.user_pet_add, font="times 20", width=20, textvariable=pet_name_var)
        pet_name_label.pack()
        pet_name_entry.pack()

        pet_type_label = Label(self.user_pet_add, text='Pet Type', font="times 15")
        pet_type_entry = Entry(self.user_pet_add, textvariable=pet_type_var, font="times 20", width=20)
        pet_type_label.pack()
        pet_type_entry.pack()

        pet_breed_label = Label(self.user_pet_add, text='Pet Breed', font="times 15")
        pet_breed_entry = Entry(self.user_pet_add, textvariable=pet_breed_var, font="times 20")
        pet_breed_label.pack()
        pet_breed_entry.pack()

        pet_color_label = Label(self.user_pet_add, text='Pet Color', font="times 15")
        pet_color_entry = Entry(self.user_pet_add, textvariable=pet_color_var, font="times 20")
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


        ################################################################################################################################################   


