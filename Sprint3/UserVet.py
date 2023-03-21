from datetime import datetime
import tkinter as tk
from tkcalendar import Calendar
 
 
def updateLabel(event):
    label.config(text = "Selected Date: " + calendar.get_date())
 
root = tk.Tk()
 
calendar = Calendar(root, mindate = datetime(2020, 1, 1),
                          maxdate = datetime(2023, 12, 30),
                          showweeknumbers = False,
                          showothermonthdays = False,
                          background = "green",
                          foreground = "white",
                          selectbackground = "red", 
                          normalbackground = "lightgreen",
                          weekendbackground = "darkgreen",
                          weekendforeground = "white")
calendar.pack()
 
calendar.bind("<<CalendarSelected>>", updateLabel)
 
label = tk.Label(root, text = "Selected Date: ")
label.pack()
root.mainloop()