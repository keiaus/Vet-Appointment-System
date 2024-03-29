from tkinter import * # gui import
import tkinter as tk # gui import
from tkinter import ttk # necessary for comboboxes
import pyodbc # necessary for aws rds sql server connection

#Connection to AWS RDS SQL Server (required to run properly)
connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=Arthur;PWD=123;')
cursor = connection.cursor()

# Used to show each frame as the menu is interacted with
def vetapp():
    create_vetapp()
    vet_update_schedule_menu()
    vet_update_account_menu()
    user_update_account_menu()
    user_update_pet_menu()
    user_register()
    pet_register()
    user_login()
    user_after_login_menu()
    vet_login()
    vet_after_login_menu()
    admin_register()
    admin_login()
    admin_after_login_menu()
    admin_vet_dropdown_menu()
    show_frame(account_page)

# Used to show each frame as the menu is interacted with
def show_frame(frame):
    frame.tkraise()

# Opens the update schedule menu on click (for vets)
def vet_update_schedule_clicked():
    window.title("Update Schedule")
    show_frame(vet_update_schedule)

# Opens the update account menu on click (for vets)
def vet_update_button_clicked():
    window.title("Update Account")
    show_frame(vet_update_info)

# Opens the update account menu on click (for users)
def user_update_button_clicked():
    window.title("Update Account")
    show_frame(user_update_info)

# Opens the update pet menu on click (for users)
def user_update_pet_button_clicked():
    window.title("Update Pet Information")
    show_frame(user_update_pet_info)

# Opens the account creation menu on click (on base menu frame)
def account_creation_clicked():
    window.title("Create Your Account")
    show_frame(account_create)

# Opens the login menu on click (on base menu frame)
def user_log_in_clicked():
    window.title("User Log In")
    show_frame(user_log_in)

# Opens the user menu after successful login (users)
def user_menu_launch():
    window.title("User Menu")
    if(isinstance(label,Label)):
        label.destroy()
        show_frame(user_menu)
    else:
        show_frame(user_menu)

# Opens the user pet menu after successful login (users)
def user_pet_menu_launch():
    window.title("User Pet Menu")
    if(isinstance(label,Label)):
        label.destroy()
        show_frame(user_pet_menu)
    else:
        show_frame(user_pet_menu)

# Opens the add pet screen on click
def user_pet_add_clicked():
    window.title("Add a Pet(s)")
    if (isinstance(label, Label)):
        label.destroy()
        show_frame(user_pet_add)
    else:
        show_frame(user_pet_add)

# Opens the vet login menu on click (vets)
def vet_log_in_clicked():
    window.title("Vet Log In")
    show_frame(vet_log_in)

# Opens the vet menu after login (vets)
def vet_menu_launch():
    window.title("Vet Menu")
    if(isinstance(label,Label)):
        label.destroy()
        show_frame(vet_menu)
    else:
        show_frame(vet_menu)

def admin_log_in_clicked():
    window.title("Admin Log In")
    show_frame(admin_log_in)

def admin_menu_launch():
    window.title("Admin Menu")
    if(isinstance(label,Label)):
        label.destroy()
        show_frame(admin_menu)
    else:
        show_frame(admin_menu)

def admin_dropdown_clicked():
    window.title("Admin Vet Delete")
    if(isinstance(label,Label)):
        label.destroy()
        show_frame(admin_vet_dropdown)
    else:
        show_frame(admin_vet_dropdown)

def admin_vet_create_clicked():
    window.title("Create a Vet")
    show_frame(admin_create_vet)

# Returns to the base account page on click
def return_to_main():
    window.title("Home")
    if(isinstance(label,Label)):
        label.destroy()
        show_frame(account_page)
    else:
        show_frame(account_page)
    
# Closes the menu
def close_clicked():
    window.destroy()

# Program window configuration
window = Tk()
window.state('zoomed')
window.title("Home")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

account_page = Frame(window)
account_create = Frame(window)
user_log_in = Frame(window)
user_menu = Frame(window)
user_pet_menu = Frame(window)
user_pet_add = Frame(window)
user_update_info = Frame(window)
vet_log_in = Frame(window)
vet_menu = Frame(window)
vet_update_info = Frame(window)
user_update_pet_info = Frame(window)
user_update_pet_dropdown = Frame(window)
vet_update_schedule = Frame(window)
admin_log_in = Frame(window)
admin_menu = Frame(window)
admin_update_info = Frame(window)
admin_create_vet = Frame(window)
admin_delete_vet = Frame(window)
admin_vet_dropdown = Frame(window)

for frame in (account_page, account_create, user_log_in, user_pet_menu, user_pet_add,  user_menu, user_update_info, user_update_pet_info, user_update_pet_dropdown, vet_log_in, vet_menu, vet_update_info, vet_update_schedule,
              admin_log_in, admin_menu, admin_update_info, admin_create_vet, admin_delete_vet, admin_vet_dropdown):
    frame.grid(row=0, column=0, sticky='nsew')

global label
label = None
# **Don't touch**
# Main window on program start
def create_vetapp():
    account_page_header = Label(account_page, text='Vet Appointment System', font='times 50 bold', bg='SpringGreen4', anchor=N, pady=50)
    account_page_header.pack(fill='both')

    Label(account_page, text="", pady=60).pack()

    create_button = Button(account_page, text='Create Account', bd=20, bg="SpringGreen4", width=20, font='times 30', command=lambda:account_creation_clicked())
    create_button.pack(pady=15, side=TOP)

    user_log_button = Button(account_page, text='User Log In', bd=20, bg="SpringGreen4", width=20, font='times 30', command=lambda:user_log_in_clicked())
    user_log_button.pack(pady=15, side=TOP)

    vet_log_button = Button(account_page, text='Vet Log In', bd=20, bg="SpringGreen4", width=20, font='times 30', command=lambda:vet_log_in_clicked())
    vet_log_button.pack(pady=15, side=TOP)
    
    admin_log_button = Button(account_page, text='Admin Log In', bd=20, bg="SpringGreen4", width=20, font='times 30', command=lambda:admin_log_in_clicked())
    admin_log_button.pack(pady=15, side=TOP)

    close_button = Button(account_page, text='Close System', bd=20, bg="SpringGreen4", width=20, font='times 30', command=lambda:close_clicked())
    close_button.pack(pady=15, side=TOP)

# User registration menu
def user_register():
    global username
    global password
    global username_entry
    global password_entry 
    username = StringVar()
    password = StringVar()
 
    Label(account_create, text="Please enter details below", font='times 50 bold', bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
    Label(account_create, text="", pady=60).pack()
    username_lable = Label(account_create, font='times 30', text="Username")
    username_lable.pack()
    username_entry = Entry(account_create, font='times 30', textvariable=username)
    username_entry.pack()
    password_lable = Label(account_create, font='times 30', text="Password")
    password_lable.pack()
    password_entry = Entry(account_create, font='times 30', textvariable=password, show='*')
    password_entry.pack()
    Label(account_create, text="", pady=60).pack()
    Button(account_create, text="Register", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = register_user).pack()
    Label(account_create, text="").pack()
    Button(account_create, text="Return to Main Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = return_to_main).pack()

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
        empty_login_info()
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

# Tells the user that the username they're trying to register with was taken
def username_taken():
    global username_taken_screen
    username_taken_screen = Toplevel(window)
    username_taken_screen.title("Alerts")
    username_taken_screen.geometry("300x150")
    Label(username_taken_screen, text="Username is already taken").pack()
    Button(username_taken_screen, text="OK", command=delete_username_taken).pack()

# Closes the username_taken() pop-up
def delete_username_taken():
    username_taken_screen.destroy()

# Tells the user that a required field was empty
def empty_login_info():
    global empty_login_info_screen
    empty_login_info_screen = Toplevel(window)
    empty_login_info_screen.title("Alert")
    empty_login_info_screen.geometry("300x150")
    Label(empty_login_info_screen, text="A field was empty, please try again.").pack()
    Button(empty_login_info_screen, text="OK", command=delete_empty_login_info).pack()    

# Closes the empty_login_info() pop-up on click
def delete_empty_login_info():
    empty_login_info_screen.destroy()
###########################################################################################################################

# Registered user login (prompts the user to enter their login info, passes info to user_login_verify for verification)
def user_login():
    Label(user_log_in, text="Please enter details below to login", font="times 50 bold", bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
    Label(user_log_in, text="", pady=60).pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(user_log_in, font="times 30", text="Username").pack()
    username_login_entry = Entry(user_log_in, font="times 30", textvariable=username_verify)
    username_login_entry.pack()
    Label(user_log_in, text="").pack()
    Label(user_log_in, font="times 30", text="Password").pack()
    password_login_entry = Entry(user_log_in, font="times 30", textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(user_log_in, text="", pady=60).pack()
    Button(user_log_in, text="Login", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = user_login_verify).pack()
    Label(user_log_in, text="").pack()
    Button(user_log_in, text="Return to Main Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = return_to_main).pack()

# User login verification (checks that the entered user information matches a record in the UserLoginInfo table)
def user_login_verify():
    global label
    global username1
    global password1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    user_login_ID = NONE
    if(username1 == "" or password1 == ""):
        user_invalid_login()
    else:
        cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username1, password1)
        user_login_ID = cursor.fetchone()
        if(user_login_ID != None):
            user_menu_launch()
        else:
            user_invalid_login()

# def user_login_sucess():
#     global login_success_screen
#     login_success_screen = Toplevel(window)
#     login_success_screen.title("Account")
#     login_success_screen.geometry("150x100")
#     Label(login_success_screen, text="Login Successful").pack()
#     Button(login_success_screen, text="OK", command=delete_user_login_success).pack()

# def delete_user_login_success():
#     login_success_screen.destroy()

# Tells the user that their login was invalid (whatever they entered didn't match anything in the UserLoginInfo table)
def user_invalid_login():
    global invalid_login_screen
    invalid_login_screen = Toplevel(window)
    invalid_login_screen.title("Alert")
    invalid_login_screen.geometry("300x150")
    Label(invalid_login_screen, text="Invalid Login ").pack()
    Button(invalid_login_screen, text="OK", command=delete_user_invalid_login).pack()

# Removes the user_invalid_login() pop-up on click
def delete_user_invalid_login():
    invalid_login_screen.destroy()
###################################################################################################################################################

# Menu that appears when the registered user clicks the update account info button
# Takes in user's inputs and sends it to the user_update_account() function for processing
def user_update_account_menu():
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

    Label(user_update_info, text="", pady=60).pack()
    
    first_name_label = Label(user_update_info, text='First Name', font="times 15")
    first_name_entry = Entry(user_update_info, font="times 20", width=20, textvariable=first_name_var)
    first_name_label.pack()
    first_name_entry.pack()

    last_name_label = Label(user_update_info, text='Last Name', font="times 15")
    last_name_entry = Entry(user_update_info, textvariable=last_name_var, font="times 20", width=20)
    last_name_label.pack()
    last_name_entry.pack()

    email_label = Label(user_update_info, text='Email', font="times 15")
    email_entry = Entry(user_update_info, textvariable=email_var, font="times 20")
    email_label.pack()
    email_entry.pack()

    phone_number_label = Label(user_update_info, text='Phone Number', font="times 15")
    phone_number_entry = Entry(user_update_info, textvariable=phone_number_var, font="times 20")
    phone_number_label.pack()
    phone_number_entry.pack()

    street_address_label = Label(user_update_info, text='Street Address', font="times 15")
    street_address_entry = Entry(user_update_info, textvariable=street_address_var, font="times 20")
    street_address_label.pack()
    street_address_entry.pack()

    city_label = Label(user_update_info, text='City', font="times 15")
    city_entry = Entry(user_update_info, textvariable=city_var, font="times 20")
    city_label.pack()
    city_entry.pack()

    state_label = Label(user_update_info, text='State', font="times 15")
    state_entry = Entry(user_update_info, textvariable=state_var, font="times 20")
    state_label.pack(side =TOP)
    state_entry.pack()

    zip_label = Label(user_update_info, text='Zip Code', font="times 15")
    zip_entry = Entry(user_update_info, textvariable=zip_var, font="times 20")
    zip_label.pack()
    zip_entry.pack()

    Label(user_update_info, text="", pady=30).pack()
    
    Button(user_update_info, text='Submit', width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = user_update_account).pack()
    Button(user_update_info, text="Return to User Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = user_menu_launch).pack()
####################################################################################################################################################################

# Menu that appears when the registered user clicks the update pet info button
# Allows the user to view pet(s) on file 
# Takes in user's inputs and sends it to the user_update_pet() function for processing
def user_update_pet_menu():
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
    pet_info_query = "select * from PetInfo"
    pet_info_query_data = list(cursor.execute(pet_info_query))
    pet_info_dictionary = {}
    pet_info_list = []

    #creates a dictionary list of the pets selected from the table and appends their id and name data
    for tablerow in pet_info_query_data:
        pet_info_dictionary[[tablerow][0][0]] = tablerow
        pet_info_list.append(tablerow[1]) #appends index 1 to the list

    #creates a display for pet info based on selection
    def pet_selection_display(*args):
        pet_info_display.config(text = "")

        for i, j in pet_info_dictionary.items():
            if j[1] == pet_info_selection.get():
                pet_info_display.config(text = str(j[0]) + ", " + j[1] + ", " + j[2] + ", " + j[3] + "," + j[4])
                # pet_id_conversion = str(j[0])
                # pet_name_conversion = j[1]
                # pet_type_conversion = j[2]
                # pet_color_conversion = j[3]
                global user_pet_id 
                global user_id 
                user_pet_id =  j[0] # stores the users selecion for update
                user_id = j[5] # stores the user selection for update

    def pet_confirmation_popup():
        global pet_confirmation
        pet_confirmation = Toplevel(window)
        pet_confirmation.title("Alert")
        pet_confirmation.geometry("300x150")
        Label(pet_confirmation, text=f'You selected {pet_info_selection.get()}.').pack()
        Button(pet_confirmation, text="Update", command=pet_confirmation_update).pack()
        Button(pet_confirmation, text="No", command=pet_confirmation_des).pack()

    def pet_confirmation_update():
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
        label = Label(user_update_pet_info, text ="Update Successful")
        label.pack()
        pet_confirmation_des()
    
    def pet_confirmation_des():
        pet_confirmation.destroy()
    
    Label(user_update_pet_info, text="Update Pet(s)", font='times 50 bold', bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
    Label(user_update_pet_info, text="", pady=20).pack()

    #combobox creation and configuration
    pet_info_selection = tk.StringVar()
    Label(user_update_pet_info, text="Select a Pet", font="times 20 bold").pack()
    pet_info_combobox = ttk.Combobox(user_update_pet_info, textvariable = pet_info_selection, values = pet_info_list)
    pet_info_combobox.pack(pady = 20)
    pet_info_display = Label(user_update_pet_info, text = "Pet Info:", bg = "SpringGreen4")
    pet_info_display.pack()
    pet_info_selection.trace("w", pet_selection_display)
    
    pet_name_label = Label(user_update_pet_info, text='Pet Name', font="times 15")
    pet_name_entry1 = Entry(user_update_pet_info, font="times 20", width=20, textvariable=pet_name_var)
    pet_name_label.pack()
    pet_name_entry1.pack()

    pet_type_label = Label(user_update_pet_info, text='Pet Type', font="times 15")
    pet_type_entry1 = Entry(user_update_pet_info, textvariable=pet_type_var, font="times 20", width=20)
    pet_type_label.pack()
    pet_type_entry1.pack()

    pet_breed_label = Label(user_update_pet_info, text='Pet Breed', font="times 15")
    pet_breed_entry1 = Entry(user_update_pet_info, textvariable=pet_breed_var, font="times 20")
    pet_breed_label.pack()
    pet_breed_entry1.pack()

    pet_color_label = Label(user_update_pet_info, text='Pet Color', font="times 15")
    pet_color_entry1 = Entry(user_update_pet_info, textvariable=pet_color_var, font="times 20")
    pet_color_label.pack()
    pet_color_entry1.pack()

    Label(user_update_pet_info, text="", pady=30).pack()
    
    Button(user_update_pet_info, text='Update Pet', width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = pet_confirmation_popup).pack()
    Label(user_update_pet_info, text="").pack()
    Button(user_update_pet_info, text="Return to User Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = user_menu_launch).pack()

####################################################################################################################################################################

# Takes inputs from user_update_account_menu() and finds user's LoginID from the UserLoginInfo table
# to update the correct records in the UserAccountInfo table
def user_update_account():
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
    label = Label(user_update_info, text="Update Successful", fg="green", font="times 20")
    label.pack()

##################################################################################################################################################

# Takes inputs from user_update_pet_menu() and finds user's LoginID from the UserLoginInfo table
# to update the correct records in the UserAccountInfo table
def user_update_pet():
    global label
    pet_name_var = pet_name_entry.get()
    pet_type_var = pet_type_entry.get()
    pet_breed_var = pet_breed_entry.get()
    pet_color_var = pet_color_entry.get()
    
    cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username1, password1)
    user_login_ID = cursor.fetchone()
    cursor.execute("SELECT PetID FROM PetInfo INNER JOIN UserLoginInfo ON PetInfo.UserLoginID = UserLoginInfo.UserLoginID WHERE PetInfo.UserLoginID = ?", user_login_ID)
    user_id = cursor.fetchone()
    cursor.execute("UPDATE PetInfo SET PetName = ?, PetType = ?, PetBreed = ?, PetColor = ? WHERE PetID = ?", pet_name_var, pet_type_var, pet_breed_var, pet_color_var, user_id[0])
    cursor.commit()
    pet_name_entry.delete(0,END)
    pet_type_entry.delete(0,END)
    pet_breed_entry.delete(0,END)
    pet_color_entry.delete(0,END)
    
    label = Label(user_update_info, text="Update Successful", fg="green", font="times 20")
    label.pack()


##################################################################################################################################################

# Menu that appears after successful user login
# Provides the options to update account info or log out
def user_after_login_menu():
    Label(user_menu, text="Select Your Choice", font='times 50 bold', bg='SpringGreen4', anchor=N, pady=50).pack(fill=BOTH)
    Label(user_menu, text="", pady=60).pack()
    Button(user_menu, text="Update Account Info", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command =lambda:user_update_button_clicked()).pack()
    Label(user_menu, text="").pack()
    Button(user_menu, text="Update Pet Info", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command =lambda:user_update_pet_button_clicked()).pack()
    Label(user_menu, text="").pack()
    Button(user_menu, text="Add New Pet", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command =lambda:user_pet_add_clicked()).pack()
    Label(user_menu, text="").pack()
    Button(user_menu, text="Log Out", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = return_to_main).pack()
    
######################################################################################################################################


# Pet registration menu
def pet_register():
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

    Label(user_pet_add, text="Add a Pet(s)", font='times 50 bold', bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
    Label(user_pet_add, text="", pady=60).pack()
    
    pet_name_label = Label(user_pet_add, text='Pet Name', font="times 15")
    pet_name_entry = Entry(user_pet_add, font="times 20", width=20, textvariable=pet_name_var)
    pet_name_label.pack()
    pet_name_entry.pack()

    pet_type_label = Label(user_pet_add, text='Pet Type', font="times 15")
    pet_type_entry = Entry(user_pet_add, textvariable=pet_type_var, font="times 20", width=20)
    pet_type_label.pack()
    pet_type_entry.pack()

    pet_breed_label = Label(user_pet_add, text='Pet Breed', font="times 15")
    pet_breed_entry = Entry(user_pet_add, textvariable=pet_breed_var, font="times 20")
    pet_breed_label.pack()
    pet_breed_entry.pack()

    pet_color_label = Label(user_pet_add, text='Pet Color', font="times 15")
    pet_color_entry = Entry(user_pet_add, textvariable=pet_color_var, font="times 20")
    pet_color_label.pack()
    pet_color_entry.pack()

    Label(user_pet_add, text="", pady=30).pack()
    
    Button(user_pet_add, text='Register Pet', width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = register_pet).pack()
    Label(user_pet_add, text="").pack()
    Button(user_pet_add, text="Return to User Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = user_menu_launch).pack()

######################################################################################################################################

# Registered pet menu
def register_pet():
    global label
    global pet_id 
    pet_name_info = pet_name_var.get()
    pet_type_info = pet_type_var.get()
    pet_breed_info = pet_breed_var.get()
    pet_color_info = pet_color_var.get()
    
    user_login_ID = None
    pet_id = None
    if(pet_name_info == "" or pet_type_info == "" or pet_breed_info == "" or pet_color_info == ""):
        pet_name_entry.delete(0, END)
        pet_type_entry.delete(0, END)
        pet_breed_entry.delete(0, END)
        pet_color_entry.delete(0, END)
        empty_login_info()
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

        Label(user_pet_add, text="").pack()

        label = Label(user_pet_add, text="Registration Successful", fg="green", font="times 20")
        label.pack() 


################################################################################################################################################

# Veterinarian login (prompts user to enter their login info, passes info to vet_login_verify for verification)
def vet_login():
    Label(vet_log_in, text="Please enter details below to login", font="times 50 bold", bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
    Label(vet_log_in, text="", pady=60).pack()
 
    global vet_username_verify
    global vet_password_verify
 
    vet_username_verify = StringVar()
    vet_password_verify = StringVar()
 
    global vet_username_login_entry
    global vet_password_login_entry
 
    Label(vet_log_in, font="times 30", text="Username").pack()
    vet_username_login_entry = Entry(vet_log_in, font="times 30", textvariable=vet_username_verify)
    vet_username_login_entry.pack()
    Label(vet_log_in, text="").pack()
    Label(vet_log_in, font="times 30", text="Password").pack()
    vet_password_login_entry = Entry(vet_log_in, font="times 30", textvariable=vet_password_verify, show= '*')
    vet_password_login_entry.pack()
    Label(vet_log_in, text="", pady=60).pack()
    Button(vet_log_in, text="Login", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = vet_login_verify).pack()
    Label(vet_log_in, text="").pack()
    Button(vet_log_in, text="Return to Main Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = return_to_main).pack()

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
        vet_invalid_login()
    else:
        cursor.execute("SELECT VetLoginID FROM VetLoginInfo WHERE VetUserName = ? AND VetPassword = ?",username2, password2)
        vet_login_ID = cursor.fetchone()
        if(vet_login_ID != None):
            vet_menu_launch()
            #VET SUB MENU REPLACES THE SUCCESS MESSAGE
        else:
            vet_invalid_login()

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
    invalid_login_screen = Toplevel(window)
    invalid_login_screen.title("Alert")
    invalid_login_screen.geometry("300x150")
    Label(invalid_login_screen, text="Invalid Login ").pack()
    Button(invalid_login_screen, text="OK", command=delete_vet_invalid_login).pack()

# Removes the vet_invalid_login() pop-up on click
def delete_vet_invalid_login():
    invalid_login_screen.destroy()
######################################################################################################################################

# Menu that appears after successful vet login
# Provides the options to update vet account info, update schedule info, or log out
def vet_after_login_menu():
    Label(vet_menu, text="Select Your Choice", font='times 50 bold', bg='SpringGreen4', anchor=N, pady=50).pack(fill=BOTH)
    Label(vet_menu,text="", pady=60).pack()
    Button(vet_menu,text="Update Account Info", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command =lambda:vet_update_button_clicked()).pack()
    Label(vet_menu,text="").pack()
    Button(vet_menu,text="Update Schedule Info", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = lambda:vet_update_schedule_clicked()).pack()
    Label(vet_menu,text="").pack()
    Button(vet_menu,text="Log Out", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = return_to_main).pack()
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
    
    vet_first_name_label = Label(vet_update_info, text='First Name', font="times 15")
    vet_first_name_entry = Entry(vet_update_info, textvariable=vet_first_name_var, font="times 20")
    vet_first_name_label.pack()
    vet_first_name_entry.pack()

    vet_last_name_label = Label(vet_update_info, text='Last Name', font="times 15")
    vet_last_name_entry = Entry(vet_update_info, textvariable=vet_last_name_var, font="times 20")
    vet_last_name_label.pack()
    vet_last_name_entry.pack()

    vet_email_label = Label(vet_update_info, text='Email', font="times 15")
    vet_email_entry = Entry(vet_update_info, textvariable=vet_email_var, font="times 20")
    vet_email_label.pack()
    vet_email_entry.pack()

    vet_phone_number_label = Label(vet_update_info, text='Phone Number', font="times 15")
    vet_phone_number_entry = Entry(vet_update_info, textvariable=vet_phone_number_var, font="times 20")
    vet_phone_number_label.pack()
    vet_phone_number_entry.pack()

    vet_street_address_label = Label(vet_update_info, text='Street Address', font="times 15")
    vet_street_address_entry = Entry(vet_update_info, textvariable=vet_street_address_var, font="times 20")
    vet_street_address_label.pack()
    vet_street_address_entry.pack()
  

    vet_city_label = Label(vet_update_info, text='City', font="times 15")
    vet_city_entry = Entry(vet_update_info, textvariable=vet_city_var, font="times 20")
    vet_city_label.pack()
    vet_city_entry.pack()

    vet_state_label = Label(vet_update_info, text='State', font="times 15")
    vet_state_entry = Entry(vet_update_info, textvariable=vet_state_var, font="times 20")
    vet_state_label.pack(side =TOP)
    vet_state_entry.pack()

    vet_zip_label = Label(vet_update_info, text='Zip Code', font="times 15")
    vet_zip_entry = Entry(vet_update_info, textvariable=vet_zip_var, font="times 20")
    vet_zip_label.pack()
    vet_zip_entry.pack()
    
    Label(vet_update_info, text="").pack()
    
    Button(vet_update_info, text='Submit', width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = vet_update_account).pack()
    Button(vet_update_info, text="Return to Vet Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = vet_menu_launch).pack()

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
    label = Label(vet_update_info, text="Update Successful", fg="green", font="times 20")
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


   monday_label = Label(vet_update_schedule, text='Monday', font="times 15")
   monday_entry = Entry(vet_update_schedule, textvariable=monday, font="times 20")
   monday_label.pack()
   monday_entry.pack()

   tuesday_label = Label(vet_update_schedule, text='Tuesday', font="times 15")
   tuesday_entry = Entry(vet_update_schedule, textvariable=tuesday, font="times 20")
   tuesday_label.pack()
   tuesday_entry.pack()

   wednesday_label = Label(vet_update_schedule, text='Wednesday', font="times 15")
   wednesday_entry = Entry(vet_update_schedule, textvariable=wednesday, font="times 20")
   wednesday_label.pack()
   wednesday_entry.pack()

   thursday_label = Label(vet_update_schedule, text='Thursday', font="times 15")
   thursday_entry = Entry(vet_update_schedule, textvariable=thursday, font="times 20")
   thursday_label.pack()
   thursday_entry.pack()

   friday_label = Label(vet_update_schedule, text='Friday', font="times 15")
   friday_entry = Entry(vet_update_schedule, textvariable=friday, font="times 20")
   friday_label.pack()
   friday_entry.pack()

   saturday_label = Label(vet_update_schedule, text='Saturday', font="times 15")
   saturday_entry = Entry(vet_update_schedule, textvariable=saturday, font="times 20")
   saturday_label.pack()
   saturday_entry.pack()

   sunday_label = Label(vet_update_schedule, text='Sunday', font="times 15")
   sunday_entry = Entry(vet_update_schedule, textvariable=sunday, font="times 20")
   sunday_label.pack()
   sunday_entry.pack()    
   
   Label(vet_update_schedule, text="").pack()

   Button(vet_update_schedule, text='Submit', width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = vet_update_schedule_info).pack()
   Button(vet_update_schedule, text="Return to Vet Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = vet_menu_launch).pack()

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
    label = Label(vet_update_schedule, text="Update Successful", fg="green", font="times 20")
    label.pack()
###########################################################################################################################################################################

#Admin Log In
def admin_login():
    Label(admin_log_in, text="Please enter details below to login", font="times 50 bold", bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
    Label(admin_log_in, text="", pady=60).pack()
 
    global admin_username_verify
    global admin_password_verify
 
    admin_username_verify = StringVar()
    admin_password_verify = StringVar()
 
    global admin_username_login_entry
    global admin_password_login_entry
 
    Label(admin_log_in, font="times 30", text="Username").pack()
    admin_username_login_entry = Entry(admin_log_in, font="times 30", textvariable=admin_username_verify)
    admin_username_login_entry.pack()
    Label(admin_log_in, text="").pack()
    Label(admin_log_in, font="times 30", text="Password").pack()
    admin_password_login_entry = Entry(admin_log_in, font="times 30", textvariable=admin_password_verify, show= '*')
    admin_password_login_entry.pack()
    Label(admin_log_in, text="", pady=60).pack()
    Button(admin_log_in, text="Login", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = admin_login_verify).pack()
    Label(admin_log_in, text="").pack()
    Button(admin_log_in, text="Return to Main Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = return_to_main).pack()

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
        admin_invalid_login()
    else:
        cursor.execute("SELECT AdminLoginID FROM AdminLoginInfo WHERE AdminUserName = ? AND AdminPassword = ?",username3, password3)
        admin_login_ID = cursor.fetchone()
        if(admin_login_ID != None):
            admin_menu_launch()
        else:
            admin_invalid_login()

###################################################################################################################################################################################

# admin invalid login
def admin_invalid_login():
    global invalid_login_screen
    invalid_login_screen = Toplevel(window)
    invalid_login_screen.title("Alert")
    invalid_login_screen.geometry("300x150")
    Label(invalid_login_screen, text="Invalid Login ").pack()
    Button(invalid_login_screen, text="OK", command=delete_admin_invalid_login).pack()

# Removes the admin_invalid_login() pop-up on click
def delete_admin_invalid_login():
    invalid_login_screen.destroy()

######################################################################################################################################

# Menu that appears after successful admin login
#NEEEDS BUTTON REPLACEMENT
def admin_after_login_menu():
    Label(admin_menu, text="Select Your Choice", font='times 50 bold', bg='SpringGreen4', anchor=N, pady=50).pack(fill=BOTH)
    Label(admin_menu,text="", pady=60).pack()
    Button(admin_menu,text="Create a Vet Login", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command =lambda:admin_vet_create_clicked()).pack()
    Label(admin_menu,text="").pack()
    Button(admin_menu,text="Delete a Vet", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = lambda:admin_dropdown_clicked()).pack()
    Label(admin_menu,text="").pack()
    Button(admin_menu,text="Log Out", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = return_to_main).pack()
    
################################################################################################################################################

def admin_register():
    global username4
    global password4
    global username_entry1
    global password_entry1 
    username4 = StringVar()
    password4 = StringVar()
 
    Label(admin_create_vet, text="Please enter details below", font='times 50 bold', bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
    Label(admin_create_vet, text="", pady=60).pack()
    username_label = Label(admin_create_vet, font='times 30', text="Username")
    username_label.pack()
    username_entry1 = Entry(admin_create_vet, font='times 30', textvariable=username4)
    username_entry1.pack()
    password_label = Label(admin_create_vet, font='times 30', text="Password")
    password_label.pack()
    password_entry1 = Entry(admin_create_vet, font='times 30', textvariable=password4, show='*')
    password_entry1.pack()
    Label(admin_create_vet, text="", pady=60).pack()
    Button(admin_create_vet, text="Register", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = add_vet_creation).pack()
    Label(admin_create_vet, text="").pack()
    Button(admin_create_vet, text="Return to Admin Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = admin_menu_launch).pack()

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
        empty_login_info()
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
 
            label = Label(admin_create_vet, text="Registration Successful", fg="green", font="times 20")
            label.pack() 
        else:
            username_entry1.delete(0, END)
            password_entry1.delete(0, END)
            username_taken()    

# Menu that appears after View Veterinarians is clicked by an admin
def admin_vet_dropdown_menu():
    global admin_view_vet_menu_label
    global admin_view_vet_combobox_prompt

    #menu labels
    admin_view_vet_menu_label = Label(admin_vet_dropdown, text = "View Veterinarians Menu", font = "times 15")
    admin_view_vet_menu_label.pack()

    admin_view_vet_combobox_prompt = Label(admin_vet_dropdown, text = "Select a Vet:", font = "times 15")
    admin_view_vet_combobox_prompt.pack()

    global admin_vetaccinfo_query
    global admin_vetaccinfo_querydata
    global admin_vetaccinfo_dictionary
    global admin_vetaccinfo_list
    global admin_vet_selection
    global admin_vet_combobox
    global admin_vet_selection_display

    #list of vets and their info from the query
    admin_vetaccinfo_query ="select * from VetAccountInfo"
    admin_vetaccinfo_querydata = list(cursor.execute(admin_vetaccinfo_query))
    admin_vetaccinfo_dictionary = {}
    admin_vetaccinfo_list = []

    #creates a dictionary list of the vets selected from the table and appends their id and name data
    for tablerow in admin_vetaccinfo_querydata:
        admin_vetaccinfo_dictionary[[tablerow][0][0]] = tablerow 
        tablerow[2] = str(tablerow[2]) + " " + str(tablerow[3]) #combines row 2 and 3 (first and last name) into the second index
        admin_vetaccinfo_list.append(tablerow[2]) #appends index 2 to the list
    
    #creates a display for vet info based on selection
    def admin_selection_display(*args):
        admin_vet_selection_display.config(text = "")
    
        for i, j in admin_vetaccinfo_dictionary.items(): 
            if j[2] == admin_vet_selection.get(): 
                admin_vet_selection_display.config(text = str(j[0]) + ", " + j[2])
                global admin_vetid
                global admin_vetloginid
                admin_vetid = j[0] #stores user selection for deletion IMPORTANT
                admin_vetloginid = j[1] #stores user selection for deletion IMPORTANT
    
    #combobox creation and configuration
    admin_vet_selection = tk.StringVar()
    admin_vet_combobox = ttk.Combobox(admin_vet_dropdown, textvariable = admin_vet_selection, values = admin_vetaccinfo_list)
    admin_vet_combobox.pack(padx = 10, pady = 30)
    admin_vet_selection_display = Label(admin_vet_dropdown, text = "Vet Info:", bg = "SpringGreen4")
    admin_vet_selection_display.pack()
    admin_vet_selection.trace("w", admin_selection_display)
    
    def admin_confirmation_popup():
        global admin_confirmation
        admin_confirmation = Toplevel(window)
        admin_confirmation.title("Alert")
        admin_confirmation.geometry("300x150")
        Label(admin_confirmation, text=f'You selected {admin_vet_selection.get()}.').pack()
        Button(admin_confirmation, text="Delete", command=admin_confirmation_del).pack()
        Button(admin_confirmation, text="No", command=admin_confirmation_des).pack()

    def admin_confirmation_del():
        cursor.execute("DELETE FROM VetScheduleInfo where VetID=?", admin_vetid)
        cursor.execute("DELETE FROM VetAccountInfo WHERE VetID=?", admin_vetid) 
        cursor.execute("DELETE FROM VetLoginInfo WHERE VetLoginID=?", admin_vetloginid)
        cursor.commit()
        label = Label(admin_vet_dropdown, text ="Successfully deleted!")
        label.pack()
        admin_confirmation_des()
    
    def admin_confirmation_des():
        admin_confirmation.destroy()

    #buttons 
    Button(admin_vet_dropdown, text="Delete Vet", width = 20, height = 1, font = 'times 20', bd = 20, bg = 'SpringGreen4', command = admin_confirmation_popup).pack()
    Button(admin_vet_dropdown, text="Return to Main Menu", width = 20, height = 1, font = 'times 20', bd = 20, bg = 'SpringGreen4', command = admin_menu_launch).pack()

####################################################################################################################################################################

















# Main window on program start (loops until closed)
vetapp()
window.mainloop()