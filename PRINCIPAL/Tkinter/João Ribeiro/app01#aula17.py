# GRID MANAGER

from tkinter import *
from typing import Collection

menu_principal = Tk()
menu_principal.title("AULA 17")
menu_principal.geometry("500x500")

label_1 = Label(menu_principal,
                text="Label 1",
                font="Times 20",
                bg="red")

label_2 = Label(menu_principal,
                text="Label 2",
                font="Arial 20",
                bg="green")

label_3 = Label(menu_principal,
                text="Label 3",
                font="Verdana 20",
                bg="blue")

btn1 = Button(menu_principal, text="Click 1")
btn2 = Button(menu_principal, text="Click 2")
btn3 = Button(menu_principal, text="Click 3")

label_1.grid(row=0, column=0)
label_2.grid(row=0, column=1)
label_3.grid(row=0, column=2)

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)
menu_principal.mainloop()