from tkinter import *
import os

pastaApp=os.path.dirname(__file__)

root = Tk()

img = PhotoImage(file="PRINCIPAL\LOGIN\Icon\logo.png")

label_imagem = Label(root, image=img).pack()




root.mainloop()