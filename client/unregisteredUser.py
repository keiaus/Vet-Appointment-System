import tkinter as tk
from tkinter import *
from tkinter import ttk

# This file allows the unregistered user to sign up

root = tk.Tk()

root.title('Sign up')
root.geometry('800x1000')
title = ttk.Label(root, text='Sign Up', font=('Arial', 18), border=10, borderwidth=1, relief=SOLID)
title.pack(padx=0, pady=14)

# May have to use int(phone_number_entry.get()) to retrieve numeric values

user_name_var = tk.StringVar()
first_name_var = tk.StringVar()
last_name_var = tk.StringVar()
email_var = tk.StringVar()
phone_number_var = tk.StringVar()
street_address_var = tk.StringVar()
city_var = tk.StringVar()
state_var = tk.StringVar()
zip_var = tk.StringVar()
password1_var = tk.StringVar()
password2_var = tk.StringVar()

first_name_label = ttk.Label(root, text='First Name', font=('calibre', 12, 'bold'))
first_name_entry = ttk.Entry(root, textvariable=first_name_var, font=('calibre', 10, 'normal'))
first_name_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
first_name_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

last_name_label = ttk.Label(root, text='Last Name', font=('calibre', 12, 'bold'))
last_name_entry = ttk.Entry(root, textvariable=last_name_var, font=('calibre', 10, 'normal'))
last_name_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
last_name_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

user_name_label = ttk.Label(root, text='Username', font=('calibre', 12, 'bold'))
user_name_entry = ttk.Entry(root, textvariable=user_name_var, font=('calibre', 10, 'normal'))
user_name_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
user_name_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

email_label = ttk.Label(root, text='Email', font=('calibre', 12, 'bold'))
email_entry = ttk.Entry(root, textvariable=email_var, font=('calibre', 10, 'normal'))
email_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
email_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

phone_number_label = ttk.Label(root, text='Phone Number', font=('calibre', 12, 'bold'))
phone_number_entry = ttk.Entry(root, textvariable=phone_number_var, font=('calibre', 10, 'normal'))
phone_number_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
phone_number_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

street_address_label = ttk.Label(root, text='Street Address', font=('calibre', 12, 'bold'))
street_address_entry = ttk.Entry(root, textvariable=street_address_var, font=('calibre', 10, 'normal'))
street_address_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
street_address_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

city_label = ttk.Label(root, text='City', font=('calibre', 12, 'bold'))
city_entry = ttk.Entry(root, textvariable=city_var, font=('calibre', 10, 'normal'))
city_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
city_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

state_label = ttk.Label(root, text='State', font=('calibre', 12, 'bold'))
state_entry = ttk.Entry(root, textvariable=state_var, font=('calibre', 10, 'normal'))
state_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
state_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

zip_label = ttk.Label(root, text='Zip Code', font=('calibre', 12, 'bold'))
zip_entry = ttk.Entry(root, textvariable=zip_var, font=('calibre', 10, 'normal'))
zip_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
zip_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

password1_label = ttk.Label(root, text='Password', font=('calibre', 12, 'bold'))
password1_entry = ttk.Entry(root, textvariable=password1_var, font=('calibre', 10, 'normal'))
password1_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
password1_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

password2_label = ttk.Label(root, text='Confirm Password', font=('calibre', 12, 'bold'))
password2_entry = ttk.Entry(root, textvariable=password2_var, font=('calibre', 10, 'normal'))
password2_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
password2_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

btn = Button(root, text="Sign Up", bd=7, command=root.destroy, font='Helevetica')
btn.pack(pady=40)

root.mainloop()