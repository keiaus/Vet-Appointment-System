from tkinter import * # gui import
import tkinter as tk # gui import
from tkinter import ttk # necessary for comboboxes
import pyodbc # necessary for aws rds sql server connection

#Connection to AWS RDS SQL Server (required to run properly)
connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=Arthur;PWD=123;')
cursor = connection.cursor()

label = None
class Vet():

    def __init__(self, window, account_page, vet_log_in, vet_menu, vet_update_info, vet_update_schedule, vet_update_pet, appointments_frame, vet_upcoming_appointments, vet_canceled_appointments):
        super().__init__()
        self.window = window
        self.account_page = account_page
        self.vet_log_in = vet_log_in
        self.vet_menu = vet_menu
        self.vet_update_info = vet_update_info
        self.vet_update_schedule = vet_update_schedule
        self.vet_update_pet = vet_update_pet
        self.appointments_frame = appointments_frame
        self.vet_upcoming_appointments = vet_upcoming_appointments
        self.vet_canceled_appointments = vet_canceled_appointments
    
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

    def appointments_clicked(self):
         self.window.title("Appointments")
         self.show_frame(self.appointments_frame)

    def upcoming_clicked(self):
         self.window.title("Upcoming Appointments")
         self.show_frame(self.vet_upcoming_appointments)    

    def canceled_clicked(self):
         self.window.title("Canceled Appointments")
         self.show_frame(self.vet_canceled_appointments)    
            
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
    
        Label(self.vet_log_in, font="times 20", text="Username").pack()
        vet_username_login_entry = Entry(self.vet_log_in, font="times 20", textvariable=vet_username_verify)
        vet_username_login_entry.pack()
        Label(self.vet_log_in, text="").pack()
        Label(self.vet_log_in, font="times 20", text="Password").pack()
        vet_password_login_entry = Entry(self.vet_log_in, font="times 20", textvariable=vet_password_verify, show= '*')
        vet_password_login_entry.pack()
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
        Button(self.vet_menu,text="Update Account Info", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command =lambda:self.vet_update_button_clicked()).pack()
        Label(self.vet_menu,text="").pack()
        Button(self.vet_menu,text="Update Schedule Info", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = lambda:self.vet_update_schedule_clicked()).pack()
        Label(self.vet_menu,text="").pack()
        Button(self.vet_menu, text="Update Pet Info", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = lambda:self.vet_update_pet_clicked()).pack()
        Label(self.vet_menu,text="").pack()
        Button(self.vet_menu, text="View Appointments", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = lambda:self.appointments_clicked()).pack()
        Label(self.vet_menu,text="").pack()
        Button(self.vet_menu,text="Log Out", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = self.return_to_main).pack()
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
        
        vet_frame_label = Label(self.vet_update_info, text='Enter your Information', font="times 20")
        vet_frame_label.pack()
        
        vet_first_name_label = Label(self.vet_update_info, text='First Name', font="times 15")
        vet_first_name_entry = Entry(self.vet_update_info, textvariable=vet_first_name_var, font="times 15")
        vet_first_name_label.pack()
        vet_first_name_entry.pack()

        vet_last_name_label = Label(self.vet_update_info, text='Last Name', font="times 15")
        vet_last_name_entry = Entry(self.vet_update_info, textvariable=vet_last_name_var, font="times 15")
        vet_last_name_label.pack()
        vet_last_name_entry.pack()

        vet_email_label = Label(self.vet_update_info, text='Email', font="times 15")
        vet_email_entry = Entry(self.vet_update_info, textvariable=vet_email_var, font="times 15")
        vet_email_label.pack()
        vet_email_entry.pack()

        vet_phone_number_label = Label(self.vet_update_info, text='Phone Number', font="times 15")
        vet_phone_number_entry = Entry(self.vet_update_info, textvariable=vet_phone_number_var, font="times 15")
        vet_phone_number_label.pack()
        vet_phone_number_entry.pack()

        vet_street_address_label = Label(self.vet_update_info, text='Street Address', font="times 15")
        vet_street_address_entry = Entry(self.vet_update_info, textvariable=vet_street_address_var, font="times 15")
        vet_street_address_label.pack()
        vet_street_address_entry.pack()
    

        vet_city_label = Label(self.vet_update_info, text='City', font="times 15")
        vet_city_entry = Entry(self.vet_update_info, textvariable=vet_city_var, font="times 15")
        vet_city_label.pack()
        vet_city_entry.pack()

        vet_state_label = Label(self.vet_update_info, text='State', font="times 15")
        vet_state_entry = Entry(self.vet_update_info, textvariable=vet_state_var, font="times 15")
        vet_state_label.pack(side =TOP)
        vet_state_entry.pack()

        vet_zip_label = Label(self.vet_update_info, text='Zip Code', font="times 15")
        vet_zip_entry = Entry(self.vet_update_info, textvariable=vet_zip_var, font="times 15")
        vet_zip_label.pack()
        vet_zip_entry.pack()

        vet_spec_label = Label(self.vet_update_info, text='Specialization', font="times 15")
        vet_spec_label.pack()
        
        vet_spec_cb = ttk.Combobox(self.vet_update_info, textvariable = vet_spec_var, font="times 15")
        vet_spec_cb['values'] = ('Check Ups', 'Surgery', 'Dentistry', 'Other')
        vet_spec_cb.pack()
        
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
        vet_spec = vet_spec_var.get()
        cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?", username2, password2)
        vet_login_ID = cursor.fetchone()
        cursor.execute("SELECT VetID FROM VetAccountInfo INNER JOIN VetLoginInfo ON VetAccountInfo.VetLoginID = VetLoginInfo.VetLoginID WHERE VetAccountInfo.VetLoginID = ?", vet_login_ID)
        vet_id = cursor.fetchone()
        cursor.execute("UPDATE VetAccountInfo SET VetFirstName = ?, VetLastName = ?, VetPhoneNumber = ?, VetEmailAddress = ?, VetStreetAddress = ?, VetCity = ?, VetState = ?, VetZip = ?, Specialization = ? WHERE VetID = ?", vet_first_name_var, vet_last_name_var, vet_phone_number_var, vet_email_var, vet_street_address_var, vet_city_var, vet_state_var, vet_zip_var, vet_spec ,vet_id[0])
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
        
        #Label(self.vet_update_schedule, text=f'You selected {emcb1_selection}.').pack()

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
        pet_name_entry2 = Entry(self.vet_update_pet, font="times 15", width=20, textvariable=pet_name_var)
        pet_name_label.pack()
        pet_name_entry2.pack()

        pet_type_label = Label(self.vet_update_pet, text='Pet Type', font="times 15")
        pet_type_entry2 = Entry(self.vet_update_pet, textvariable=pet_type_var, font="times 15", width=20)
        pet_type_label.pack()
        pet_type_entry2.pack()

        pet_breed_label = Label(self.vet_update_pet, text='Pet Breed', font="times 15")
        pet_breed_entry2 = Entry(self.vet_update_pet, textvariable=pet_breed_var, font="times 15")
        pet_breed_label.pack()
        pet_breed_entry2.pack()

        pet_color_label = Label(self.vet_update_pet, text='Pet Color', font="times 15")
        pet_color_entry2 = Entry(self.vet_update_pet, textvariable=pet_color_var, font="times 15")
        pet_color_label.pack()
        pet_color_entry2.pack()

        Label(self.vet_update_pet, text="").pack()
        
        Button(self.vet_update_pet, text='Update Pet', width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = self.vet_pet_confirmation_popup).pack()
        Label(self.vet_update_pet, text="").pack()
        Button(self.vet_update_pet, text="Return to Vet Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = self.vet_menu_launch).pack()

    # This function displays buttons to view upcoming and canceled appointments for the vets
    def vet_appointments(self):
        Label(self.appointments_frame, text="Appointments", font='times 50 bold', bg='SpringGreen4', anchor=N, pady=50).pack(fill=BOTH)
        Label(self.appointments_frame,text="").pack()
        upcoming_appointments = Button(self.appointments_frame, text="Upcoming Appointments", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = self.upcoming_clicked).pack()
        Label(self.vet_update_pet, text="").pack()
        canceled_appointments = Button(self.appointments_frame, text="Canceled Appointments", width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = self.canceled_clicked).pack()
        
    # This function displays the upcoming appointments for the vets in a table form
    def upcoming(self):
        Label(self.vet_upcoming_appointments, text="Upcoming Appointments", font='times 50 bold', bg='SpringGreen4', anchor=N, pady=50).pack(fill=BOTH)
        Label(self.vet_upcoming_appointments,text="").pack()

        # code for making the table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(self.vet_upcoming_appointments, width=20, fg="SpringGreen4", font=('Arial', 'times 10', 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, listt[i][j])

        pet_name = cursor.execute("select PetName from PetInfo where PetInfo.PetID = AppointmentInfo.PetID")
        cursor.fetchone

        pet_type = cursor.execute("select PetType from PetInfo where PetInfo.PetID = AppointmentInfo.PetID")
        cursor.fetchone

        get_date = cursor.execute("select Date from AppointmentInfo where Date.")

    listt = 




    def canceled(self):

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
        label = Label(self.vet_update_pet, text="Update Successful", fg="green", font="times 15")
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
        