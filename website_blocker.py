print("Website Blocker ............ ")

from tkinter import *
import tkinter as tk

window = Tk()
window.geometry('500x300')
window.resizable(0,0)
window.title("Website Blocker")

Label(window, text = "Welcome to website blocker", font='arial 20 bold', bg='blue').pack()
Label(window, text = "OK THEN !!!!!!!! LET'S GO").pack(side=BOTTOM)
#Entry widget
Label(window, text = "Enter Website ").place(x = 35, y = 80)
webs = Text(window, height='2', width='30', wrap = WORD)
webs.place(x = 200, y = 80)

host_file = 'C:\hosts.txt'
ip_add = '127.0.0.1'

def blocker():
    web_lists = webs.get(1.0,END)
    print(web_lists)
    web = list(web_lists.split(","))
    print(web)

    with open(host_file, 'r+') as file:
        file_content = file.read()
        for w in web:
            if w in file_content:
                Label(window, text="Already Blocked",).place(x = 50, y = 130)

            else:
                file.write(ip_add + " " + w + '\n')
                Label(window, text=" Blocked").place(x=50, y=130)




block = Button(window, text = 'Block',font = 'arial 12 bold',pady = 5,command = blocker ,width = 6, bg = 'royal blue1', activebackground = 'sky blue')
block.place(x = 230, y = 150)
window.mainloop()

