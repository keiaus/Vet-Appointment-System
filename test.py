import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()
frame1 = Frame(root)
frame1.pack(expand=True)

frame2 = Frame(root)

usernameLabel = Label(frame2, text = "Email:")
usernameLabel.pack(padx = 0, pady = 0)

usernameInput = Entry(frame2)
usernameInput.pack()
usernameInput.focus_set()

passwordLabel = Label(frame2, text = "Password:")
passwordLabel.pack()

passwordInput = Entry(frame2, show = "*", width = 20)
passwordInput.pack()
passwordInput.focus_set()
# submitEmail = Button(frame2, text = "Submit", fg = "black", width = 10, command\
#  = callback)
# submitEmail.pack()

frame2.pack(anchor=CENTER)

frame3 = Frame(root)
frame3.pack(expand=True)

root.mainloop()