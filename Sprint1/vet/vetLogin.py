import tkinter as tk
from tkinter import *
from tkinter import ttk

# This file allows the veterinarian user to log in

root = tk.Tk()

root.title('Vet Log In')
root.geometry('800x1000')
title = ttk.Label(root, text='Vet Log In', font=('Arial', 18), border=10, relief=SOLID)
title.pack(padx=0, pady=14)

user_name_var = tk.StringVar()
password_var = tk.StringVar()

user_name_label = ttk.Label(root, text='Username', font=('calibre', 12, 'bold'))
user_name_entry = ttk.Entry(root, textvariable=user_name_var, font=('calibre', 10, 'normal'))
user_name_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
user_name_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

password_label = ttk.Label(root, text='Password', font=('calibre', 12, 'bold'))
password_entry = ttk.Entry(root, textvariable=password_var, font=('calibre', 10, 'normal'))
password_label.pack(padx=5, pady=5, side=tk.TOP, anchor=N)
password_entry.pack(padx=5, pady=5, side=tk.TOP, anchor=N, ipadx=30)

btn = Button(root, text="Log In", bd=7, command=root.destroy, font='Helevetica')
btn.pack(pady=40)

root.mainloop()