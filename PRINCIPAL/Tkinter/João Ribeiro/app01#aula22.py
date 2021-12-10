
from tkinter import *
#-------------------------------------------------
#funções
def mostrarNome():
        vartexto.set("O seu nome é "+ textBox1.get().strip().capitalize())

#-------------------------------------------------
#GUI

root = Tk()
root.title("Aula 22")
root.geometry("500x250")

vartexto = StringVar()

#-------------------------------------------------
#widgets
label_1 = Label(root,
                text="O Seu nome é: ")
textBox1 = Entry(root)
btn_1 = Button(root, text="Executar", command=mostrarNome)
label_2 = Label(root, textvariable=vartexto)

#-------------------------------------------------
#layout

label_1.grid()
textBox1.grid()
btn_1.grid()
label_2.grid()





root.mainloop()