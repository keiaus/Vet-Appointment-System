import tkinter as tk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, ttk
from tkcalendar import DateEntry
import os

# path to widget images (button images and text area images)
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(os.path.abspath('widget_images'))
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# window
window = Tk()
window.geometry("1440x1024")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=1024,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
# Nav bar
# Nav Bar Frame
canvas.place(x=0, y=0)
canvas.create_rectangle(
    1.0,
    1.0,
    1441.0,
    101.0,
    fill="#FFFFFF",
    outline="")

# New Appointment Button

new_appointment_button_img = PhotoImage(
    file=relative_to_assets("new_appointment_btn.png"))
new_appointment_button = Button(
    image=new_appointment_button_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("new appointment button clicked"),
    relief="flat"
)
new_appointment_button.place(
    x=23.0,
    y=57.0,
    width=200.0,
    height=35.0
)

# -----------------------------------------------------------------
# appointment search
appointment_search_img = PhotoImage(
    file=relative_to_assets("appointment_search_holder.png"))
appointment_search_bg = canvas.create_image(
    796.0,
    76.0,
    image=appointment_search_img
)


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


appointment_list = ['Search existing appointments', 'Appointment date and time - Pet Owner Name - Pet Name ..']
appointment_dropdown = ttk.Combobox(window, values=appointment_list)
appointment_dropdown.current(0)
appointment_dropdown.pack()
appointment_dropdown.bind('KeyRelease', appointment_search)
appointment_dropdown.place(
    x=606.0,
    y=57.0,
    width=380.0,
    height=36.0
)
# -----------------------------------------------------------------

# vet dashboard button
vet_dashboard_button_image = PhotoImage(
    file=relative_to_assets("vet_dashboard_btn.png"))
vet_dashboard_button = Button(
    image=vet_dashboard_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("vet dashboard button clicked"),
    relief="flat"
)
vet_dashboard_button.place(
    x=1063.0,
    y=57.0,
    width=140.0,
    height=35.0
)
# -----------------------------------------------------------------

# logout button
logout_button_image = PhotoImage(
    file=relative_to_assets("logout_btn.png"))
logout_button = Button(
    image=logout_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("logout button clicked"),
    relief="flat"
)
logout_button.place(
    x=1270.0,
    y=57.0,
    width=120.0,
    height=35.0
)
# End of Nav Bar
# -----------------------------------------------------------------

# Create new appointment frame
canvas.create_rectangle(
    319.0,
    217.0,
    1119.0,
    807.0,
    fill="white",
    outline="black")

canvas.create_text(
    333.0,
    227.0,
    anchor="nw",
    text="Create New Appointment",
    fill="#000000",
    font=("Alata Regular", 16 * -1)
)
# -----------------------------------------------------------------

# -- Date --
canvas.create_text(
    329.0,
    653.0,
    anchor="nw",
    text="Date",
    fill="#000000",
    font=("Alata Regular", 12 * -1)
)
date_dropdown = DateEntry(window,
                          borderwidth=0,
                          highlightthickness=0,
                          relief="flat",
                          selectmode='day')

date_dropdown.place(
    x=329.0,
    y=669.0,
    width=200.0,
    height=40.0,

)
# -----------------------------------------------------------------

# -- Time --
canvas.create_text(
    562.0,
    653.0,
    anchor="nw",
    text="Time",
    fill="#000000",
    font=("Alata Regular", 12 * -1)
)
time_list = []
time_value = tk.StringVar()
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


time_listbox = ttk.Spinbox(window, values=time_list, textvariable=time_value, command=display_time, state='readonly')

text = f"Selected Time:  {str(time_listbox.get())}"
label = tk.Label(window, text=text)
label.pack()
label.place(x=562.0, y=720.0)
time_value.set(time_list[0])

time_listbox.place(
    x=562.0,
    y=669.0,
    height=40.0,
    width=200.0
)
# -----------------------------------------------------------------

# -- Duration --
canvas.create_text(
    795.0,
    653.0,
    anchor="nw",
    text="Duration",
    fill="#000000",
    font=("Alata Regular", 12 * -1)
)
duration_list = []
duration_value = tk.StringVar()
for duration_time in range(5, 61, 5):
    duration_list.append(f"{duration_time} Minutes")

duration_dropdown = ttk.Combobox(window, values=duration_list, state='readonly')
duration_dropdown.set(duration_list[0])

duration_dropdown.place(
    x=795.0,
    y=669.0,
    width=200.0,
    height=40.0
)
# -----------------------------------------------------------------

# -- End Time --
canvas.create_text(
    1028.0,
    653.0,
    anchor="nw",
    text="End Time",
    fill="#000000",
    font=("Alata Regular", 12 * -1))


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

    return end_time_str


# prints to console at the moment
end_time_calculation = Button(window,
                              borderwidth=0,
                              highlightthickness=0,
                              relief="ridge",
                              overrelief="ridge",
                              command=lambda: print(calc_end_time()),
                              background="green",
                              text="click"
                              )
end_time = f"{calc_end_time()}"
end_label = tk.Label(window, text=end_time)
end_label.pack()
end_label.place(x=1028.0, y=750.0)
end_time_calculation.place(
    x=1028.0,
    y=669.0,
    width=81.0,
    height=40.0
)
# -----------------------------------------------------------------

# -- Reason for visit --
canvas.create_text(
    329.0,
    427.0,
    anchor="nw",
    text="Reason For Visit",
    fill="#000000",
    font=("Alata Regular", 12 * -1)
)
reason_for_visit_img = PhotoImage(
    file=relative_to_assets("reason_for_visit_holder.png"))
reason_for_visit_img_bg = canvas.create_image(
    721.0,
    521.0,
    image=reason_for_visit_img
)
reason_for_visit_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
reason_for_visit_entry.place(
    x=329.0,
    y=444.0,
    width=784.0,
    height=152.0
)
# -----------------------------------------------------------------

# -- Appointment Type --
canvas.create_text(
    329.0,
    349.0,
    anchor="nw",
    text="Appointment Type",
    fill="#000000",
    font=("Alata Regular", 12 * -1)
)

appointment_type_img = PhotoImage(
    file=relative_to_assets("appointment_type_holder.png"))
appointment_type_bg = canvas.create_image(
    429.0,
    389.0,
    image=appointment_type_img
)
appointment_type_list = ['New Client Visit', 'Sick Visit', 'Follow-up Visit', 'Routine Wellness Exam', 'Vaccinations',
                         'Emergency/Urgent Care', 'Surgical Consultation', 'Euthanasia']
appointment_type_dropdown = ttk.Combobox(window, values=appointment_type_list)
appointment_type_dropdown.current(0)
appointment_type_dropdown.pack()

appointment_type_dropdown.place(
    x=329.0,
    y=369.0,
    width=200.0,
    height=40.0
)
# -----------------------------------------------------------------

# -- Patient Search --
patient_search_img = PhotoImage(
    file=relative_to_assets("patient_search_holder.png"))
patient_search_bg = canvas.create_image(
    529.0,
    318.0,
    image=patient_search_img
)


def patient_search(event):
    patient_search_value = event.widget.get()
    if patient_search_value == '':
        patient_dropdown['values'] = patient_names
    else:
        data = []

        for patient in patient_names:
            if patient_search_value.lower() in patient.lower():
                data.append(patient)
        patient_dropdown['values'] = data


patient_names = ['Search owner name, phone, email, or add new patient', 'patient_1', 'patient_2', 'patient_3']
patient_dropdown = ttk.Combobox(window, values=patient_names)
patient_dropdown.current(0)
patient_dropdown.pack()
patient_dropdown.bind('KeyRelease', patient_search)

patient_dropdown.place(
    x=329.0,
    y=298.0,
    width=400.0,
    height=40.0
)
# -----------------------------------------------------------------

# -- Veterinarian search --
# drop down to select veterinarian
# veterinarian_var = tk.StringVar()
veterinarian_search_img = PhotoImage(
    file=relative_to_assets("veterinarian_search.png"))
veterinarian_search_bg = canvas.create_image(
    1014,
    318.0,
    image=veterinarian_search_img
)
veterinarian_names = ['firstname lastname', 'lastname, firstname']
veterinarian_dropdown = ttk.Combobox(window, values=veterinarian_names, state='readonly')
veterinarian_dropdown.set('Select veterinarian')
veterinarian_dropdown.place(x=913.0, y=298.0, height=40, width=200)

canvas.create_text(
    329.0,
    278.0,
    anchor="nw",
    text="Patient",
    fill="#000000",
    font=("Alata Regular", 12 * -1)
)

veterinarian_dropdown_label = canvas.create_text(
    913.0,
    278.0,
    anchor="nw",
    text="Veterinarian",
    fill="#000000",
    font=("Alata Regular", 12 * -1)
)
# -----------------------------------------------------------------

# Save Button
save_button_image = PhotoImage(
    file=relative_to_assets("save_btn.png"))
save_button = Button(
    image=save_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("save button clicked"),
    relief="flat"
)
save_button.place(
    x=913.0,
    y=751.0,
    width=200.0,
    height=35.0
)
# Cancel Button
cancel_button_image = PhotoImage(
    file=relative_to_assets("cancel_btn.png"))
cancel_button = Button(
    image=cancel_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("cancel button clicked"),
    relief="raised",
    highlightcolor="black"
)
cancel_button.place(
    x=330.0,
    y=751.0,
    width=200.0,
    height=35.0
)
# -----------------------------------------------------------------
window.resizable(True, True)
window.mainloop()
