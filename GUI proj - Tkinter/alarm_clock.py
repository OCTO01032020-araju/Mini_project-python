from tkinter import *
import tkinter as tk
import time

window = Tk()

window.resizable
Label(window, text="Alarm Clock........" , bg='blue').place(x= 50, y = 20)

def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    current_time.config(text = clock_time)
    current_time.after(1000,clock)

current_time = Label(window, text="Current Time").place(x = 50, y = 100)

clock()

window.mainloop()