import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()

root.title('Sign up')
root.geometry('800x800')
title = ttk.Label(root, text='Sign Up', font=('Arial', 18))
title.pack(padx=20, pady=20)

user_name_var = tk.StringVar()
first_name_var = tk.StringVar()
last_name_var = tk.StringVar()
email_var = tk.StringVar()
phone_number_var = tk.IntVar()
street_address_var = tk.StringVar()
city_var = tk.StringVar()
state_var = tk.StringVar()
zip_var = tk.IntVar()

first_name_label = ttk.Label(root, text='First Name', font=('calibre', 12, 'bold'))
first_name_entry = ttk.Entry(root, textvariable=user_name_var, font=('calibre', 10, 'normal'))
first_name_label.pack(side=TOP)
first_name_entry.pack(side=TOP, anchor=NE)

root.mainloop()