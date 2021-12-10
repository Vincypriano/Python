# grid manager

from tkinter import *

menu_principal = Tk()
menu_principal.title("AULA 20")
#menu_principal.geometry("500x300")

Label(menu_principal, width= 20, bg="red").grid(column=0)
Label(menu_principal, width= 20, bg="green").grid(column=1)
Label(menu_principal, width=40, bg="blue").grid(columnspan=2, sticky='we')


menu_principal.mainloop()