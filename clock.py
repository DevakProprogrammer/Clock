#things to import (make sure to have pip)
from cProfile import label
import imp
from logging import root
import string
from tkinter import *
from tkinter import font
from tkinter.ttk import  *
from time import strftime

root = Tk()
root.title("Clock")

#format of time in 12 hours to change it write (''%H:%M:%S %p) instead of ('%I:%M:%S %p')
def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

#designing
label = Label(root, font=("DS-DIGITAL", 80), background = "black", foreground = "cyan")
label.pack(anchor = 'center')

time()

mainloop()