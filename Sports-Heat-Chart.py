# Sports-Heat-Chart.py

import tkinter as tk
from tkcalendar import DateEntry
screen = tk.Tk()
screen.geometry("900x600")
screen.title("Sports Heat Chart")
cal = DateEntry(screen,selectmode='day')
cal.grid(row=1,column=1,padx=15)

screen.mainloop()