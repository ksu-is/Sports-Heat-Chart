# Sports-Heat-Chart.py

import tkinter as tk
from tkinter.ttk import Button
from tkcalendar import DateEntry
import numpy as np
import pandas as pd
import pybaseball as bb
from pybaseball import statcast
from pybaseball import batting_leaders

root = tk.Tk()
root.geometry("300x150")
root.title("Sports Heat Chart")

# data for date range
def data():
    data = statcast(start_dt= date, end_dt= date2)

# allows user to select start date
cal = DateEntry(root,selectmode='day')
cal.grid(row=1,column=1,padx=15)
def date():
    start_dt=cal.get_date()

# allows user to selct end date    
cal2 = DateEntry(root,selectmode='day')
cal2.grid(row=1,column=2,padx=15)
def date2():
    end_dt=cal2.get_date()

# Go button takes the date range and plugs it into statcast search
b1 = Button(root, text='Go', command=data)
b1.grid(row=2, column=2, padx=10)


root.mainloop()