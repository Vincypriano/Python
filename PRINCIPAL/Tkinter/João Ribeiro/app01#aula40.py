from tkinter import *

root = Tk()
root.title("Aula 40 PYINSTALLER")
root.geometry("300x200")


text_1 = StringVar()
text_1.set("")

label_1 = Label(root, textvariable=text_1)
label_1.pack()

def executar():
    text_1.set("Texto Alterado")
    
root.mainloop()