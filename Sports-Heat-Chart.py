# Sports-Heat-Chart.py

import tkinter as tk
from tkcalendar import DateEntry
import numpy as np
import pandas as pd
import pybaseball as bb

screen = tk.Tk()
screen.geometry("900x600")
screen.title("Sports Heat Chart")

cal = DateEntry(screen,selectmode='day')
cal.grid(row=1,column=1,padx=15)
def date():
    dt=cal.get_date()
    str=dt.strftime('%m-%d-%y')

screen.mainloop()