# Create a program with A Digital Clock

from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title("DIGITAL CLOCK")


def get_time():
    timevar = time.strftime("%I:%M:%S %p")
    clock.config(text = timevar)
    clock.after(200,get_time)

Label(master, font =("Arial", 30), text = "Digital CLock", fg ="white", bg="black").pack()
clock = Label(master, font =("Arial", 100), bg ="black", fg = "green")
clock.pack()

get_time()

master.mainloop()