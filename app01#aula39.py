from tkinter import *

root = Tk()
root.title("Aula 39 TOP LEVEL")
root.geometry("300x200")



def open_form():
    #TOP LEVEL
    top_1 = Toplevel()
    top_1.title("Novo formulário")
    top_1.geometry("200x100")
    lb1 = Label(top_1, text="label na nova janela")
    lb1.pack()
    
btn = Button(root, text="Novo...", command=open_form)
btn.pack()
root.mainloop()