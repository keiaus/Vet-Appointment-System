from tkinter import * # gui import
import tkinter as tk # gui import
from tkinter import ttk # necessary for comboboxes
import pyodbc # necessary for aws rds sql server connection

#Connection to AWS RDS SQL Server (required to run properly)
connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=Arthur;PWD=123;')
cursor = connection.cursor()

label = None
class vet():

    def __init__(self, window, account_page, vet_log_in, vet_menu, vet_update_info, vet_update_schedule, vet_update_pet):
        super().__init__()
        self.window = window
        self.account_page = account_page
        self.vet_log_in = vet_log_in
        self.vet_menu = vet_menu
        self.vet_update_info = vet_update_info
        self.vet_update_schedule = vet_update_schedule
        self.vet_update_pet = vet_update_pet
    
    def show_frame(self,frame):
        frame.tkraise()
    
    def clear_vet_frame(self):
        for widgets in self.vet_update_pet.winfo_children():
            widgets.destroy()
        self.vet_update_pet.pack_forget()
    
    def vet_menu_launch(self):
        self.window.title("Vet Menu")
        if(isinstance(label,Label)):
            label.destroy()
            self.clear_vet_frame()
            self.vet_update_pet_info()
            self.show_frame(self.vet_menu)
        else:
            self.clear_vet_frame()
            self.vet_update_pet_info()
            self.show_frame(self.vet_menu)
    
    def vet_update_schedule_clicked(self):
        self.window.title("Update Schedule")
        self.show_frame(self.vet_update_schedule)
    
    def vet_update_button_clicked(self):
        self.window.title("Update Account")
        self.show_frame(self.vet_update_info)
        
    def vet_update_pet_clicked(self):
        self.window.title("Update Pet")
        self.show_frame(self.vet_update_pet)    
            
    def vet_log_in_clicked(self):
        self.window.title("Vet Log In")
        self.show_frame(self.vet_log_in)        
            
    def return_to_main(self):
        self.window.title("Home")
        if(isinstance(label,Label)):
            label.destroy()
            self.clear_vet_frame()
            self.show_frame(self.account_page)
        else:
            self.clear_vet_frame()
            self.show_frame(self.account_page)
            
    #################################################################################################################################################

    # Veterinarian login (prompts user to enter their login info, passes info to vet_login_verify for verification)
    def vet_login(self):
        Label(self.vet_log_in, text="Please enter details below to login", font="times 50 bold", bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
        Label(self.vet_log_in, text="").pack()
    
        global vet_username_verify
        global vet_password_verify
    
        vet_username_verify = StringVar()
        vet_password_verify = StringVar()
    
        global vet_username_login_entry
        global vet_password_login_entry
    
        Label(self.vet_log_in, font="times 30", text="Username").pack()
        vet_username_login_entry = Entry(self.vet_log_in, font="times 30", textvariable=vet_username_verify)
        vet_username_login_entry.pack()
        Label(self.vet_log_in, text="").pack()
        Label(self.vet_log_in, font="times 30", text="Password").pack()
        vet_password_login_entry = Entry(self.vet_log_in, font="times 30", textvariable=vet_password_verify, show= '*')
        vet_password_login_entry.pack()
        Label(self.vet_log_in, text="").pack()
        Button(self.vet_log_in, text="Login", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = self.vet_login_verify).pack()
        Label(self.vet_log_in, text="").pack()
        Button(self.vet_log_in, text="Return to Main Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = self.return_to_main).pack()

    # Vet login verification (checks that the entered vet information matches a record in VetLoginInfo table)
    def vet_login_verify(self):
        global label
        global username2
        global password2
        username2 = vet_username_verify.get()
        password2 = vet_password_verify.get()
        vet_username_login_entry.delete(0, END)
        vet_password_login_entry.delete(0, END)
        vet_login_ID = NONE
        if(username2 == "" or password2 == ""):
            self.vet_invalid_login()
        else:
            cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?",username2, password2)
            vet_login_ID = cursor.fetchone()
            if(vet_login_ID != None):
                self.vet_menu_launch()
            else:
                self.vet_invalid_login()

    # Tells the vet that their login was invalid (whatever they entered didn't match anything in the VetLoginInfo table)
    def vet_invalid_login(self):
        global invalid_login_screen
        invalid_login_screen = Toplevel(self.window)
        invalid_login_screen.title("Alert")
        invalid_login_screen.geometry("300x150")
        Label(invalid_login_screen, text="Invalid Login ").pack()
        Button(invalid_login_screen, text="OK", command=self.delete_vet_invalid_login).pack()

    # Removes the vet_invalid_login() pop-up on click
    def delete_vet_invalid_login(self):
        invalid_login_screen.destroy()
    ######################################################################################################################################

    # Menu that appears after successful vet login
    # Provides the options to update vet account info, update schedule info, or log out
    def vet_after_login_menu(self):
        Label(self.vet_menu, text="Select Your Choice", font='times 50 bold', bg='SpringGreen4', anchor=N, pady=50).pack(fill=BOTH)
        Label(self.vet_menu,text="").pack()
        Button(self.vet_menu,text="Update Account Info", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command =lambda:self.vet_update_button_clicked()).pack()
        Label(self.vet_menu,text="").pack()
        Button(self.vet_menu,text="Update Schedule Info", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = lambda:self.vet_update_schedule_clicked()).pack()
        Label(self.vet_menu,text="").pack()
        Button(self.vet_menu, text="Update Pet Info", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = lambda:self.vet_update_pet_clicked()).pack()
        Label(self.vet_menu,text="").pack()
        Button(self.vet_menu,text="Log Out", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = self.return_to_main).pack()
    ######################################################################################################################################

    # Menu that appears when the vet clicks the update account info button
    # Takes in vet's inputs and sends it to the vet_update_account() function for processing
    def vet_update_account_menu(self):
        
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
        
        vet_first_name_label = Label(self.vet_update_info, text='First Name', font="times 15")
        vet_first_name_entry = Entry(self.vet_update_info, textvariable=vet_first_name_var, font="times 20")
        vet_first_name_label.pack()
        vet_first_name_entry.pack()

        vet_last_name_label = Label(self.vet_update_info, text='Last Name', font="times 15")
        vet_last_name_entry = Entry(self.vet_update_info, textvariable=vet_last_name_var, font="times 20")
        vet_last_name_label.pack()
        vet_last_name_entry.pack()

        vet_email_label = Label(self.vet_update_info, text='Email', font="times 15")
        vet_email_entry = Entry(self.vet_update_info, textvariable=vet_email_var, font="times 20")
        vet_email_label.pack()
        vet_email_entry.pack()

        vet_phone_number_label = Label(self.vet_update_info, text='Phone Number', font="times 15")
        vet_phone_number_entry = Entry(self.vet_update_info, textvariable=vet_phone_number_var, font="times 20")
        vet_phone_number_label.pack()
        vet_phone_number_entry.pack()

        vet_street_address_label = Label(self.vet_update_info, text='Street Address', font="times 15")
        vet_street_address_entry = Entry(self.vet_update_info, textvariable=vet_street_address_var, font="times 20")
        vet_street_address_label.pack()
        vet_street_address_entry.pack()
    

        vet_city_label = Label(self.vet_update_info, text='City', font="times 15")
        vet_city_entry = Entry(self.vet_update_info, textvariable=vet_city_var, font="times 20")
        vet_city_label.pack()
        vet_city_entry.pack()

        vet_state_label = Label(self.vet_update_info, text='State', font="times 15")
        vet_state_entry = Entry(self.vet_update_info, textvariable=vet_state_var, font="times 20")
        vet_state_label.pack(side =TOP)
        vet_state_entry.pack()

        vet_zip_label = Label(self.vet_update_info, text='Zip Code', font="times 15")
        vet_zip_entry = Entry(self.vet_update_info, textvariable=vet_zip_var, font="times 20")
        vet_zip_label.pack()
        vet_zip_entry.pack()
        
        Label(self.vet_update_info, text="").pack()
        
        Button(self.vet_update_info, text='Submit', width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = self.vet_update_account).pack()
        Label(self.vet_update_info, text="").pack() 
        Button(self.vet_update_info, text="Return to Vet Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = self.vet_menu_launch).pack()

    # Takes inputs from vet_update_account_menu() and finds vet's LoginID from the VetLoginInfo table
    # to update the correct records in the VetAccountInfo table
    def vet_update_account(self):
        global label
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
        Label(self.vet_update_info, text="").pack()
        label = Label(self.vet_update_info, text="Update Successful", fg="green", font="times 15")
        label.pack()

    ##################################################################################################################################################

    # Menu that appears when the vet clicks the update schedule button
    # Takes in vet's inputs for processing in vet_update_schedule_info()
    def vet_update_schedule_menu(self):
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


        monday_label = Label(self.vet_update_schedule, text='Monday', font="times 15")
        monday_entry = Entry(self.vet_update_schedule, textvariable=monday, font="times 20")
        monday_label.pack()
        monday_entry.pack()

        tuesday_label = Label(self.vet_update_schedule, text='Tuesday', font="times 15")
        tuesday_entry = Entry(self.vet_update_schedule, textvariable=tuesday, font="times 20")
        tuesday_label.pack()
        tuesday_entry.pack()

        wednesday_label = Label(self.vet_update_schedule, text='Wednesday', font="times 15")
        wednesday_entry = Entry(self.vet_update_schedule, textvariable=wednesday, font="times 20")
        wednesday_label.pack()
        wednesday_entry.pack()

        thursday_label = Label(self.vet_update_schedule, text='Thursday', font="times 15")
        thursday_entry = Entry(self.vet_update_schedule, textvariable=thursday, font="times 20")
        thursday_label.pack()
        thursday_entry.pack()

        friday_label = Label(self.vet_update_schedule, text='Friday', font="times 15")
        friday_entry = Entry(self.vet_update_schedule, textvariable=friday, font="times 20")
        friday_label.pack()
        friday_entry.pack()

        saturday_label = Label(self.vet_update_schedule, text='Saturday', font="times 15")
        saturday_entry = Entry(self.vet_update_schedule, textvariable=saturday, font="times 20")
        saturday_label.pack()
        saturday_entry.pack()

        sunday_label = Label(self.vet_update_schedule, text='Sunday', font="times 15")
        sunday_entry = Entry(self.vet_update_schedule, textvariable=sunday, font="times 20")
        sunday_label.pack()
        sunday_entry.pack()    
        
        Label(self.vet_update_schedule, text="").pack()

        Button(self.vet_update_schedule, text='Submit', width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = self.vet_update_schedule_info).pack()
        Label(self.vet_update_schedule, text="").pack()
        Button(self.vet_update_schedule, text="Return to Vet Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = self.vet_menu_launch).pack()

    # Takes inputs from vet_update_schedule_menu() and finds vet's LoginID from the VetLoginInfo table
    # to update the correct records in the VetScheduleInfo table
    def vet_update_schedule_info(self):
        global label
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
        cursor.execute("UPDATE VetScheduleInfo SET Monday=?, Tuesday=?, Wednesday=?, Thursday=?, Friday=?, Saturday=?, Sunday=? WHERE VetID = ?", monday, tuesday, wednesday, thursday, friday, saturday, sunday, vet_id[0])
        cursor.commit()
        monday_entry.delete(0,END)
        tuesday_entry.delete(0,END)
        wednesday_entry.delete(0,END)
        thursday_entry.delete(0,END)
        friday_entry.delete(0,END)
        saturday_entry.delete(0,END)
        sunday_entry.delete(0,END)
        Label(self.vet_update_schedule, text="").pack()
        label = Label(self.vet_update_schedule, text="Update Successful", fg="green", font="times 15")
        label.pack()

    #Allows vets to select a user and update specific pet information
    def vet_update_pet_info(self):
        global pet_name_var
        pet_name_var= StringVar()
        global pet_type_var
        pet_type_var = StringVar()
        global pet_breed_var
        pet_breed_var = StringVar()
        global pet_color_var
        pet_color_var = StringVar()
        global pet_name_entry2
        global pet_type_entry2
        global pet_breed_entry2
        global pet_color_entry2
        global cb1
        global cb2
        global sel
        
        Label(self.vet_update_pet, text = "").pack()
        vet_update_pet_menu_label = Label(self.vet_update_pet, text = "Veterinarian Update Pet Menu", font = "times 15")
        vet_update_pet_menu_label.pack()

        query= "SELECT Concat(UserID, ', ', UserFirstName, ', ', UserLastName) FROM USERACCOUNTINFO"
                    
        my_data = cursor.execute(query) # SQLAlchem engine result
        my_list = [r for r, in my_data] # create a  list 
        my_list2=[] 
        
        sel=tk.StringVar()

        cb1 = ttk.Combobox(self.vet_update_pet, values=my_list,width=15,textvariable = sel)
        cb1.pack(padx=30,pady=30)

        sel.trace('w', self.my_upd)

        cb2 = ttk.Combobox(self.vet_update_pet, values=my_list2, width=15,)
        cb2.pack()
        
        
        pet_name_label = Label(self.vet_update_pet, text='Pet Name', font="times 15")
        pet_name_entry2 = Entry(self.vet_update_pet, font="times 20", width=20, textvariable=pet_name_var)
        pet_name_label.pack()
        pet_name_entry2.pack()

        pet_type_label = Label(self.vet_update_pet, text='Pet Type', font="times 15")
        pet_type_entry2 = Entry(self.vet_update_pet, textvariable=pet_type_var, font="times 20", width=20)
        pet_type_label.pack()
        pet_type_entry2.pack()

        pet_breed_label = Label(self.vet_update_pet, text='Pet Breed', font="times 15")
        pet_breed_entry2 = Entry(self.vet_update_pet, textvariable=pet_breed_var, font="times 20")
        pet_breed_label.pack()
        pet_breed_entry2.pack()

        pet_color_label = Label(self.vet_update_pet, text='Pet Color', font="times 15")
        pet_color_entry2 = Entry(self.vet_update_pet, textvariable=pet_color_var, font="times 20")
        pet_color_label.pack()
        pet_color_entry2.pack()

        Label(self.vet_update_pet, text="").pack()
        
        Button(self.vet_update_pet, text='Update Pet', width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = self.vet_pet_confirmation_popup).pack()
        Label(self.vet_update_pet, text="").pack()
        Button(self.vet_update_pet, text="Return to Vet Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = self.vet_menu_launch).pack()
        
    def my_upd(*args):
        cb2.set('') # remove the previous selected option
        selection = sel.get().split(", ")
        query = "SELECT Concat(PetID, ', ', PetName) FROM PetInfo WHERE UserID = '"+selection[0]+"'"
        my_data = cursor.execute(query) # SQLAlchem engine result
        my_list2 = [r for r, in my_data] # create a  list
        cb2['values']=my_list2    
            
    def vetUpdatePet(self,*args):        
        selection2 = cb2.get().split(", ")
        global label
        pet_name_var = pet_name_entry2.get()
        pet_type_var = pet_type_entry2.get()
        pet_breed_var = pet_breed_entry2.get()
        pet_color_var = pet_color_entry2.get()
        cursor.execute("UPDATE PetInfo SET PetName = ?, PetType = ?, PetBreed = ?, PetColor = ? WHERE PetID = ?", pet_name_var, pet_type_var, pet_breed_var, pet_color_var, selection2[0])
        cursor.commit()
        pet_name_entry2.delete(0,END)
        pet_type_entry2.delete(0,END)
        pet_breed_entry2.delete(0,END)
        pet_color_entry2.delete(0,END)
        self.vet_pet_confirmation_des()
        cb1.set('')
        label = Label(self.vet_update_pet, text="Update Successful", fg="green", font="times 20")
        label.pack()
        
    def vet_pet_confirmation_popup(self):
        global vet_pet_confirmation
        vet_pet_confirmation = Toplevel(self.window)
        vet_pet_confirmation.title("Alert")
        vet_pet_confirmation.geometry("300x150")
        Label(vet_pet_confirmation, text=f'You selected {cb2.get()}.').pack()
        Button(vet_pet_confirmation, text="Update", command=self.vetUpdatePet).pack()
        Button(vet_pet_confirmation, text="No", command=self.vet_pet_confirmation_des).pack()    
    
    def vet_pet_confirmation_des(self):
        vet_pet_confirmation.destroy()
            
        
    ###########################################################################################################################################################################
        