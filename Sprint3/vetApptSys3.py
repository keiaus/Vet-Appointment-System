from tkinter import * # gui import
import tkinter as tk # gui import
from tkcalendar import Calendar, DateEntry # gui import (must install tkcalendar "pip install tkcalendar")
from tkinter import ttk # necessary for comboboxes
import pyodbc # necessary for aws rds sql server connection
import os # used in obtaining image directory path
from ttkwidgets.autocomplete import AutocompleteCombobox # import ttkwidgets to import AutoCompleteBox widget
import tkinter.messagebox
# new appointment button images
dir = os.path.abspath("create_new_appointment\widget_images")

#Connection to AWS RDS SQL Server (required to run properly)
connection = pyodbc.connect('DRIVER={SQL Server};PORT=1433;SERVER=database-1.ci7iawyx7c5x.us-east-1.rds.amazonaws.com;DATABASE=VetAppointmentSystem;UID=Arthur;PWD=123;')
cursor = connection.cursor()

# Used to show each frame as the menu is interacted with
def vetapp():
    create_vetapp()
    calendar_display()
    user_register()
    user_login()
    user_after_login_menu()
    user_update_account_menu()
    pet_register()
    vet_login()
    vet_after_login_menu()
    vet_update_schedule_menu()
    vet_update_account_menu()
    admin_register()
    admin_login()
    admin_after_login_menu()
    show_frame(account_page)
    # added new appointment function
    new_appointment()
    # ---

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

# Opens the update pet menu on click (for vets)
def vet_update_pet_clicked():
    window.title("Update Pet")
    show_frame(vet_update_pet)

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

# Opens the calendar menu on click (on base menu frame)
def calendar_clicked():
    window.title("Calendar")
    show_frame(calendar)

# -- added by Kashaf
# Opens the new_appointment menu on click (on base menu frame)
def new_appointment_clicked():
    window.title("New Appointment")
    show_frame(new_appointment_menu)
# Opens the login menu on click (on base menu frame)
def user_log_in_clicked():
    window.title("User Log In")
    show_frame(user_log_in)


# Opens the user menu after successful login (users)
def user_menu_launch():
    window.title("User Menu")
    if(isinstance(label,Label)):
        label.destroy()
        clear_user_frame()
        user_update_pet_menu()
        show_frame(user_menu)
    else:
        clear_user_frame()
        user_update_pet_menu()
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
        clear_vet_frame()
        vet_update_pet_info()
        show_frame(vet_menu)
    else:
        clear_vet_frame()
        vet_update_pet_info()
        show_frame(vet_menu)

def admin_log_in_clicked():
    window.title("Admin Log In")
    show_frame(admin_log_in)

def admin_menu_launch():
    window.title("Admin Menu")
    if(isinstance(label,Label)):
        label.destroy()
        clear_admin_frame()
        admin_vet_dropdown_menu()
        show_frame(admin_menu)
    else:
        clear_admin_frame()
        admin_vet_dropdown_menu()
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
        clear_all_frame()
        show_frame(account_page)
    else:
        clear_all_frame()
        show_frame(account_page)

def clear_all_frame():
    for widgets in user_update_pet_info.winfo_children():
        widgets.destroy()
    for widgets in vet_update_pet.winfo_children():
        widgets.destroy()
    for widgets in admin_vet_dropdown.winfo_children():
        widgets.destroy()
    user_update_pet_info.pack_forget()
    vet_update_pet.pack_forget()
    admin_vet_dropdown.pack_forget()

def clear_user_frame():
    for widgets in user_update_pet_info.winfo_children():
        widgets.destroy()
    user_update_pet_info.pack_forget()

def clear_vet_frame():
    for widgets in vet_update_pet.winfo_children():
        widgets.destroy()
    vet_update_pet.pack_forget()

def clear_admin_frame():
    for widgets in admin_vet_dropdown.winfo_children():
        widgets.destroy()
    admin_vet_dropdown.pack_forget()
    
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
calendar = Frame(window)
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
vet_update_pet = Frame(window)
admin_log_in = Frame(window)
admin_menu = Frame(window)
admin_update_info = Frame(window)
admin_create_vet = Frame(window)
admin_delete_vet = Frame(window)
admin_vet_dropdown = Frame(window)
# added new_appointment_menu frame
new_appointment_menu = Frame(window)

for frame in (account_page, account_create, calendar, user_log_in, user_pet_menu, user_pet_add,  user_menu, user_update_info, user_update_pet_info, 
              user_update_pet_dropdown, vet_log_in, vet_menu, vet_update_info, vet_update_schedule, vet_update_pet,
              admin_log_in, admin_menu, admin_update_info, admin_create_vet, admin_delete_vet, admin_vet_dropdown,new_appointment_menu):
    frame.grid(row=0, column=0, sticky='nsew')

global label
label = None
# **Don't touch**
# Main window on program start
def create_vetapp():
    account_page_header = Label(account_page, text='Vet Appointment System', font='times 50 bold', bg='SpringGreen4', anchor=N, pady=50)
    account_page_header.pack(fill='both')

    Label(account_page, text="").pack()

    create_button = Button(account_page, text='Create Account', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:account_creation_clicked())
    create_button.pack(pady=15, side=TOP)

    user_log_button = Button(account_page, text='User Log In', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:user_log_in_clicked())
    user_log_button.pack(pady=15, side=TOP)

    vet_log_button = Button(account_page, text='Vet Log In', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:vet_log_in_clicked())
    vet_log_button.pack(pady=15, side=TOP)
    
    admin_log_button = Button(account_page, text='Admin Log In', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:admin_log_in_clicked())
    admin_log_button.pack(pady=15, side=TOP)

    calendar_button = Button(account_page, text='Calendar', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:calendar_clicked())
    calendar_button.pack(pady=15, side=TOP)

    # new appointment button -- added by Kashaf
    new_appointment_button = Button(account_page, text="New Appointment", bd=20, bg="SpringGreen4", width=20,
                                    font='times 15', command=lambda: new_appointment_clicked())
    new_appointment_button.pack(pady=15, side=TOP)
    # ----------------------------

    close_button = Button(account_page, text='Close System', bd=20, bg="SpringGreen4", width=20, font='times 15', command=lambda:close_clicked())
    close_button.pack(pady=15, side=TOP)

# -- new appointment function -- added by Kashaf --
pixelVirtual = tk.PhotoImage(width=1, height=1)
def new_appointment():
    nav_bar_frame = LabelFrame(new_appointment_menu, bg="#FFFFFF", height=100, width=1440, pady=10, padx=350)
    nav_bar_frame.grid(row=0, column=0)

    # Main Menu Button
    new_appointment_nav_button_1 = Button(nav_bar_frame, text="Button 1 (temp main menu)", image=pixelVirtual,
                                          width=200,
                                          height=25,
                                          compound=tk.CENTER,
                                          command=return_to_main,
                                          bg='#008000')
    new_appointment_nav_button_1.grid(row=0, column=0, padx=20, pady=0, sticky='nw')

    # ----------------------------------------------------------

    # Existing Appointment Search

    def appointment_search(event):
        search_appointment_value = event.widget.get()
        if search_appointment_value == '':
            appointment_dropdown['values'] = appointment_list
        else:
            data = []

            for appointment in appointment_list:
                if search_appointment_value.lower() in appointment.lower():
                    data.append(appointment)
            appointment_dropdown['values'] = data

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Custom.TCombobox", background='white', arrowsize=20, bordercolor='black')
    style.configure("Custom.TSpinbox", background='white', arrowsize=15, bordercolor='black')
    style.configure("Custom.DateEntry", background='white', arrowsize=15, bordercolor='black')
    style.configure("Custom.Button", background='white', arrowsize=15, bordercolor='black')
    appointment_list = ['Search existing appointments', 'Appointment date and time - Pet Owner Name - Pet Name ..']
    appointment_dropdown = ttk.Combobox(nav_bar_frame, values=appointment_list, style="Custom.TCombobox")
    appointment_dropdown.current(0)
    appointment_dropdown.grid(row=0, column=1, padx=20, pady=0, ipadx=125, ipady=6, sticky='ne')
    appointment_dropdown.bind('KeyRelease', appointment_search)
    # ----------------------------------------------------------

    # vet dashboard button
    new_appointment_nav_button_2 = Button(nav_bar_frame, text="Button 2 Temp", image=pixelVirtual,
                                          width=200,
                                          height=25,
                                          compound=tk.CENTER,
                                          command=return_to_main,
                                          bg='#008000')

    new_appointment_nav_button_2.grid(row=0, column=2, padx=20, pady=0, sticky='ne')
    # ----------------------------------------------------------

    # new_appointment_nav_button_3
    new_appointment_nav_button_3 = Button(nav_bar_frame, text="Button 3 Temp", image=pixelVirtual,
                                          width=200,
                                          height=25,
                                          compound=tk.CENTER,
                                          command=return_to_main,
                                          bg='#008000')

    new_appointment_nav_button_3.grid(row=0, column=3, padx=20, pady=0, sticky='ne')

    # Create new appointment frame
    new_appointment_frame = Frame(new_appointment_menu, bg="white", width=800, height=590, bd=2, relief='ridge')
    new_appointment_frame.grid(row=1, column=0, padx=400, pady=100, sticky='nw')
    # ----------------------------------------------------------

    # Create new appointment label
    create_new_appointment_label = ttk.Label(
        new_appointment_frame,
        text="Create New Appointment",
        font=("Alata Regular", 16),
        background='white'
    )
    create_new_appointment_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
    # # -- Patient Search --
    ttk.Label(new_appointment_frame,
              anchor="nw",
              text="Patient",
              font=("Alata Regular", 12 * -1, "bold"),
              background='white'
              ).grid(row=1, column=0, padx=5, pady=5, sticky="nw")
    current_pets = []
    def pet_search():
        cursor.execute(
            "SELECT Pet.PetName, CONCAT_WS(' ',Client.UserFirstName, Client.UserLastName) as ClientFullName, Client.UserPhoneNumber, Client.UserEmailAddress \
            FROM PetInfo AS Pet \
            INNER JOIN UserAccountInfo AS Client \
            ON Pet.UserID = Client.UserID ")

        data = cursor.fetchall()
        # Creating list of patient names by concatenating first and last names
        pet_info = [f"{row[0]}, {row[1]}, {row[2]}, {row[3]} " for row in data]
        for item in pet_info:
            if item not in current_pets:
                current_pets.append(item)
        return current_pets
    pet_search()
    pet_var = tk.StringVar()
    patient_dropdown = AutocompleteCombobox(new_appointment_frame,completevalues=current_pets,textvariable=pet_var)
    patient_dropdown.grid(row=2, column=0, padx=5, pady=5, ipadx=150, ipady=5, sticky="nw")
    # # -----------------------------------------------------------------

    # # -- Veterinarian search --
    vet_search_label = ttk.Label(new_appointment_frame,
                                 anchor="nw",
                                 text="Veterinarian",
                                 font=("Alata Regular", 12 * -1, "bold"),
                                 background='white'
                                 )
    vet_search_label.grid(row=1, column=3, padx=5, pady=5, sticky="nw")
    veterinarian_names = ['No Preference']

    def get_vet_names():
        cursor.execute("SELECT CONCAT_WS(', ',VetLastName,VetFirstName) FROM VetAccountInfo WHERE NOT VetLastName = "
                       "'' AND NOT VetFirstName = '' ")
        current_vets = list(cursor.fetchall())
        for vet in current_vets:
            full_name = f"{vet[0]}"
            if full_name not in veterinarian_names:
                veterinarian_names.append(str(full_name))
        return veterinarian_names

    get_vet_names()
    vet_var = tk.StringVar()
    veterinarian_dropdown = ttk.Combobox(new_appointment_frame, values=veterinarian_names, state='readonly',
                                         style="Custom.TCombobox")

    veterinarian_dropdown.set('Select Veterinarian')
    veterinarian_dropdown.grid(row=2, column=3, padx=5, pady=5, ipadx=40, ipady=5, sticky="nw")


    # # -----------------------------------------------------------------

    # # -- Appointment Type --
    appointment_type_label = ttk.Label(new_appointment_frame,
                                       anchor="nw",
                                       text="Appointment Type",
                                       font=("Alata Regular", 12 * -1, "bold"),
                                       background='white'
                                       )
    appointment_type_label.grid(row=3, column=0, padx=5, pady=5, sticky="nw")
    appointment_type_entry = tk.StringVar()
    appointment_type_list = ['New Client Visit', 'Sick Visit', 'Follow-up Visit', 'Routine Wellness Exam',
                             'Vaccinations', 'Emergency/Urgent Care', 'Surgical Consultation', 'Euthanasia']
    appointment_type_dropdown = ttk.Combobox(new_appointment_frame, values=appointment_type_list, state='readonly',
                                             style="Custom.TCombobox")
    appointment_type_dropdown.set("Select Apppointment Type")
    appointment_type_dropdown.grid(row=4, column=0, padx=5, pady=5, ipadx=40, ipady=5, sticky="nw")

    # # -- Reason for visit --
    reason_for_visit_label = ttk.Label(new_appointment_frame,
                                       anchor="nw",
                                       text="Reason For Visit",
                                       font=("Alata Regular", 12 * -1, "bold"),
                                       background='white'
                                       )
    reason_for_visit_label.grid(row=5, column=0, padx=5, pady=5, sticky="nw")

    reason_for_visit_entry = Text(new_appointment_frame,
                                  bd=2,
                                  bg="#FFFFFF",
                                  fg='#000716',
                                  highlightthickness=0
                                  )
    reason_for_visit_entry.grid(row=6, column=0, padx=5, pady=5, sticky="nw")
    # # -----------------------------------------------------------------
    #
    # date, time, duration, end time grid frame
    datetime_input_frame = LabelFrame(new_appointment_frame, bg="white", width=800, height=200, bd=2, relief='ridge')
    datetime_input_frame.grid(row=7, column=0, padx=5, pady=5, sticky='nsew')

    # # ----------------------------------------------------------
    # # -- Date --
    date_entry = StringVar()
    import datetime
    def date_input():
        datelabel = ttk.Label(
            datetime_input_frame,
            text="Date",
            font=("Alata Regular", 12 * -1, "bold"),
            background='white'
        )
        datelabel.grid(row=1, column=0, padx=5, pady=5, sticky="nw")
        today = datetime.date.today()

        date_dropdown = DateEntry(datetime_input_frame,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  relief="flat",
                                  mindate=today,
                                  selectmode='day',
                                  textvariable=date_entry,
                                  anchor="nw",
                                  style='Custom.TCombobox'
                                  )
        date_dropdown.grid(row=2, column=0, pady=5, ipady=7, ipadx=5)
        date_dropdown.set_date(today)
    select_date_button = ttk.Button(datetime_input_frame, text="Select Date", command=date_input)
    select_date_button.grid(row=2, column=0, pady=5)
    date_selected = date_entry.get()
    date_entry.set(str(datetime.date.today()))

    # ----------------------------------------------------------

    # # -- Time --
    timelabel = ttk.Label(
        datetime_input_frame,
        text="Time",
        font=("Alata Regular", 12 * -1, "bold"),
        background='white'
    )
    timelabel.grid(row=1, column=1, padx=5, pady=5, sticky="nw")
    #
    time_list = []
    time_value = StringVar()

    for hour in [8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7]:
        for minute in range(0, 60, 5):
            time_list.append(
                f'{"0" + str(hour) if hour in (1, 2, 3, 4, 5, 6, 7, 8, 9) else str(hour)}:'
                f'{"0" + str(minute) if minute < 10 else str(minute)}'
                f' {"AM" if hour in (8, 9, 10, 11) else "PM"}')

    def display_time():
        selected_time = time_listbox.get()
        display_selected_time = f"Selected Time:  {str(selected_time)}"
        label.configure(text=display_selected_time)
        return selected_time

    #
    time_listbox = ttk.Spinbox(datetime_input_frame, values=time_list, textvariable=time_value, command=display_time,
                               state='readonly', style="Custom.TSpinbox")
    time_listbox.grid(row=2, column=1, padx=5, pady=5, sticky="nw")
    time_listbox.set(time_list[0])
    text = f"Selected Time:  {str(time_listbox.get())}"
    label = ttk.Label(datetime_input_frame, text=text)
    label.grid(row=3, column=1, padx=5, pady=5, sticky="nw")
    time_selected = time_listbox.get()
    # ------------------------------------------------------------
    #
    # # -- Duration --
    durationlabel = ttk.Label(datetime_input_frame,
                              anchor="nw",
                              text="Duration",
                              font=("Alata Regular", 12 * -1, "bold"),
                              background='white'
                              )
    durationlabel.grid(row=1, column=3, padx=5, pady=5, sticky="w")
    duration_list = []
    for duration_time in range(5, 61, 5):
        duration_list.append(f"{duration_time} Minutes")
    #
    duration_time_entry = tk.StringVar()
    duration_dropdown = ttk.Combobox(datetime_input_frame,
                                     values=duration_list,
                                     state='readonly',
                                     width=20,
                                     height=4, style="Custom.TCombobox")
    duration_dropdown.set(duration_list[0])
    duration_dropdown.grid(row=2, column=3, padx=5, pady=5, ipady=6, sticky="nw")

    # # -----------------------------------------------------------------
    #
    # # # -- End Time --
    ttk.Label(datetime_input_frame,
              anchor="ne",
              text="End Time",
              font=("Alata Regular", 12 * -1, "bold"),
              background='white'
              ).grid(row=1, column=4, padx=5, pady=5, sticky="ne")

    global end_time_str
    end_label = ttk.Label(datetime_input_frame)

    def calc_end_time():
        start_time = time_listbox.get()
        start_hour = int(start_time[0:2])
        start_minutes = int(start_time[3:5])
        duration = int(duration_dropdown.get()[0:2])
        overall_minutes = start_minutes + duration
        end_time_str = ""
        if overall_minutes >= 60:
            end_minutes = overall_minutes - 60
            start_hour += 1
            end_time_str = f"{'0' + str(start_hour) if start_hour in (1, 2, 3, 4, 5, 6, 7, 8, 9) else str(start_hour)}:" \
                           f"{'0' + str(end_minutes) if end_minutes < 10 else str(end_minutes)} " \
                           f"{'AM' if start_hour in (8, 9, 10, 11) else 'PM'}"
        elif overall_minutes < 60:
            end_time_str = f"{'0' + str(start_hour) if start_hour in (1, 2, 3, 4, 5, 6, 7, 8, 9) else str(start_hour)}:" \
                           f"{'0' + str(overall_minutes) if overall_minutes < 10 else str(overall_minutes)} " \
                           f"{'AM' if start_hour in (8, 9, 10, 11) else 'PM'}"
        if time_listbox.get() != 0 and date_selected != 0 and duration_dropdown.get() != 0:
            end_time_calculation.grid(row=2, column=4, padx=5, pady=5, sticky="nw")
        end_label.configure(text=end_time_str)
        return end_time_str

    # prints to console at the moment
    end_time_calculation = Button(datetime_input_frame,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  relief="ridge",
                                  overrelief="ridge",
                                  command=calc_end_time,
                                  background="green",
                                  text="click"
                                  )

    end_time_calculation.grid(row=2, column=4, padx=5, pady=5, sticky="nw")
    end_label.grid(row=3, column=4, padx=5, pady=5, sticky="nw")
    # # -----------------------------------------------------------------

    # # Save Button
    # displayed in pop up message box after clicking save
    def appointment_details():
        appointment_scheduled = f"Patient Name: {patient_dropdown.get().split(', ')[0]}\n" \
                                f"Client Name: {patient_dropdown.get().split(', ')[1]}\n" \
                                f"Client Phone Number: {patient_dropdown.get().split(', ')[2]}\n" \
                                f"Client Email Address: {patient_dropdown.get().split(', ')[2]}\n" \
                                f"Veterinarian: {veterinarian_dropdown.get()}\n" \
                                f"Appointment Type: {appointment_type_dropdown.get()}\n" \
                                f"Reason: {reason_for_visit_entry.get('1.0', 'end-1c')}\n" \
                                f"Date: {date_entry.get()}\n" \
                                f"Start Time: {time_selected}\n" \
                                f"End Time: {calc_end_time()}"
        print(appointment_scheduled)
        return appointment_scheduled
    # resets form after confirming appointment details
    def reset_new_appointment_form():
        patient_dropdown.set("Select pet by searching pet name, or click dropdown to view all pets")
        veterinarian_dropdown.set("Select Veterinarian")
        appointment_type_dropdown.set("Select Appointment Type")
        reason_for_visit_entry.delete("1.0", "end-1c")
        date_entry.set(str(datetime.date.today()))
        time_listbox.set(time_list[0])
        duration_dropdown.set(duration_list[0])

    # pop up window for save button
    def save_button_clicked():
        message_box = tkinter.messagebox.askyesnocancel("Confirm Appt",message=appointment_details())
        if message_box:
            reset_new_appointment_form()


    save_button_image = PhotoImage(
        file=dir + r"\save_btn.png")
    save_button = Button(new_appointment_frame,
                         image=save_button_image,
                         borderwidth=0,
                         highlightthickness=0,
                         command=save_button_clicked,
                         relief="flat"
                         )
    save_button.image = save_button_image
    save_button.grid(row=10, column=3, padx=5, pady=20, sticky="nw")
    # # ----------------------------------------------------------

    # # Cancel Button

    cancel_button_image = PhotoImage(
        file=dir + r"\cancel_btn.png")
    cancel_button = Button(new_appointment_frame,
                           image=cancel_button_image,
                           borderwidth=0,
                           highlightthickness=0,
                           command=lambda: print("cancel button clicked"),
                           relief="raised",
                           highlightcolor="black"
                           )
    cancel_button.image = cancel_button_image
    cancel_button.grid(row=10, column=0, padx=5, pady=20, sticky="nw")
    # end new_appointment function
def calendar_display():
    cal = Calendar(calendar, selectmode = 'day', year = 2023, month = 3, day = 14)
    cal.pack(pady = 300)
    
    date = Label(calendar, text = "")
    date.pack(pady = 20)

# User registration menu
def user_register():
    global username
    global password
    global username_entry
    global password_entry 
    username = StringVar()
    password = StringVar()
 
    Label(account_create, text="Please enter details below", font='times 50 bold', bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
    Label(account_create, text="").pack()
    username_lable = Label(account_create, font='times 30', text="Username")
    username_lable.pack()
    username_entry = Entry(account_create, font='times 30', textvariable=username)
    username_entry.pack()
    password_lable = Label(account_create, font='times 30', text="Password")
    password_lable.pack()
    password_entry = Entry(account_create, font='times 30', textvariable=password, show='*')
    password_entry.pack()
    Label(account_create, text="").pack()
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
    Label(user_log_in, text="").pack()
 
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
    Label(user_log_in, text="").pack()
    Button(user_log_in, text="Login", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = user_login_verify).pack()
    Label(user_log_in, text="").pack()
    Button(user_log_in, text="Return to Main Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = return_to_main).pack()

#user_id1 = NONE
# User login verification (checks that the entered user information matches a record in the UserLoginInfo table)
counter = 0
def user_login_verify():
    global label
    global username1
    global password1
    username1 = username_verify.get()
    password1 = password_verify.get() 
    user_login_ID = NONE
    if(username1 == "" or password1 == ""): 
        user_invalid_login()
    else: 
        user_login_ID = getUserLoginID()
        if(user_login_ID != None): 
            user_menu_launch() 
        else:
            user_invalid_login()


def getUserID():
    #global user_id1

    user_login_ID = getUserLoginID()
    
    cursor.execute("select UserID from UserAccountInfo where UserLoginID = ?", user_login_ID)
    user_id1 = cursor.fetchone()
    
    return user_id1

def getUserLoginID():
    global user_login_ID

    username1 = username_verify.get()
    password1 = password_verify.get()

    cursor.execute("SELECT UserLoginID FROM UserLoginInfo WHERE UserUserName = ? AND UserPassword = ?", username1, password1)
    user_login_ID = cursor.fetchone()

    #username_login_entry.delete(0, END)
    #password_login_entry.delete(0, END)

    return user_login_ID

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

    Label(user_update_info, text="").pack()
    
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
    
    Label(user_update_info, text="").pack()
    Button(user_update_info, text='Submit', width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = user_update_account).pack()
    Label(user_update_info, text="").pack()
    Button(user_update_info, text="Return to User Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = user_menu_launch).pack()
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
    #user_id1 = getUserID()
    
    user_id1 = getUserID()
    pet_info_query_data = list(cursor.execute("select * from PetInfo where UserID =?", user_id1))
    pet_info_dictionary = {}
    pet_info_list = []
    
    #Label(user_update_pet_info, text=str(user_id1)).pack()
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
    
    Label(user_update_pet_info, text="Update Pet(s)", font='times 50 bold', bg="SpringGreen4", anchor=N).pack(fill=BOTH)
    Label(user_update_pet_info, text="").pack()

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

    Label(user_update_pet_info, text="").pack()
    
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
    Label(user_update_info, text="").pack()
    label = Label(user_update_info, text="Update Successful", fg="green", font="times 15")
    label.pack()

##################################################################################################################################################

# Takes inputs from user_update_pet_menu() and finds user's LoginID from the UserLoginInfo table
# to update the correct records in the UserAccountInfo table
def user_update_pet():
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
    
    label = Label(user_update_info, text="Update Successful", fg="green", font="times 20")
    label.pack()


##################################################################################################################################################

# Menu that appears after successful user login
# Provides the options to update account info or log out
def user_after_login_menu():
    Label(user_menu, text="Select Your Choice", font='times 50 bold', bg='SpringGreen4', anchor=N, pady=50).pack(fill=BOTH)
    Label(user_menu, text="").pack()
    Button(user_menu, text="Update Account Info", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command =lambda:user_update_button_clicked()).pack()
    Label(user_menu, text="").pack()
    Button(user_menu, text="Add New Pet", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command =lambda:user_pet_add_clicked()).pack()
    Label(user_menu, text="").pack()
    Button(user_menu, text="Update Pet Info", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command =lambda:user_update_pet_button_clicked()).pack()
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
    Label(user_pet_add, text="").pack()
    
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

    Label(user_pet_add, text="").pack()
    Button(user_pet_add, text='Register Pet', width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = register_pet).pack()
    Label(user_pet_add, text="").pack()
    Button(user_pet_add, text="Return to User Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = user_menu_launch).pack()

######################################################################################################################################

# Registered pet menu
def register_pet():
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

        label = Label(user_pet_add, text="Registration Successful", fg="green", font="times 15")
        label.pack() 


################################################################################################################################################

# Veterinarian login (prompts user to enter their login info, passes info to vet_login_verify for verification)
def vet_login():
    Label(vet_log_in, text="Please enter details below to login", font="times 50 bold", bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
    Label(vet_log_in, text="").pack()
 
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
    Label(vet_log_in, text="").pack()
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
    Label(vet_menu,text="").pack()
    Button(vet_menu,text="Update Account Info", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command =lambda:vet_update_button_clicked()).pack()
    Label(vet_menu,text="").pack()
    Button(vet_menu,text="Update Schedule Info", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = lambda:vet_update_schedule_clicked()).pack()
    Label(vet_menu,text="").pack()
    Button(vet_menu, text="Update Pet Info", width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = lambda:vet_update_pet_clicked()).pack()
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
    
    Button(vet_update_info, text='Submit', width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = vet_update_account).pack()
    Label(vet_update_info, text="").pack() 
    Button(vet_update_info, text="Return to Vet Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = vet_menu_launch).pack()

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
    Label(vet_update_info, text="").pack()
    label = Label(vet_update_info, text="Update Successful", fg="green", font="times 15")
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

   Button(vet_update_schedule, text='Submit', width=20, height=1, font="times 15", bd=20, bg="SpringGreen4", command = vet_update_schedule_info).pack()
   Label(vet_update_schedule, text="").pack()
   Button(vet_update_schedule, text="Return to Vet Menu", width=20, height=1, font='times 15', bd=20, bg='SpringGreen4', command = vet_menu_launch).pack()

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
    Label(vet_update_schedule, text="").pack()
    label = Label(vet_update_schedule, text="Update Successful", fg="green", font="times 15")
    label.pack()

#Allows vets to select a user and update specific pet information
def vet_update_pet_info():

    Label(vet_update_pet, text = "").pack()
    vet_update_pet_menu_label = Label(vet_update_pet, text = "Veterinarian Update Pet Menu", font = "times 15")
    vet_update_pet_menu_label.pack()

    query= "SELECT Concat(UserID, ', ', UserFirstName, ', ', UserLastName) FROM USERACCOUNTINFO"
                
    my_data = cursor.execute(query) # SQLAlchem engine result
    my_list = [r for r, in my_data] # create a  list 
    my_list2=[] 
    
    def my_upd(*args):
        cb2.set('') # remove the previous selected option
        selection = sel.get().split(", ")
        query = "SELECT Concat(PetID, ', ', PetName) FROM PetInfo WHERE UserID = '"+selection[0]+"'"
        my_data = cursor.execute(query) # SQLAlchem engine result
        my_list2 = [r for r, in my_data] # create a  list
        cb2['values']=my_list2    
          
    def vetUpdatePet(*args):        
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
        vet_pet_confirmation_des()
        cb1.set('')
        label = Label(vet_update_pet, text="Update Successful", fg="green", font="times 20")
        label.pack()
        
    def vet_pet_confirmation_popup():
        global vet_pet_confirmation
        vet_pet_confirmation = Toplevel(window)
        vet_pet_confirmation.title("Alert")
        vet_pet_confirmation.geometry("300x150")
        Label(vet_pet_confirmation, text=f'You selected {cb2.get()}.').pack()
        Button(vet_pet_confirmation, text="Update", command=vetUpdatePet).pack()
        Button(vet_pet_confirmation, text="No", command=vet_pet_confirmation_des).pack()    
     
    def vet_pet_confirmation_des():
        vet_pet_confirmation.destroy()
        
    sel=tk.StringVar()

    cb1 = ttk.Combobox(vet_update_pet, values=my_list,width=15,textvariable = sel)
    cb1.pack(padx=30,pady=30)

    sel.trace('w', my_upd)

    cb2 = ttk.Combobox(vet_update_pet, values=my_list2, width=15,)
    cb2.pack()
    
    pet_name_label = Label(vet_update_pet, text='Pet Name', font="times 15")
    pet_name_entry2 = Entry(vet_update_pet, font="times 20", width=20, textvariable=pet_name_var)
    pet_name_label.pack()
    pet_name_entry2.pack()

    pet_type_label = Label(vet_update_pet, text='Pet Type', font="times 15")
    pet_type_entry2 = Entry(vet_update_pet, textvariable=pet_type_var, font="times 20", width=20)
    pet_type_label.pack()
    pet_type_entry2.pack()

    pet_breed_label = Label(vet_update_pet, text='Pet Breed', font="times 15")
    pet_breed_entry2 = Entry(vet_update_pet, textvariable=pet_breed_var, font="times 20")
    pet_breed_label.pack()
    pet_breed_entry2.pack()

    pet_color_label = Label(vet_update_pet, text='Pet Color', font="times 15")
    pet_color_entry2 = Entry(vet_update_pet, textvariable=pet_color_var, font="times 20")
    pet_color_label.pack()
    pet_color_entry2.pack()

    Label(vet_update_pet, text="").pack()
    
    Button(vet_update_pet, text='Update Pet', width=20, height=1, font="times 20", bd=20, bg="SpringGreen4", command = vet_pet_confirmation_popup).pack()
    Label(vet_update_pet, text="").pack()
    Button(vet_update_pet, text="Return to Vet Menu", width=20, height=1, font='times 20', bd=20, bg='SpringGreen4', command = vet_menu_launch).pack()
###########################################################################################################################################################################

#Admin Log In
def admin_login():
    Label(admin_log_in, text="Please enter details below to login", font="times 50 bold", bg="SpringGreen4", anchor=N, pady=50).pack(fill=BOTH)
    Label(admin_log_in, text="").pack()
 
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
    Label(admin_log_in, text="").pack()
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
    Label(admin_menu,text="").pack()
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
    Label(admin_create_vet, text="").pack()
    username_label = Label(admin_create_vet, font='times 30', text="Username")
    username_label.pack()
    username_entry1 = Entry(admin_create_vet, font='times 30', textvariable=username4)
    username_entry1.pack()
    password_label = Label(admin_create_vet, font='times 30', text="Password")
    password_label.pack()
    password_entry1 = Entry(admin_create_vet, font='times 30', textvariable=password4, show='*')
    password_entry1.pack()
    Label(admin_create_vet, text="").pack()
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
    
    Label(admin_vet_dropdown, text = "").pack()
    admin_view_vet_menu_label = Label(admin_vet_dropdown, text = "View/Delete Veterinarians Menu", font = "times 15")
    admin_view_vet_menu_label.pack()

    query= "SELECT Concat(VetID, ', ', VetLoginID, ', ', VetFirstName, ', ', VetLastName) FROM VETACCOUNTINFO"
                
    my_data = cursor.execute(query) # SQLAlchem engine result
    my_list = [r for r, in my_data] # create a  list 
   
    sel=tk.StringVar()

    cb1 = ttk.Combobox(admin_vet_dropdown, values=my_list,width=15,textvariable = sel)
    cb1.pack(padx=30,pady=30)

    def admin_confirmation_popup():
        global admin_confirmation
        admin_confirmation = Toplevel(window)
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
        label = Label(admin_vet_dropdown, text ="Successfully deleted!")
        label.pack()
        cb1.set('')
        admin_confirmation_des()
    
    def admin_confirmation_des():
        admin_confirmation.destroy()
    
    #buttons
    Label(admin_vet_dropdown, text = "").pack()
    Button(admin_vet_dropdown, text="Delete Vet", width = 20, height = 1, font = 'times 20', bd = 20, bg = 'SpringGreen4', command = admin_confirmation_popup).pack()
    Label(admin_vet_dropdown, text = "").pack()
    Button(admin_vet_dropdown, text="Return to Admin Menu", width = 20, height = 1, font = 'times 20', bd = 20, bg = 'SpringGreen4', command = admin_menu_launch).pack()

####################################################################################################################################################################

# Main window on program start (loops until closed)
vetapp()
window.mainloop()