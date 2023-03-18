from tkinter import * # gui import
import tkinter as tk # gui import
from tkcalendar import Calendar # gui import (must install tkcalendar "pip install tkcalendar")
from tkinter import ttk # necessary for comboboxes
import main

# This class stores all variables and methods related to the Vet 
class Vet(Tk):

    def __init__(self, window):
        super().__init__()
        self.window = window
    
    # Veterinarian login (prompts user to enter their login info, passes info to vet_login_verify for verification)
    def vet_login():
        Label(main.GUI.vet_log_in, text="Please enter details below to login", font="times 50 bold", bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
        Label(main.GUI.vet_log_in, text="").pack()

        global vet_username_verify
        global vet_password_verify

        vet_username_verify = StringVar()
        vet_password_verify = StringVar()

        global vet_username_login_entry
        global vet_password_login_entry

        Label(main.GUI.vet_log_in, font="times 30", text="Username").pack()
        vet_username_login_entry = Entry(main.GUI.vet_log_in, font="times 30", textvariable=vet_username_verify)
        vet_username_login_entry.pack()
        Label(main.GUI.vet_log_in, text="").pack()
        Label(main.GUI.vet_log_in, font="times 30", text="Password").pack()
        vet_password_login_entry = Entry(main.GUI.vet_log_in, font="times 30", textvariable=vet_password_verify, show= '*')
        vet_password_login_entry.pack()
        Label(main.GUI.vet_log_in, text="").pack()
        Button(main.GUI.vet_log_in, text="Login", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = Vet.vet_login_verify).pack()
        Label(main.GUI.vet_log_in, text="").pack()
        Button(main.GUI.vet_log_in, text="Return to Main Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = main.GUI.return_to_main).pack()

    # Vet login verification (checks that the entered vet information matches a record in VetLoginInfo table)
    def vet_login_verify():
        global label
        global username2
        global password2
        username2 = vet_username_verify.get()
        password2 = vet_password_verify.get()
        vet_username_login_entry.delete(0, END)
        vet_password_login_entry.delete(0, END)
        vet_login_ID = NONE
        if(username2 == "" or password2 == ""):
            Vet.vet_invalid_login()
        else:
            main.GUI.cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?",username2, password2)
            vet_login_ID = main.GUI.cursor.fetchone()
            if(vet_login_ID != None):
                main.GUI.vet_menu_launch()
            else:
                Vet.vet_invalid_login()

    # def vet_login_sucess():
    #     global login_success_screen
    #     login_success_screen = Toplevel(window)
    #     login_success_screen.title("Account")
    #     login_success_screen.geometry("150x100")
    #     Label(login_success_screen, text="Login Successful").pack()
    #     Button(login_success_screen, text="OK", command=delete_vet_login_success).pack()

    # def delete_vet_login_success():
    #     login_success_screen.destroy()

    # Tells the vet that their login was invalid (whatever they entered didn't match anything in the VetLoginInfo table)
    def vet_invalid_login():
        global invalid_login_screen
        invalid_login_screen = Toplevel(main.GUI.window)
        invalid_login_screen.title("Alert")
        invalid_login_screen.geometry("300x150")
        Label(invalid_login_screen, text="Invalid Login ").pack()
        Button(invalid_login_screen, text="OK", command=Vet.delete_vet_invalid_login).pack()

    # Removes the vet_invalid_login() pop-up on click
    def delete_vet_invalid_login():
        invalid_login_screen.destroy()
    ######################################################################################################################################

    # Menu that appears after successful vet login
    # Provides the options to update vet account info, update schedule info, or log out
    def vet_after_login_menu():
        Label(main.GUI.vet_menu, text="Select Your Choice", font='times 50 bold', bg='SpringGreen4', anchor=N, pady=50).pack(fill=BOTH)
        Label(main.GUI.vet_menu,text="").pack()
        Button(main.GUI.vet_menu,text="Update Account Info", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command =lambda:main.GUI.vet_update_button_clicked()).pack()
        Label(main.GUI.vet_menu,text="").pack()
        Button(main.GUI.vet_menu,text="Update Schedule Info", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = lambda:main.GUI.vet_update_schedule_clicked()).pack()
        Label(main.GUI.vet_menu,text="").pack()
        Button(main.GUI.vet_menu, text="Update Pet Info", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = lambda:main.GUI.vet_update_pet_clicked()).pack()
        Label(main.GUI.vet_menu,text="").pack()
        Button(main.GUI.vet_menu,text="Log Out", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = main.GUI.return_to_main).pack()
    ######################################################################################################################################

    # Menu that appears when the vet clicks the update account info button
    # Takes in vet's inputs and sends it to the vet_update_account() function for processing
    def vet_update_account_menu():
        
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
        
        vet_first_name_label = Label(main.GUI.vet_update_info, text='First Name', font="times 15")
        vet_first_name_entry = Entry(main.GUI.vet_update_info, textvariable=vet_first_name_var, font="times 20")
        vet_first_name_label.pack()
        vet_first_name_entry.pack()

        vet_last_name_label = Label(main.GUI.vet_update_info, text='Last Name', font="times 15")
        vet_last_name_entry = Entry(main.GUI.vet_update_info, textvariable=vet_last_name_var, font="times 20")
        vet_last_name_label.pack()
        vet_last_name_entry.pack()

        vet_email_label = Label(main.GUI.vet_update_info, text='Email', font="times 15")
        vet_email_entry = Entry(main.GUI.vet_update_info, textvariable=vet_email_var, font="times 20")
        vet_email_label.pack()
        vet_email_entry.pack()

        vet_phone_number_label = Label(main.GUI.vet_update_info, text='Phone Number', font="times 15")
        vet_phone_number_entry = Entry(main.GUI.vet_update_info, textvariable=vet_phone_number_var, font="times 20")
        vet_phone_number_label.pack()
        vet_phone_number_entry.pack()

        vet_street_address_label = Label(main.GUI.vet_update_info, text='Street Address', font="times 15")
        vet_street_address_entry = Entry(main.GUI.vet_update_info, textvariable=vet_street_address_var, font="times 20")
        vet_street_address_label.pack()
        vet_street_address_entry.pack()


        vet_city_label = Label(main.GUI.vet_update_info, text='City', font="times 15")
        vet_city_entry = Entry(main.GUI.vet_update_info, textvariable=vet_city_var, font="times 20")
        vet_city_label.pack()
        vet_city_entry.pack()

        vet_state_label = Label(main.GUI.vet_update_info, text='State', font="times 15")
        vet_state_entry = Entry(main.GUI.vet_update_info, textvariable=vet_state_var, font="times 20")
        vet_state_label.pack(side =TOP)
        vet_state_entry.pack()

        vet_zip_label = Label(main.GUI.vet_update_info, text='Zip Code', font="times 15")
        vet_zip_entry = Entry(main.GUI.vet_update_info, textvariable=vet_zip_var, font="times 20")
        vet_zip_label.pack()
        vet_zip_entry.pack()
        
        Label(main.GUI.vet_update_info, text="").pack()
        
        Button(main.GUI.vet_update_info, text='Submit', width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = Vet.vet_update_account).pack()
        Label(main.GUI.vet_update_info, text="").pack() 
        Button(main.GUI.vet_update_info, text="Return to Vet Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = main.GUI.vet_menu_launch).pack()

    # Takes inputs from vet_update_account_menu() and finds vet's LoginID from the VetLoginInfo table
    # to update the correct records in the VetAccountInfo table
    def vet_update_account():
        global label
        vet_first_name_var = vet_first_name_entry.get()
        vet_last_name_var = vet_last_name_entry.get()
        vet_email_var = vet_email_entry.get()
        vet_phone_number_var = vet_phone_number_entry.get()
        vet_street_address_var = vet_street_address_entry.get()
        vet_city_var = vet_city_entry.get()
        vet_state_var = vet_state_entry.get()
        vet_zip_var = vet_zip_entry.get()
        main.GUI.cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?", username2, password2)
        vet_login_ID = main.GUI.cursor.fetchone()
        main.GUI.cursor.execute("SELECT VetID FROM VetAccountInfo INNER JOIN VetLoginInfo ON VetAccountInfo.VetLoginID = VetLoginInfo.VetLoginID WHERE VetAccountInfo.VetLoginID = ?", vet_login_ID)
        vet_id = main.GUI.cursor.fetchone()
        main.GUI.cursor.execute("UPDATE VetAccountInfo SET VetFirstName = ?, VetLastName = ?, VetPhoneNumber = ?, VetEmailAddress = ?, VetStreetAddress = ?, VetCity = ?, VetState = ?, VetZip = ? WHERE VetID = ?", vet_first_name_var, vet_last_name_var, vet_phone_number_var, vet_email_var, vet_street_address_var, vet_city_var, vet_state_var, vet_zip_var, vet_id[0])
        main.GUI.cursor.commit()
        vet_first_name_entry.delete(0,END)
        vet_last_name_entry.delete(0,END)
        vet_phone_number_entry.delete(0,END)
        vet_email_entry.delete(0,END)
        vet_street_address_entry.delete(0,END)
        vet_city_entry.delete(0,END)
        vet_state_entry.delete(0,END)
        vet_zip_entry.delete(0,END)
        Label(main.GUI.vet_update_info, text="").pack()
        label = Label(main.GUI.vet_update_info, text="Update Successful", fg="green", font="times 15")
        label.pack()

    ##################################################################################################################################################

    # Menu that appears when the vet clicks the update schedule button
    # Takes in vet's inputs for processing in vet_update_schedule_info()
    def vet_update_schedule_menu():
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


        monday_label = Label(main.GUI.vet_update_schedule, text='Monday', font="times 15")
        monday_entry = Entry(main.GUI.vet_update_schedule, textvariable=monday, font="times 20")
        monday_label.pack()
        monday_entry.pack()

        tuesday_label = Label(main.GUI.vet_update_schedule, text='Tuesday', font="times 15")
        tuesday_entry = Entry(main.GUI.vet_update_schedule, textvariable=tuesday, font="times 20")
        tuesday_label.pack()
        tuesday_entry.pack()

        wednesday_label = Label(main.GUI.vet_update_schedule, text='Wednesday', font="times 15")
        wednesday_entry = Entry(main.GUI.vet_update_schedule, textvariable=wednesday, font="times 20")
        wednesday_label.pack()
        wednesday_entry.pack()

        thursday_label = Label(main.GUI.vet_update_schedule, text='Thursday', font="times 15")
        thursday_entry = Entry(main.GUI.vet_update_schedule, textvariable=thursday, font="times 20")
        thursday_label.pack()
        thursday_entry.pack()

        friday_label = Label(main.GUI.vet_update_schedule, text='Friday', font="times 15")
        friday_entry = Entry(main.GUI.vet_update_schedule, textvariable=friday, font="times 20")
        friday_label.pack()
        friday_entry.pack()

        saturday_label = Label(main.GUI.vet_update_schedule, text='Saturday', font="times 15")
        saturday_entry = Entry(main.GUI.vet_update_schedule, textvariable=saturday, font="times 20")
        saturday_label.pack()
        saturday_entry.pack()

        sunday_label = Label(main.GUI.vet_update_schedule, text='Sunday', font="times 15")
        sunday_entry = Entry(main.GUI.vet_update_schedule, textvariable=sunday, font="times 20")
        sunday_label.pack()
        sunday_entry.pack()    

        Label(main.GUI.vet_update_schedule, text="").pack()

        Button(main.GUI.vet_update_schedule, text='Submit', width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = Vet.vet_update_schedule_info).pack()
        Label(main.GUI.vet_update_schedule, text="").pack()
        Button(main.GUI.vet_update_schedule, text="Return to Vet Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = main.GUI.vet_menu_launch).pack()

    # Takes inputs from vet_update_schedule_menu() and finds vet's LoginID from the VetLoginInfo table
    # to update the correct records in the VetScheduleInfo table
    def vet_update_schedule_info():
        global label
        monday = monday_entry.get()
        tuesday = tuesday_entry.get()
        wednesday = wednesday_entry.get()
        thursday = thursday_entry.get()
        friday = friday_entry.get()
        saturday = saturday_entry.get()
        sunday = sunday_entry.get()
        main.GUI.cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?", username2, password2)
        vet_login_ID = main.GUI.cursor.fetchone()
        main.GUI.cursor.execute("SELECT VetID FROM VetAccountInfo INNER JOIN VetLoginInfo ON VetAccountInfo.VetLoginID = VetLoginInfo.VetLoginID WHERE VetAccountInfo.VetLoginID = ?", vet_login_ID)
        vet_id = main.GUI.cursor.fetchone()
        main.GUI.cursor.execute("UPDATE VetScheduleInfo SET Monday=?, Tuesday=?, Wednesday=?, Thursday=?, Friday=?, Saturday=?, Sunday=? WHERE VetID = ?", monday, tuesday, wednesday, thursday, friday, saturday, sunday, vet_id[0])
        main.GUI.cursor.commit()
        monday_entry.delete(0,END)
        tuesday_entry.delete(0,END)
        wednesday_entry.delete(0,END)
        thursday_entry.delete(0,END)
        friday_entry.delete(0,END)
        saturday_entry.delete(0,END)
        sunday_entry.delete(0,END)
        Label(main.GUI.vet_update_schedule, text="").pack()
        label = Label(main.GUI.vet_update_schedule, text="Update Successful", fg="green", font="times 15")
        label.pack()

    #Allows vets to select a user and update specific pet information
    def vet_update_pet_info():

        Label(main.GUI.vet_update_pet, text = "").pack()
        vet_update_pet_menu_label = Label(main.GUI.vet_update_pet, text = "Veterinarian Update Pet Menu", font = "times 15")
        vet_update_pet_menu_label.pack()

        query= "SELECT Concat(UserID, ', ', UserFirstName, ', ', UserLastName) FROM USERACCOUNTINFO"
                    
        my_data = main.GUI.cursor.execute(query) # SQLAlchem engine result
        my_list = [r for r, in my_data] # create a  list 
        my_list2=[] 
        
        def my_upd(*args):
            cb2.set('') # remove the previous selected option
            selection = sel.get().split(", ")
            query = "SELECT Concat(PetID, ', ', PetName) FROM PetInfo WHERE UserID = '"+selection[0]+"'"
            my_data = main.GUI.cursor.execute(query) # SQLAlchem engine result
            my_list2 = [r for r, in my_data] # create a  list
            cb2['values']=my_list2    
            
        def vetUpdatePet(*args):        
            selection2 = cb2.get().split(", ")
            global label
            pet_name_var = pet_name_entry2.get()
            pet_type_var = pet_type_entry2.get()
            pet_breed_var = pet_breed_entry2.get()
            pet_color_var = pet_color_entry2.get()
            main.GUI.cursor.execute("UPDATE PetInfo SET PetName = ?, PetType = ?, PetBreed = ?, PetColor = ? WHERE PetID = ?", pet_name_var, pet_type_var, pet_breed_var, pet_color_var, selection2[0])
            main.GUI.cursor.commit()
            pet_name_entry2.delete(0,END)
            pet_type_entry2.delete(0,END)
            pet_breed_entry2.delete(0,END)
            pet_color_entry2.delete(0,END)
            vet_pet_confirmation_des()
            cb1.set('')
            label = Label(main.GUI.vet_update_pet, text="Update Successful", fg="green", font="times 20")
            label.pack()
            
        def vet_pet_confirmation_popup():
            global vet_pet_confirmation
            vet_pet_confirmation = Toplevel(main.GUI.window)
            vet_pet_confirmation.title("Alert")
            vet_pet_confirmation.geometry("300x150")
            Label(vet_pet_confirmation, text=f'You selected {cb2.get()}.').pack()
            Button(vet_pet_confirmation, text="Update", command=vetUpdatePet).pack()
            Button(vet_pet_confirmation, text="No", command=vet_pet_confirmation_des).pack()    
        
        def vet_pet_confirmation_des():
            vet_pet_confirmation.destroy()
            
        sel=tk.StringVar()

        cb1 = ttk.Combobox(main.GUI.vet_update_pet, values=my_list,width=15,textvariable = sel)
        cb1.pack(padx=30,pady=30)

        sel.trace('w', my_upd)

        cb2 = ttk.Combobox(main.GUI.vet_update_pet, values=my_list2, width=15,)
        cb2.pack()
        
        pet_name_label = Label(main.GUI.vet_update_pet, text='Pet Name', font="times 15")
        pet_name_entry2 = Entry(main.GUI.vet_update_pet, font="times 20", width=20, textvariable=Vet.pet_name_var)
        pet_name_label.pack()
        pet_name_entry2.pack()

        pet_type_label = Label(main.GUI.vet_update_pet, text='Pet Type', font="times 15")
        pet_type_entry2 = Entry(main.GUI.vet_update_pet, textvariable=Vet.pet_type_var, font="times 20", width=20)
        pet_type_label.pack()
        pet_type_entry2.pack()

        pet_breed_label = Label(main.GUI.vet_update_pet, text='Pet Breed', font="times 15")
        pet_breed_entry2 = Entry(main.GUI.vet_update_pet, textvariable=Vet.pet_breed_var, font="times 20")
        pet_breed_label.pack()
        pet_breed_entry2.pack()

        pet_color_label = Label(main.GUI.vet_update_pet, text='Pet Color', font="times 15")
        pet_color_entry2 = Entry(main.GUI.vet_update_pet, textvariable=Vet.pet_color_var, font="times 20")
        pet_color_label.pack()
        pet_color_entry2.pack()

        Label(main.GUI.vet_update_pet, text="").pack()
        
        Button(main.GUI.vet_update_pet, text='Update Pet', width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = vet_pet_confirmation_popup).pack()
        Label(main.GUI.vet_update_pet, text="").pack()
        Button(main.GUI.vet_update_pet, text="Return to Vet Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = main.GUI.vet_menu_launch).pack()