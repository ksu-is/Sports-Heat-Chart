from tkinter import *
from tkcalendar import *
import tkinter.messagebox

root = Tk()
space = " "
root.title(185 * space + "Sports Heat Chart")
root.geometry("1265x700+56+0")

MainFrame = Frame(root, bd = 10, width = 1245, height = 680, relief = RIDGE, bg = "gray")
MainFrame.pack()

TitleFrame = Frame(MainFrame, bd=7, width=1245, height=100, relief=RIDGE)
TitleFrame.pack()

TopFrame = Frame(MainFrame, bd=5, width=1245, height=500, relief=RIDGE)
TopFrame.pack()

RightFrameTop = Frame(TopFrame, bd=7, width=600, height=150, relief=RIDGE)
RightFrameTop.pack(side=RIGHT)
RightFrameBottom = Frame(TopFrame, bd=7, width=600, height=250, relief=RIDGE)
RightFrameTop.pack(side=TOP)



root.mainloop()