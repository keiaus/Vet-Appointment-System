from tkinter import * # gui import
import tkinter as tk # gui import
from tkinter import ttk # necessary for comboboxes
import pyodbc # necessary for aws rds sql server connection
from datetime import datetime
from datetime import date
#Connection to AWS RDS SQL Server (required to run properly)
connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=Arthur;PWD=123;')
cursor = connection.cursor()

label = None
class vet():

    #necessary to display each main frame (sub frames are handled in their relevant functions)
    def __init__(self, window, account_page, vet_log_in, vet_menu, vet_update_info, vet_update_schedule, vet_update_pet, vet_daily_appointment, vet_canceled_appointment, vet_upload_pet_rec):
        super().__init__()
        self.window = window
        self.account_page = account_page
        self.vet_log_in = vet_log_in
        self.vet_menu = vet_menu
        self.vet_update_info = vet_update_info
        self.vet_update_schedule = vet_update_schedule
        self.vet_update_pet = vet_update_pet
        self.vet_daily_appointment = vet_daily_appointment
        self.vet_canceled_appointment = vet_canceled_appointment
        self.vet_upload_pet_rec = vet_upload_pet_rec
    
    def show_frame(self,frame):
        frame.tkraise()
    
    #clears all of the vet frames when exiting them to prevent overlapping
    def clear_vet_frame(self):
        for widgets in self.vet_log_in.winfo_children():
            widgets.destroy()
        self.vet_log_in.pack_forget()
        
        for widgets in self.vet_update_info.winfo_children():
            widgets.destroy()
        self.vet_update_info.pack_forget()
        
        for widgets in self.vet_update_schedule.winfo_children():
            widgets.destroy()
        self.vet_update_schedule.pack_forget()
        
        for widgets in self.vet_update_pet.winfo_children():
            widgets.destroy()
        self.vet_update_pet.pack_forget()
        
        for widgets in self.vet_daily_appointment.winfo_children():
            widgets.destroy()
        self.vet_daily_appointment.pack_forget()
        
        for widgets in self.vet_canceled_appointment.winfo_children():
            widgets.destroy()
        self.vet_canceled_appointment.pack_forget()
        
        for widgets in self.vet_upload_pet_rec.winfo_children():
            widgets.destroy()
        self.vet_upload_pet_rec.pack_forget()
        
    #launches the main vet menu on click from the main menu
    def vet_menu_launch(self):
        self.window.title("Vet Menu")
        if(isinstance(label,Label)):
            label.destroy()
            self.clear_vet_frame()
            self.show_frame(self.vet_menu)
        else:
            self.clear_vet_frame()
            self.show_frame(self.vet_menu)
    
    #goes to the login menu for the vets on click from the main menu
    def vet_log_in_clicked(self):
        self.window.title("Vet Log In")
        self.vet_login()
        self.show_frame(self.vet_log_in) 
    
    #goes to the update account menu on click from the vet menu
    def vet_update_button_clicked(self):
        self.window.title("Update Account")
        self.vet_update_account_menu()
        self.show_frame(self.vet_update_info)
    
    #goes to the update schedule menu on click from the vet menu
    def vet_update_schedule_clicked(self):
        self.window.title("Update Schedule")
        self.vet_update_schedule_menu()
        self.show_frame(self.vet_update_schedule)
    
    #goes to the update pet menu on click from the vet menu
    def vet_update_pet_clicked(self):
        self.window.title("Update Pet")
        self.vet_update_pet_info()
        self.show_frame(self.vet_update_pet)    
    
    #goes to the daily appointments menu on click from the vet menu
    def vet_daily_appointment_clicked(self):
        for widgets in self.vet_daily_appointment.winfo_children():
            widgets.destroy()
        self.vet_daily_appointment.pack_forget()
        self.window.title("Today's Appointments")
        self.vet_daily_app()
        self.show_frame(self.vet_daily_appointment)    

    #goes to the canceled appointments menu on click from the vet menu
    def vet_canceled_appointment_clicked(self):
        self.window.title("Canceled Appointments")
        self.vet_canceled_app()
        self.show_frame(self.vet_canceled_appointment)
        
    # goes to vet upload record frame when clicked   
    def vet_upload_pet_record_clicked(self, pet_default):
        for widgets in self.vet_upload_pet_rec.winfo_children():
            widgets.destroy()
        self.vet_upload_pet_rec.pack_forget()
        self.window.title("Upload Pet Record")
        self.upload_pet_rec(pet_default)
        self.show_frame(self.vet_upload_pet_rec)   
    
    #returns to the main menu and clears the vet frame on click
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
    
        #entry boxes and related labels (username and password)
        Label(self.vet_log_in, font="times 20", text="Username").pack()
        vet_username_login_entry = Entry(self.vet_log_in, font="times 20", textvariable=vet_username_verify)
        vet_username_login_entry.pack()
        Label(self.vet_log_in, text="").pack()
        Label(self.vet_log_in, font="times 20", text="Password").pack()
        vet_password_login_entry = Entry(self.vet_log_in, font="times 20", textvariable=vet_password_verify, show= '*')
        vet_password_login_entry.pack()

        #buttons
        Label(self.vet_log_in, text="").pack()
        Button(self.vet_log_in, text="Login", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = self.vet_login_verify).pack()
        Label(self.vet_log_in, text="").pack()
        Button(self.vet_log_in, text="Return to Main Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = self.return_to_main).pack()

    # Vet login verification (checks that the entered vet information matches a record in VetLoginInfo table)
    def vet_login_verify(self):
        global label
        global username2
        global password2
        username2 = vet_username_verify.get()
        password2 = vet_password_verify.get()
        vet_login_ID = NONE

        #if there's nothing entered or there's no matches, it's an invalid login. otherwise it proceeds to the vet menu
        if(username2 == "" or password2 == ""):
            self.vet_invalid_login()
        else:
            cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?",username2, password2)
            vet_login_ID = cursor.fetchone()
            if(vet_login_ID != None):
                self.vet_menu_launch()
            else:
                self.vet_invalid_login()

    #gets the vet's account id from the database
    def getVetID(self):
        vet_login_ID = vet.getVetLoginID(self)
        cursor.execute("select VetID from VetAccountInfo where VetLoginID = ?", vet_login_ID)
        vet_id1 = cursor.fetchone()

        return vet_id1

    #gets the vet's login id from the database
    def getVetLoginID(self):
        username1 = vet_username_verify.get()
        password1 = vet_password_verify.get()

        cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?", username1, password1)
        vet_login_ID = cursor.fetchone()

        return vet_login_ID

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
        selectlabel = Label(self.vet_menu, text="Select Your Choice", font='times 50 bold', bg='SpringGreen4', anchor=N, pady=50)
        selectlabel.pack(fill = "both")

        vetmenuframe = Frame(self.vet_menu)
        vetmenuframe.pack()
        
        #buttons
        upacc = Button(vetmenuframe,text="Update Account Info", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command =lambda:self.vet_update_button_clicked())
        upsch = Button(vetmenuframe,text="Update Schedule Info", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = lambda:self.vet_update_schedule_clicked())
        uppet = Button(vetmenuframe, text="Update Pet Info", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = lambda:self.vet_update_pet_clicked())
        apptstoday = Button(vetmenuframe, text="View Today's Appointments", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = lambda:self.vet_daily_appointment_clicked())
        apptscand = Button(vetmenuframe, text = "Canceled Appointments", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = lambda:self.vet_canceled_appointment_clicked())
        logout = Button(vetmenuframe,text="Log Out", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = self.return_to_main)

        #the griddy
        Label(vetmenuframe, text = " ", font = "times 15").grid(row = 1, column = 2)
        upacc.grid(row = 2, column = 1)
        Label(vetmenuframe, text = " ", font = "times 15").grid(row = 3, column = 2)
        upsch.grid(row = 4, column = 1)
        Label(vetmenuframe, text = " ", font = "times 15").grid(row = 5, column = 2)
        uppet.grid(row = 6, column = 2)
        Label(vetmenuframe, text = " ", font = "times 15").grid(row = 1, column = 2)
        apptstoday.grid(row = 2, column = 3)
        Label(vetmenuframe, text = " ", font = "times 15").grid(row = 3, column = 2)
        apptscand.grid(row = 4, column = 3)
        Label(vetmenuframe, text = " ", font = "times 15").grid(row = 7, column = 2)
        logout.grid(row = 8, column = 2)
        
        #the griddy configs
        vetmenuframe.grid_columnconfigure(0, weight = 1)
        vetmenuframe.grid_columnconfigure(4, weight = 1)
    ######################################################################################################################################

    # Menu that appears when the vet clicks the update account info button
    # Takes in vet's inputs and sends it to the vet_update_account() function for processing
    def vet_update_account_menu(self):
        #variables
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
        global vet_spec_var
        vet_spec_var = StringVar()
        global vet_first_name_entry
        global vet_last_name_entry
        global vet_email_entry
        global vet_phone_number_entry
        global vet_street_address_entry
        global vet_city_entry
        global vet_state_entry
        global vet_zip_entry
        
        #selects a vet and their information based on their id associated with their login credentials
        temp_vet_id = vet.getVetID(self)          
        my_data = cursor.execute("SELECT Concat(VetFirstName, ', ', VetLastName, ', ', VetEmailAddress, ', ', VetPhoneNumber, ', ', VetStreetAddress, ', ', VetCity, ', ', VetState, ', ', VetZip, ', ', Specialization) FROM VetACCOUNTINFO WHERE VetID = ?", temp_vet_id)
        my_list = [r for r, in my_data]
        sel = my_list[0].split(", ")
        
        #label at the top
        vet_frame_label = Label(self.vet_update_info, text='Enter your Information', font="times 20")
        vet_frame_label.pack()
        
        #Entry box for entering a first name
        vet_first_name_label = Label(self.vet_update_info, text='First Name', font="times 15")
        vet_first_name_entry = Entry(self.vet_update_info, textvariable=vet_first_name_var, font="times 15")
        vet_first_name_entry.insert(0, sel[0])
        vet_first_name_label.pack()
        vet_first_name_entry.pack()

        #Entry box for entering a last name
        vet_last_name_label = Label(self.vet_update_info, text='Last Name', font="times 15")
        vet_last_name_entry = Entry(self.vet_update_info, textvariable=vet_last_name_var, font="times 15")
        vet_last_name_entry.insert(0, sel[1])
        vet_last_name_label.pack()
        vet_last_name_entry.pack()

        #Entry box for entering an email address
        vet_email_label = Label(self.vet_update_info, text='Email', font="times 15")
        vet_email_entry = Entry(self.vet_update_info, textvariable=vet_email_var, font="times 15")
        vet_email_entry.insert(0, sel[2])
        vet_email_label.pack()
        vet_email_entry.pack()

        #Entry box for entering a phone number
        vet_phone_number_label = Label(self.vet_update_info, text='Phone Number', font="times 15")
        vet_phone_number_entry = Entry(self.vet_update_info, textvariable=vet_phone_number_var, font="times 15")
        vet_phone_number_entry.insert(0, sel[3])
        vet_phone_number_label.pack()
        vet_phone_number_entry.pack()

        #Entry box for entering a street address
        vet_street_address_label = Label(self.vet_update_info, text='Street Address', font="times 15")
        vet_street_address_entry = Entry(self.vet_update_info, textvariable=vet_street_address_var, font="times 15")
        vet_street_address_entry.insert(0, sel[4])
        vet_street_address_label.pack()
        vet_street_address_entry.pack()
    
        #Entry box for entering a city
        vet_city_label = Label(self.vet_update_info, text='City', font="times 15")
        vet_city_entry = Entry(self.vet_update_info, textvariable=vet_city_var, font="times 15")
        vet_city_entry.insert(0, sel[5])
        vet_city_label.pack()
        vet_city_entry.pack()

        #Entry box or entering a state
        vet_state_label = Label(self.vet_update_info, text='State', font="times 15")
        vet_state_entry = Entry(self.vet_update_info, textvariable=vet_state_var, font="times 15")
        vet_state_entry.insert(0, sel[6])
        vet_state_label.pack()
        vet_state_entry.pack()

        #Entry box for entering a zip code
        vet_zip_label = Label(self.vet_update_info, text='Zip Code', font="times 15")
        vet_zip_entry = Entry(self.vet_update_info, textvariable=vet_zip_var, font="times 15")
        vet_zip_entry.insert(0, sel[7])
        vet_zip_label.pack()
        vet_zip_entry.pack()

        #Combobox (and label) for selecting a specialization
        vet_spec_label = Label(self.vet_update_info, text='Specialization', font="times 15")
        vet_spec_label.pack()
        
        vet_spec_cb = ttk.Combobox(self.vet_update_info, textvariable = vet_spec_var, font="times 15")
        vet_spec_cb.set(sel[8])
        vet_spec_cb['values'] = ('Check Ups', 'Surgery', 'Dentistry', 'Other')
        vet_spec_cb.pack()
        
        Label(self.vet_update_info, text="").pack()
        
        #buttons
        Button(self.vet_update_info, text='Submit', width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = self.vet_update_account).pack()
        Label(self.vet_update_info, text="").pack() 
        Button(self.vet_update_info, text="Return to Vet Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = self.vet_menu_launch).pack()

    # Takes inputs from vet_update_account_menu() and finds vet's LoginID from the VetLoginInfo table
    # to update the correct records in the VetAccountInfo table
    def vet_update_account(self):
        global label
        #grabs all of the entries from the previous function for use in the sql statements
        vet_first_name_var = vet_first_name_entry.get()
        vet_last_name_var = vet_last_name_entry.get()
        vet_email_var = vet_email_entry.get()
        vet_phone_number_var = vet_phone_number_entry.get()
        vet_street_address_var = vet_street_address_entry.get()
        vet_city_var = vet_city_entry.get()
        vet_state_var = vet_state_entry.get()
        vet_zip_var = vet_zip_entry.get()
        vet_spec = vet_spec_var.get()

        #the sql statements verifying the vet and then updating their info based on inputs
        cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?", username2, password2)
        vet_login_ID = cursor.fetchone()
        cursor.execute("SELECT VetID FROM VetAccountInfo INNER JOIN VetLoginInfo ON VetAccountInfo.VetLoginID = VetLoginInfo.VetLoginID WHERE VetAccountInfo.VetLoginID = ?", vet_login_ID)
        vet_id = cursor.fetchone()
        cursor.execute("UPDATE VetAccountInfo SET VetFirstName = ?, VetLastName = ?, VetPhoneNumber = ?, VetEmailAddress = ?, VetStreetAddress = ?, VetCity = ?, VetState = ?, VetZip = ?, Specialization = ? WHERE VetID = ?", vet_first_name_var, vet_last_name_var, vet_phone_number_var, vet_email_var, vet_street_address_var, vet_city_var, vet_state_var, vet_zip_var, vet_spec ,vet_id[0])
        cursor.commit()

        #clears all of the entry boxes
        vet_first_name_entry.delete(0,END)
        vet_last_name_entry.delete(0,END)
        vet_phone_number_entry.delete(0,END)
        vet_email_entry.delete(0,END)
        vet_street_address_entry.delete(0,END)
        vet_city_entry.delete(0,END)
        vet_state_entry.delete(0,END)
        vet_zip_entry.delete(0,END)

        #tells the vet that their information was successfully updated
        Label(self.vet_update_info, text="").pack()
        label = Label(self.vet_update_info, text="Update Successful", fg="green", font="times 15")
        label.pack()

    ##################################################################################################################################################

    # Menu that appears when the vet clicks the update schedule button
    # Takes in vet's inputs for processing in vet_update_schedule_info()
    def vet_update_schedule_menu(self):
        #READ ME - Instructions for using pack() and grid() simultaneously for box organization:
        #Every single day needs its own frame for its corresponding entry/combo boxes and labels. This is **ABSOLUTELY** necessary for organizational purposes
        #Every single title label, e.g., "Monday", must be managed using pack() - this is to stack each title label vertically corresponding to the rows
        #Every single dashlabel, e.g., dashlabel1, must be managed using grid() - this is to keep each dash perfectly centered between the boxes
        #Every single frame, e.g., "entries_monday", must be managed using pack() - this is is to stack each frame vertically, as we've always done
        #Every single frame, e.g., "entries_monday", must be configured using .grid_columnconfigure([0 or 6], weight = 1) 
            # - the 0 or 6 changes depending on the amount of columns you want in that frame, the weight must equal 1 every time 
            # - the first columnconfigure always has 0 as the first parameter, and the second columnconfigure always has 6 (or whatever is decided) as the second parameter
            # - this is the only way (so far) that we've managed to use pack() and grid() simultaneously, so don't mess it up
        #Every single entry/combo box and corresponding dashlabel, e.g., "em1" and "dashlabel1", must be managed using grid() 
            # - this is to organize each box into its own row and column
            # - rows should stay the same per day, but columns change based on placement, e.g., em1, em2, emcb1, emcb2, and dashlabel1: 
                # em1.grid(row = 0, column = 1) emcb1.grid(row = 0, column = 2) dashlabel1.grid(row = 0, column = 3) em2.grid(row = 0, column = 4) emcb2.grid(row = 0, column = 5)
                # rows are n-1 (monday is row 0, tuesday is row 1, etc), columns are n (left-side entry is column 1, dashlabel is column 2, etc)
                # the order in which boxes and labels are managed matters, don't mess it up
        #In total, there should be 14 entry boxes, 7 dashlabels, 14 combo boxes, 14 textvariables, 7 frames, and 7 labels (excluding the submit button, return button, etc)
        #There are comments explaining each part of the Monday section more closely, please follow these instructions and the Monday examples for further help on other days
        #The order in which labels, boxes, and frames are managed matters, don't mess it up

        #Entry box textvariables (vusm stands for "vet_update_schedule_menu", so as to not confuse with the old vet_update_schedule_info variables)
        global monday_entry1_vusm
        monday_entry1_vusm = StringVar()
        global monday_entry2_vusm
        monday_entry2_vusm = StringVar()
        global tuesday_entry1_vusm
        tuesday_entry1_vusm = StringVar()
        global tuesday_entry2_vusm
        tuesday_entry2_vusm = StringVar()
        global wednesday_entry1_vusm
        wednesday_entry1_vusm = StringVar()
        global wednesday_entry2_vusm
        wednesday_entry2_vusm = StringVar()
        global thursday_entry1_vusm
        thursday_entry1_vusm = StringVar()
        global thursday_entry2_vusm
        thursday_entry2_vusm = StringVar()
        global friday_entry1_vusm
        friday_entry1_vusm = StringVar()
        global friday_entry2_vusm
        friday_entry2_vusm = StringVar()
        global saturday_entry1_vusm
        saturday_entry1_vusm = StringVar()
        global saturday_entry2_vusm
        saturday_entry2_vusm = StringVar()
        global sunday_entry1_vusm
        sunday_entry1_vusm = StringVar()
        global sunday_entry2_vusm
        sunday_entry2_vusm = StringVar()

        #Entry boxes for each day (2 per day for start/end)
        global em1
        global em2
        global et1
        global et2
        global ew1
        global ew2
        global er1
        global er2
        global ef1
        global ef2
        global esa1
        global esa2
        global esu1
        global esu2

        #Combo boxes for each day (2 per day for am/pm start/end)
        global emcb1
        global emcb2
        global etcb1
        global etcb2
        global ewcb1
        global ewcb2
        global ercb1
        global ercb2
        global efcb1
        global efcb2
        global esucb1
        global esucb2
        global esacb1
        global esacb2

        #Am/pm entries for combo boxes (2 per day, 1 for each combo box)
        global ampm1_emcb1
        ampm1_emcb1 = tk.StringVar()
        global ampm2_emcb2
        ampm2_emcb2 = tk.StringVar()
        global ampm1_etcb1
        ampm1_etcb1 = tk.StringVar()
        global ampm2_etcb2
        ampm2_etcb2 = tk.StringVar()
        global ampm1_ewcb1
        ampm1_ewcb1 = tk.StringVar()
        global ampm2_ewcb2
        ampm2_ewcb2 = tk.StringVar()
        global ampm1_ercb1
        ampm1_ercb1 = tk.StringVar()
        global ampm2_ercb2
        ampm2_ercb2 = tk.StringVar()
        global ampm1_efcb1
        ampm1_efcb1 = tk.StringVar()
        global ampm2_efcb2
        ampm2_efcb2 = tk.StringVar()
        global ampm1_esacb1
        ampm1_esacb1 = tk.StringVar()
        global ampm2_esacb2
        ampm2_esacb2 = tk.StringVar()
        global ampm1_esucb1
        ampm1_esucb1 = tk.StringVar()
        global ampm2_esucb2
        ampm2_esucb2 = tk.StringVar()

        #Monday
        label_monday = tk.Label(self.vet_update_schedule, text = "Monday", font = "times 10") #Monday label
        entries_monday = tk.Frame(self.vet_update_schedule) #Monday frame
        label_monday.pack(side = "top", fill = "both", expand = False) #Monday label pack (makes it centered at the top)
        entries_monday.pack(side = "top", fill = "x") #Monday frame pack (makes it centered at the top)

        em1 = tk.Entry(entries_monday, textvariable = monday_entry1_vusm) #Left-side entry box (start time)
        em2 = tk.Entry(entries_monday, textvariable = monday_entry2_vusm) #Right-side entry box (end time)

        emcb1 = ttk.Combobox(entries_monday, textvariable = ampm1_emcb1, width = 10) #Left-side combo box (am/pm for start time)
        emcb1['values'] = ('am', 'pm') #Sets the values of the left-side combo box
        emcb2 = ttk.Combobox(entries_monday, textvariable = ampm2_emcb2, width = 10) #Right-side combo box (am/pm for end time)
        emcb2['values'] = ('am', 'pm') #Sets the values of the right-side combo box

        dashlabel1 = tk.Label(entries_monday, text = " - ") #Adds a - between the two entry boxes, can be changed to " to " as well

        em1.grid(row = 0, column = 1) #Puts the left-side entry box into row 0, column 1
        emcb1.grid(row = 0, column = 2) #Puts the left-side combo box into row 0, column 2
        dashlabel1.grid(row = 0, column = 3) #Puts the " - " between the boxes, row 0, column 3
        em2.grid(row = 0, column = 4) #Puts the right-side entry box into row 0, column 4
        emcb2.grid(row = 0, column = 5) #Puts the right-side combo box into row 0, column 5

        #Tuesday
        label_tuesday = tk.Label(self.vet_update_schedule, text = "Tuesday", font = "times 10")
        entries_tuesday = tk.Frame(self.vet_update_schedule)
        label_tuesday.pack(side = "top", fill = "both", expand = False)
        entries_tuesday.pack(side = "top", fill = "x")

        et1 = tk.Entry(entries_tuesday, textvariable = tuesday_entry1_vusm)
        et2 = tk.Entry(entries_tuesday, textvariable = tuesday_entry2_vusm)

        etcb1 = ttk.Combobox(entries_tuesday, textvariable = ampm1_etcb1, width = 10)
        etcb1['values'] = ('am', 'pm')
        etcb2 = ttk.Combobox(entries_tuesday, textvariable = ampm2_etcb2, width = 10)
        etcb2['values'] = ('am', 'pm')
        
        dashlabel2 = tk.Label(entries_tuesday, text = " - ")

        et1.grid(row = 1, column = 1)
        etcb1.grid(row = 1, column = 2)
        dashlabel2.grid(row = 1, column = 3)
        et2.grid(row = 1, column = 4)
        etcb2.grid(row = 1, column = 5)

        #Wednesday
        label_wednesday = tk.Label(self.vet_update_schedule, text = "Wednesday", font = "times 10")
        entries_wednesday = tk.Frame(self.vet_update_schedule)
        label_wednesday.pack(side = "top", fill = "both", expand = False)
        entries_wednesday.pack(side = "top", fill = "x")

        ew1 = tk.Entry(entries_wednesday, textvariable = wednesday_entry1_vusm)
        ew2 = tk.Entry(entries_wednesday, textvariable = wednesday_entry2_vusm)

        ewcb1 = ttk.Combobox(entries_wednesday, textvariable = ampm1_ewcb1, width = 10)
        ewcb1['values'] = ('am', 'pm')
        ewcb2 = ttk.Combobox(entries_wednesday, textvariable = ampm2_ewcb2, width = 10)
        ewcb2['values'] = ('am', 'pm')

        dashlabel3 = tk.Label(entries_wednesday, text = " - ")

        ew1.grid(row = 2, column = 1)
        ewcb1.grid(row = 2, column = 2)
        dashlabel3.grid(row = 2, column = 3)
        ew2.grid(row = 2, column = 4)
        ewcb2.grid(row = 2, column = 5)

        #Thursday
        label_thursday = tk.Label(self.vet_update_schedule, text = "Thursday", font = "times 10")
        entries_thursday = tk.Frame(self.vet_update_schedule)
        label_thursday.pack(side = "top", fill = "both", expand = False)
        entries_thursday.pack(side = "top", fill = "x")

        er1 = tk.Entry(entries_thursday, textvariable = thursday_entry1_vusm)
        er2 = tk.Entry(entries_thursday, textvariable = thursday_entry2_vusm)

        ercb1 = ttk.Combobox(entries_thursday, textvariable = ampm1_ercb1, width = 10)
        ercb1['values'] = ('am', 'pm')
        ercb2 = ttk.Combobox(entries_thursday, textvariable = ampm2_ercb2, width = 10)
        ercb2['values'] = ('am', 'pm')

        dashlabel4 = tk.Label(entries_thursday, text = " - ")

        er1.grid(row = 3, column = 1)
        ercb1.grid(row = 3, column = 2)
        dashlabel4.grid(row = 3, column = 3)
        er2.grid(row = 3, column = 4)
        ercb2.grid(row = 3, column = 5)

        #Friday
        label_friday = tk.Label(self.vet_update_schedule, text = "Friday", font = "times 10")
        entries_friday = tk.Frame(self.vet_update_schedule)
        label_friday.pack(side = "top", fill = "both", expand = False)
        entries_friday.pack(side = "top", fill = "x")

        ef1 = tk.Entry(entries_friday, textvariable = friday_entry1_vusm)
        ef2 = tk.Entry(entries_friday, textvariable = friday_entry2_vusm)

        efcb1 = ttk.Combobox(entries_friday, textvariable = ampm1_efcb1, width = 10)
        efcb1['values'] = ('am', 'pm')
        efcb2 = ttk.Combobox(entries_friday, textvariable = ampm2_efcb2, width = 10)
        efcb2['values'] = ('am', 'pm')

        dashlabel5 = tk.Label(entries_friday, text = " - ")

        ef1.grid(row = 4, column = 1)
        efcb1.grid(row = 4, column = 2)
        dashlabel5.grid(row = 4, column = 3)
        ef2.grid(row = 4, column = 4)
        efcb2.grid(row = 4, column = 5)

        #Saturday
        label_saturday = tk.Label(self.vet_update_schedule, text = "Saturday", font = "times 10")
        entries_saturday = tk.Frame(self.vet_update_schedule)
        label_saturday.pack(side = "top", fill = "both", expand = False)
        entries_saturday.pack(side = "top", fill = "x")

        esa1 = tk.Entry(entries_saturday, textvariable = saturday_entry1_vusm)
        esa2 = tk.Entry(entries_saturday, textvariable = saturday_entry2_vusm)

        esacb1 = ttk.Combobox(entries_saturday, textvariable = ampm1_esacb1, width = 10)
        esacb1['values'] = ('am', 'pm')
        esacb2 = ttk.Combobox(entries_saturday, textvariable = ampm2_esacb2, width = 10)
        esacb2['values'] = ('am', 'pm')

        dashlabel6 = tk.Label(entries_saturday, text = " - ")

        esa1.grid(row = 5, column = 1)
        esacb1.grid(row = 5, column = 2)
        dashlabel6.grid(row = 5, column = 3)
        esa2.grid(row = 5, column = 4)
        esacb2.grid(row = 5, column = 5)

        #Sunday
        label_sunday = tk.Label(self.vet_update_schedule, text = "Sunday", font = "times 10")
        entries_sunday = tk.Frame(self.vet_update_schedule)
        label_sunday.pack(side = "top", fill = "both", expand = False)
        entries_sunday.pack(side = "top", fill = "x")

        esu1 = tk.Entry(entries_sunday, textvariable = sunday_entry1_vusm)
        esu2 = tk.Entry(entries_sunday, textvariable = sunday_entry2_vusm)

        esucb1 = ttk.Combobox(entries_sunday, textvariable = ampm1_esucb1, width = 10)
        esucb1['values'] = ('am', 'pm')
        esucb2 = ttk.Combobox(entries_sunday, textvariable = ampm2_esucb2, width = 10)
        esucb2['values'] = ('am', 'pm')

        dashlabel7 = tk.Label(entries_sunday, text = " - ")

        esu1.grid(row = 6, column = 1)
        esucb1.grid(row = 6, column = 2)
        dashlabel7.grid(row = 6, column = 3)
        esu2.grid(row = 6, column = 4)
        esucb2.grid(row = 6, column = 5)
        
        # Give empty columns a weight so that they consume all extra space in the window
        # MUST BE DONE FOR EVERY SINGLE ROW/DAY
        entries_monday.grid_columnconfigure(0, weight = 1) #Creates an "invisible" left-side boundary for the columns in the Monday row
        entries_monday.grid_columnconfigure(6, weight = 1) #Creates an "invisible" right-side boundary for the columns in the Monday row

        entries_tuesday.grid_columnconfigure(0, weight = 1)
        entries_tuesday.grid_columnconfigure(6, weight = 1)

        entries_wednesday.grid_columnconfigure(0, weight = 1)
        entries_wednesday.grid_columnconfigure(6, weight = 1)

        entries_thursday.grid_columnconfigure(0, weight = 1)
        entries_thursday.grid_columnconfigure(6, weight = 1)

        entries_friday.grid_columnconfigure(0, weight = 1)
        entries_friday.grid_columnconfigure(6, weight = 1)

        entries_saturday.grid_columnconfigure(0, weight = 1)
        entries_saturday.grid_columnconfigure(6, weight = 1)

        entries_sunday.grid_columnconfigure(0, weight = 1)
        entries_sunday.grid_columnconfigure(6, weight = 1)

        Label(self.vet_update_schedule, text="").pack()
        Button(self.vet_update_schedule, text='Submit', width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = self.vet_update_schedule_info).pack()
        Label(self.vet_update_schedule, text="").pack()
        Button(self.vet_update_schedule, text="Return to Vet Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = self.vet_menu_launch).pack()

    # Takes inputs from vet_update_schedule_menu() and finds vet's LoginID from the VetLoginInfo table
    # to update the correct records in the VetScheduleInfo table
    def vet_update_schedule_info(self):
        global label
        #Get user inputs
        monday_start = em1.get()
        monday_end = em2.get()
        tuesday_start = et1.get()
        tuesday_end = et2.get()
        wednesday_start = ew1.get()
        wednesday_end = ew2.get()
        thursday_start = er1.get()
        thursday_end = er2.get()
        friday_start = ef1.get()
        friday_end = ef2.get()
        saturday_start = esa1.get()
        saturday_end = esa2.get()
        sunday_start = esu1.get()
        sunday_end = esu2.get()
        emcb1_selection = emcb1.get() #Stores the selection from the left-side combo box
        emcb2_selection = ampm2_emcb2.get() #Stores the selection from the right-side combo box
        etcb1_selection = ampm1_etcb1.get()
        etcb2_selection = ampm2_etcb2.get()
        ewcb1_selection = ampm1_ewcb1.get()
        ewcb2_selection = ampm2_ewcb2.get()
        ercb1_selection = ampm1_ercb1.get()
        ercb2_selection = ampm2_ercb2.get()
        efcb1_selection = ampm1_efcb1.get()
        efcb2_selection = ampm2_efcb2.get()
        esacb1_selection = ampm1_esacb1.get()
        esacb2_selection = ampm2_esacb2.get()
        esucb1_selection = ampm1_esucb1.get()
        esucb2_selection = ampm2_esucb2.get()

        #concat variables for update statement
        monday = monday_start + ":" + emcb1_selection + ":" + monday_end + ":" + emcb2_selection
        tuesday = tuesday_start + ":" + etcb1_selection + ":" + tuesday_end + ":" + etcb2_selection
        wednesday = wednesday_start + ":" + ewcb1_selection + ":" + wednesday_end + ":" + ewcb2_selection
        thursday = thursday_start + ":" + ercb1_selection + ":" + thursday_end + ":" + ercb2_selection
        friday = friday_start + ":" + efcb1_selection + ":" + friday_end + ":" + efcb2_selection
        saturday = saturday_start + ":" + esacb1_selection + ":" + saturday_end + ":" + esacb2_selection
        sunday = sunday_start + ":" + esucb1_selection + ":" + sunday_end + ":" + esucb2_selection

        #SQL select statements
        cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?", username2, password2)
        vet_login_ID = cursor.fetchone()
        cursor.execute("SELECT VetID FROM VetAccountInfo INNER JOIN VetLoginInfo ON VetAccountInfo.VetLoginID = VetLoginInfo.VetLoginID WHERE VetAccountInfo.VetLoginID = ?", vet_login_ID)
        vet_id = cursor.fetchone()

        #SQL update statements
        cursor.execute("UPDATE VetScheduleInfo SET Monday=?, Tuesday=?, Wednesday=?, Thursday=?, Friday=?, Saturday=?, Sunday=? WHERE VetID = ?", monday, tuesday, wednesday, thursday, friday, saturday, sunday, vet_id[0])
        cursor.commit()

        #Delete user inputs
        em1.delete(0,END)
        em2.delete(0,END)
        et1.delete(0,END)
        et2.delete(0,END)
        ew1.delete(0,END)
        ew2.delete(0,END)
        er1.delete(0,END)
        er2.delete(0,END)
        ef1.delete(0,END)
        ef2.delete(0,END)
        esa1.delete(0,END)
        esa2.delete(0,END)
        esu1.delete(0,END)
        esu2.delete(0,END)

        #tells the vet that the update was successful
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
        
        #label at the top
        Label(self.vet_update_pet, text = "").pack()
        vet_update_pet_menu_label = Label(self.vet_update_pet, text = "Veterinarian Update Pet Menu", font = "times 15")
        vet_update_pet_menu_label.pack()

        #sql query selecting all of the users registered and makes a list of them for a combobox
        query= "SELECT Concat(UserID, ', ', UserFirstName, ', ', UserLastName) FROM USERACCOUNTINFO"
                    
        my_data = cursor.execute(query) 
        my_list = [r for r, in my_data] 
        my_list2=[] 
        
        #combobox containing the list of registered users (pet owners)
        sel=tk.StringVar()
        Label(self.vet_update_pet, text='Pet Owner', font="times 15").pack()
        cb1 = ttk.Combobox(self.vet_update_pet, values=my_list,width=15,textvariable = sel)
        cb1.pack(padx=30,pady=30)

        sel.trace('w', self.my_upd)
        
        #combobox with a list of pets depending on the selection of the previous combobox
        Label(self.vet_update_pet, text='Pet Name', font="times 15").pack()
        cb2 = ttk.Combobox(self.vet_update_pet, values=my_list2, width=15,)
        cb2.pack()
        
        #entry box for the user to provide their pet's name
        pet_name_label = Label(self.vet_update_pet, text='Pet Name', font="times 15")
        pet_name_entry2 = Entry(self.vet_update_pet, font="times 15", width=20, textvariable=pet_name_var)
        pet_name_label.pack()
        pet_name_entry2.pack()

        #entry box for the user to provide their pet's type
        pet_type_label = Label(self.vet_update_pet, text='Pet Type', font="times 15")
        pet_type_entry2 = Entry(self.vet_update_pet, textvariable=pet_type_var, font="times 15", width=20)
        pet_type_label.pack()
        pet_type_entry2.pack()

        #entry box for the user to provide their pet's breed
        pet_breed_label = Label(self.vet_update_pet, text='Pet Breed', font="times 15")
        pet_breed_entry2 = Entry(self.vet_update_pet, textvariable=pet_breed_var, font="times 15")
        pet_breed_label.pack()
        pet_breed_entry2.pack()

        #entry box for the user to provide their pet's color
        pet_color_label = Label(self.vet_update_pet, text='Pet Color', font="times 15")
        pet_color_entry2 = Entry(self.vet_update_pet, textvariable=pet_color_var, font="times 15")
        pet_color_label.pack()
        pet_color_entry2.pack()

        Label(self.vet_update_pet, text="").pack()
        
        #buttons
        Button(self.vet_update_pet, text='Update Pet', width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = self.vet_pet_confirmation_popup).pack()
        Label(self.vet_update_pet, text="").pack()
        Button(self.vet_update_pet, text="Return to Vet Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = self.vet_menu_launch).pack()
    
    #updates the values of the second combobox (pets) based on the selection in the first combobox (owners)
    def my_upd(*args):
        cb2.set('') # remove the previous selected option
        selection = sel.get().split(", ")
        query = "SELECT Concat(PetID, ', ', PetName) FROM PetInfo WHERE UserID = '"+selection[0]+"'"
        my_data = cursor.execute(query) 
        my_list2 = [r for r, in my_data] 
        cb2['values']=my_list2    
    
    #the sql statement to update the pet based on selections/inputs
    def vetUpdatePet(self,*args):        
        selection2 = cb2.get().split(", ")
        global label

        #grab all of the entries
        pet_name_var = pet_name_entry2.get()
        pet_type_var = pet_type_entry2.get()
        pet_breed_var = pet_breed_entry2.get()
        pet_color_var = pet_color_entry2.get()

        #sql update statement
        cursor.execute("UPDATE PetInfo SET PetName = ?, PetType = ?, PetBreed = ?, PetColor = ? WHERE PetID = ?", pet_name_var, pet_type_var, pet_breed_var, pet_color_var, selection2[0])
        cursor.commit()

        #clear all entries
        pet_name_entry2.delete(0,END)
        pet_type_entry2.delete(0,END)
        pet_breed_entry2.delete(0,END)
        pet_color_entry2.delete(0,END)
        self.vet_pet_confirmation_des()
        cb1.set('')

        #update successful message
        label = Label(self.vet_update_pet, text="Update Successful", fg="green", font="times 15")
        label.pack()
    
    #confirmation popup when updating a pet
    def vet_pet_confirmation_popup(self):
        global vet_pet_confirmation
        vet_pet_confirmation = Toplevel(self.window)
        vet_pet_confirmation.title("Alert")
        vet_pet_confirmation.geometry("300x150")
        Label(vet_pet_confirmation, text=f'You selected {cb2.get()}.').pack()
        Button(vet_pet_confirmation, text="Update", command=self.vetUpdatePet).pack()
        Button(vet_pet_confirmation, text="No", command=self.vet_pet_confirmation_des).pack()    
    
    #clear the frame from above ^
    def vet_pet_confirmation_des(self):
        vet_pet_confirmation.destroy()
            
        
    ###########################################################################################################################################################################
    
    #displays all of the appointments for the current day for the vet thats logged in
    global j
    j=0
    def vet_daily_app(self):
        currentdate = date.today()
        currentdate = currentdate.strftime('%m/%d/%y')
        cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?", username2, password2)
        vet_login_ID = cursor.fetchone()
        cursor.execute("SELECT VetID FROM VetAccountInfo INNER JOIN VetLoginInfo ON VetAccountInfo.VetLoginID = VetLoginInfo.VetLoginID WHERE VetAccountInfo.VetLoginID = ?", vet_login_ID)
        vet_id = cursor.fetchone()
        my_data = cursor.execute("select Concat(PetInfo.PetID, ', ', 'Time: ', AppointmentInfo.Time, ' Pet: ', PetInfo.PetName) from AppointmentInfo join PetInfo on AppointmentInfo.PetID = PetInfo.PetID where AppointmentInfo.Date = ? and AppointmentInfo.VetID = ?", currentdate, vet_id[0])
        my_list = [r for r, in my_data]
        label1 = Frame(self.vet_daily_appointment)
        label1.pack(fill ="x", anchor ="n")
        label = Label(label1, text = "Today's Appointment(s)", font = "times 15")
        label.grid(row=1, column = 1)
        label1.grid_columnconfigure(0, weight = 1)
        label1.grid_columnconfigure(2, weight = 1)
        label2 = Frame(self.vet_daily_appointment,  highlightbackground="SpringGreen4", highlightthickness=2)
        label2.pack(anchor ="n")
        if(len(my_list) == 0):
            label = Label(label2, text = 'No Scheduled Appointments', font = "times 15")
            label.grid(row=0, column = 1)
            buttonframe = Frame(self.vet_daily_appointment)
            buttonframe.pack(fill="x", anchor="se")
        else:
            for i in range(len(my_list)):
                global j
                y = j + 1
                x = 1
                list_2 = my_list[i-1].split(',')
                while (j < y):
                    label = Label(label2, text = list_2[x], font = "times 15")
                    label.grid(row=j, column = 1)
                    str = list_2[0]
                    x+=1
                    j=j+1
                Button(label2, text="Upload Pet Record", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = lambda pet_default = str : self.vet_upload_pet_record_clicked(pet_default)).grid(row=j-1, column=2)
            j = 0
            label.grid(row=i, column = 1)
            label2.grid_columnconfigure(0, weight = 1)
            label2.grid_columnconfigure(2, weight = 1)    
            buttonframe = Frame(self.vet_daily_appointment)
            buttonframe.pack(fill="x", anchor="se")
        butt = Button(buttonframe, text="Return to Vet Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = self.vet_menu_launch)
        butt.grid(row = 10, column = 5, sticky = SE)
        buttonframe.grid_columnconfigure(0, weight = 1)
        buttonframe.grid_columnconfigure(2, weight = 1)

###########################################################################################################################################################################

    # Canceled Appointments function
    def vet_canceled_app(self):
        #get the vet login id
        cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?", username2, password2)
        vet_login_ID = cursor.fetchone()

        #get the vet account id
        cursor.execute("SELECT VetID FROM VetAccountInfo INNER JOIN VetLoginInfo ON VetAccountInfo.VetLoginID = VetLoginInfo.VetLoginID WHERE VetAccountInfo.VetLoginID = ?", vet_login_ID)
        vet_id = cursor.fetchone()

        #make a list of all of the canceled appointments for the current logged in vet
        my_data = cursor.execute("select Concat('Date: ', AppointmentInfo.Date, ' Time: ', AppointmentInfo.Time, ' Patient: ', PetInfo.PetName, ' Reason: ', CancellationInfo.CancelReason) from CancellationInfo join AppointmentInfo on AppointmentInfo.AppointmentID = CancellationInfo.AppointmentID join PetInfo on PetInfo.PetID = AppointmentInfo.PetID where AppointmentInfo.Cancelled = 1 and AppointmentInfo.VetID = ?", vet_id[0])
        my_list = [r for r, in my_data]

        #label at the top
        label1 = Label(self.vet_canceled_appointment, text = "Canceled Appointment(s)", font = "times 15")
        label1.pack(fill ="x", anchor ="n")

        #frame for the canceled appointments
        label2 = Frame(self.vet_canceled_appointment,  highlightbackground="SpringGreen4", highlightthickness=2)
        label2.pack(anchor ="n")

        #creation of the labels for the canceled appointments
        if(len(my_list) == 0):
            label = Label(label2, text = 'No Canceled Appointments', font = "times 15")
            label.grid(row=0, column = 1)
        for i in range(len(my_list)):
            str = my_list[i]
            label = Label(label2, text = str, font = "times 15")
            label.grid(row=i, column = 1)
        label.grid(row=1, column = 1)

        #grid columnconfigs 
        label1.grid_columnconfigure(0, weight = 1)
        label1.grid_columnconfigure(2, weight = 1)
        label2.grid_columnconfigure(0, weight = 1)
        label2.grid_columnconfigure(2, weight = 1) 

        #frame for the button and the corresponding configs
        buttonframe = Frame(self.vet_canceled_appointment)
        buttonframe.pack(fill="x", anchor="se")
        butt = Button(buttonframe, text="Return to Vet Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = self.vet_menu_launch)
        butt.grid(row = 10, column = 5, sticky = SE)
        buttonframe.grid_columnconfigure(0, weight = 1)
        buttonframe.grid_columnconfigure(2, weight = 1)

# This function creates widgets for the vets upload pet records
    def upload_pet_rec(self, pet_default):

        global pet_weight_var
        pet_weight_var = StringVar()
        global pet_month_var
        pet_month_var = StringVar()
        global pet_day_var
        pet_day_var = StringVar()
        global pet_year_var
        pet_year_var = StringVar()
        global pet_meds_var
        pet_meds_var = StringVar()
        global pet_notes_var
        pet_notes_var = StringVar()
        global pet_outcome_var
        pet_outcome_var = StringVar()
        global pet_rec_steps_var
        pet_rec_steps_var = StringVar()

        global pet_weight_entry
        global pet_meds_entry
        global pet_notes_entry
        global pet_outcome_entry
        global pet_recom_entry
        global pet_dob_entry

        # Creates a designed header
        label = Label(self.vet_upload_pet_rec, text="Upload Pet Records", font="times 50 bold", bg="SpringGreen4", anchor=N, pady=50)
        label.pack(fill=BOTH)

        # Creates a main frame
        labelX = Frame(self.vet_upload_pet_rec)
        labelX.pack(fill="x", anchor="n")
        
        my_data = cursor.execute("SELECT Concat(PetWeight, ', ', PetDOB) FROM PetInfo WHERE PetID = ?", pet_default) 

        my_list = [r for r, in my_data] 
        sel = my_list[0].split(", ")
        
        Label(labelX, text="").grid(row=0, column=0, pady=20)
        
        pet_dob_label = Label(labelX, text="Pet's Date of Birth", font = "times 15")
        pet_dob_entry = Entry(labelX, textvariable=pet_rec_steps_var, font="times 15")
        pet_dob_entry.insert(0, sel[1])
        pet_dob_label.grid(row=1, column=0, padx=5, pady=5)
        pet_dob_entry.grid(row=1, column=1, padx=5, pady=5)
        
        pet_weight_label = Label(labelX, text="Pet's weight in pounds:", font="times 15")
        pet_weight_entry = Entry(labelX, textvariable=pet_weight_var, font="times 15")
        pet_weight_entry.insert(0, sel[0])
        pet_weight_label.grid(row=2, column=0, padx=5, pady=5)
        pet_weight_entry.grid(row=2, column=1, padx=5, pady=5)

        pet_meds_label = Label(labelX, text='Medication used:', font="times 15")
        pet_meds_entry = Text(labelX, font="times 15", height="10", width="40")
        pet_meds_label.grid(row=3, column=7, padx=5, pady=5)
        pet_meds_entry.grid(row=3, column=8, padx=5, pady=5)

        pet_notes_label = Label(labelX, text='Notes:', font="times 15")
        pet_notes_entry = Text(labelX, font="times 15", height="10", width="40")
        pet_notes_label.grid(row=4, column=7, padx=5, pady=5)
        pet_notes_entry.grid(row=4, column=8, padx=5, pady=5)

        pet_outcome_label = Label(labelX, text='Outcome', font="times 15")
        pet_outcome_entry = Entry(labelX, textvariable=pet_outcome_var, font="times 15")
        pet_outcome_label.grid(row=3, column=0, padx=5, pady=5)
        pet_outcome_entry.grid(row=3, column=1, padx=5, pady=5)

        pet_recom_label = Label(labelX, text='Recommendations', font="times 15")
        pet_recom_entry = Text(labelX, font="times 15", height="10", width="40")
        pet_recom_label.grid(row=4, column=0, padx=5, pady=5)
        pet_recom_entry.grid(row=4, column=1, padx=5, pady=5)

        butt = Button(labelX, text="Upload", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = lambda: self.upload_clicked(pet_default))
        butt.grid(row = 8, column = 2)
        Button(labelX, text="Go Back", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = self.vet_daily_appointment_clicked).grid(row = 8, column = 3)
    
    # function allows for pet record to be inserted into database and updates petinfo table       
    def upload_clicked(self, pet_default):
        pet_weight_info = pet_weight_entry.get()
        pet_meds_info = pet_meds_entry.get('1.0','end-1c')
        pet_notes_info = pet_notes_entry.get('1.0','end-1c')
        pet_outcome_info = pet_outcome_entry.get()
        pet_rec_info = pet_recom_entry.get('1.0','end-1c')
        pet_dob = pet_dob_entry.get()
        
        currentdate = date.today()
        currentdate = currentdate.strftime('%m/%d/%y')
        
        cursor.execute("INSERT INTO PetRecords (PetID, PetWeight, PetMedsUsed, PetNotes, PetOutcome, PetRecom, PetRecordDate) VALUES (?, ?, ?, ?, ?, ?, ?)", pet_default, pet_weight_info, pet_meds_info, pet_notes_info, pet_outcome_info, pet_rec_info, currentdate)
        cursor.commit()
        cursor.execute("UPDATE PetInfo SET PetDOB = ?, PetWeight = ? WHERE PetID = ?", pet_dob, pet_weight_info, pet_default)
        cursor.commit()
        self.vet_daily_appointment_clicked()