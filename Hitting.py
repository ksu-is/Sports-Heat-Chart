# Sports-Heat-Chart.py

from tkinter.ttk import Button
from numpy import *
from tkcalendar import *
from datetime import *
from tkinter import *
from pybaseball import batting_stats_range
from pybaseball import pitching_stats_range

#==============================================================================

#This is the Application window
root = Tk()
root.title("Sports Heat Chart")
root.geometry("800x295+56+0")
root.resizable(False, False)

#This is the main area within the application
MainFrame = Frame(root, bd = 10, width = 780, height = 190, relief = RIDGE, bg = "gray")
MainFrame.grid(row=0, column=0)

#This is the title frame where the main title, calender, dropdown box, and button resides 
TitleFrame = LabelFrame(MainFrame, bd=7, width=740, height=100, relief=RIDGE, text='Sports Heat Chart')
TitleFrame.grid(row=0, column=0, padx=245, pady=5)

#This is the frame that holds the stats
BottomFrame = Frame(MainFrame, bd=5, width=740, height=190, relief=RIDGE)
BottomFrame.grid(row=2, column=0)

#==============================================================================

#Calender 1 date selection
cal1 = DateEntry(TitleFrame, selectmode='day')

#Calender 2 date selection
cal2 = DateEntry(TitleFrame, selectmode='day') #date_pattern='yyyy-mm-dd'

#gui location for calender 1
cal1.grid(row=0,column=0,padx=15) 

#gui location for calender 2
cal2.grid(row=0,column=1,padx=15) 

#==============================================================================

# Dropdown box for hitting stat select
OPTIONS = [
"-",
"Hits",
"Home Runs",
"Doubles",
"Triples",
"Walks"
]

# Dropdown box for pitching stat select
OPTIONS2 = [
"-",
"Strikeouts",
"Wins",
"Innings Pitched",
]

#Variables for hitting dropdown box
variable = StringVar(TitleFrame)
variable.set(OPTIONS[0])

#Variables for pitching dropdown box
variable2 = StringVar(TitleFrame)
variable2.set(OPTIONS2[0])

#gui location for hitting dropdown box
w = OptionMenu(TitleFrame, variable, *OPTIONS)
w.grid(row=1, column=0)

#gui location for pitching dropdown box
w1 = OptionMenu(TitleFrame, variable2, *OPTIONS2)
w1.grid(row=1, column=1)

#==============================================================================

#defined variables for dropdown box
def selected():
    #Nothing selected
    if (variable.get() == "-") and (variable2.get() == "-"):
        mystat0 = Label(BottomFrame)
        mystat0.grid(row=0, column=0)
        return
    #Hits selected (Hitting)
    if (variable.get() == "Hits") and (variable2.get() == "-"):
        st = cal1.get_date().strftime('%Y-%m-%d') 
        ed = cal2.get_date().strftime('%Y-%m-%d')
        data = batting_stats_range(start_dt=st, end_dt=ed)
        sorted_d1 = data.sort_values(by='H', ascending=False)
        mystat1 = Label(BottomFrame, text=sorted_d1.head(5))
        mystat1.grid(row=0, column=0)
        return
    #Home Runs selected (Hitting)
    if (variable.get() == "Home Runs") and (variable2.get() == '-'):
        st = cal1.get_date().strftime('%Y-%m-%d') 
        ed = cal2.get_date().strftime('%Y-%m-%d')
        data = batting_stats_range(start_dt=st, end_dt=ed)
        sorted_d2 = data.sort_values(by='HR', ascending=False)
        mystat2 = Label(BottomFrame, text=sorted_d2.head(5))
        mystat2.grid(row=0, column=0)
        return
    #Doubles selected (Hitting)
    if (variable.get() == "Doubles") and (variable2.get() == '-'):
        st = cal1.get_date().strftime('%Y-%m-%d') 
        ed = cal2.get_date().strftime('%Y-%m-%d')
        data = batting_stats_range(start_dt=st, end_dt=ed)
        sorted_d3 = data.sort_values(by='2B', ascending=False)
        mystat3 = Label(BottomFrame, text=sorted_d3.head(5))
        mystat3.grid(row=0, column=0)
        return
    #Triples selected (Hitting)
    if (variable.get() == "Triples") and (variable2.get() == '-'):
        st = cal1.get_date().strftime('%Y-%m-%d') 
        ed = cal2.get_date().strftime('%Y-%m-%d')
        data = batting_stats_range(start_dt=st, end_dt=ed)
        sorted_d4 = data.sort_values(by='3B', ascending=False)
        mystat4 = Label(BottomFrame, text=sorted_d4.head(5))
        mystat4.grid(row=0, column=0)
        return
    #Walks selected (Pitching)
    if (variable.get() == "Walks") and (variable2.get() == '-'):
        st = cal1.get_date().strftime('%Y-%m-%d') 
        ed = cal2.get_date().strftime('%Y-%m-%d')
        data = batting_stats_range(start_dt=st, end_dt=ed)
        sorted_d5 = data.sort_values(by='BB', ascending=False)
        mystat5 = Label(BottomFrame, text=sorted_d5.head(5))
        mystat5.grid(row=0, column=0)
        return
    #Strikeouts selected (Pitching)
    if (variable.get() == "-") and (variable2.get() == "Strikeouts"):
        st = cal1.get_date().strftime('%Y-%m-%d') 
        ed = cal2.get_date().strftime('%Y-%m-%d')
        data = pitching_stats_range(start_dt=st, end_dt=ed)
        sorted_d6 = data.sort_values(by='SO', ascending=False)
        mystat6 = Label(BottomFrame, text=sorted_d6.head(5))
        mystat6.grid(row=0, column=0)
        return
    #Wins selected (Pitching)
    if (variable.get() == "-") and (variable2.get() == "Wins"):
        st = cal1.get_date().strftime('%Y-%m-%d') 
        ed = cal2.get_date().strftime('%Y-%m-%d')
        data = pitching_stats_range(start_dt=st, end_dt=ed)
        sorted_d7 = data.sort_values(by='W', ascending=False)
        mystat7 = Label(BottomFrame, text=sorted_d7.head(5))
        mystat7.grid(row=0, column=0)
        return
    #Innings Pitched selected (Pitching)
    if (variable.get() == "-") and (variable2.get() == "Innings Pitched"):
        st = cal1.get_date().strftime('%Y-%m-%d') 
        ed = cal2.get_date().strftime('%Y-%m-%d')
        data = pitching_stats_range(start_dt=st, end_dt=ed)
        sorted_d8 = data.sort_values(by='IP', ascending=False)
        mystat8 = Label(BottomFrame, text=sorted_d8.head(5))
        mystat8.grid(row=0, column=0)
        return

#==============================================================================

#Go button takes the date range and plugs it into statcast search
b2 = Button(TitleFrame, text='Go', command=selected)

#gui location for Go button
b2.grid(row=1, column=2)

#==============================================================================

root.mainloop()