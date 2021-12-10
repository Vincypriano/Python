# grid manager

from tkinter import *

root = Tk()
root.title("LOGIN")

Label(root, text="Usuário:").grid(row=0,sticky=W)
Label(root, text="Senha:").grid(row=1, sticky=W)

textBox1 = Entry(root).grid(row=0, column=1)
textBox2 = Entry(root).grid(row=1, column=1)

btn_login = Button(root, text="LOGIN").grid(row=2, column=1, sticky=E)

root.mainloop()