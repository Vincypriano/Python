from tkinter import *

root = Tk()
root.title("Aula 38 MENU APP")
root.geometry("300x200")

menu_1 = Menu(root)

FileMenu = Menu(menu_1, tearoff=0)
FileMenu.add_command(label="New")
FileMenu.add_command(label="Open", command= lambda : "PRINCIPAL\Tkinter\João Ribeiro\app01#aula37.py")
FileMenu.add_command(label="Save")
FileMenu.add_separator()
FileMenu.add_command(label="Exit")
menu_1.add_cascade(label="File", menu=FileMenu)



menu_1.add_command(label="Edit")

root.config(menu=menu_1)

root.mainloop()