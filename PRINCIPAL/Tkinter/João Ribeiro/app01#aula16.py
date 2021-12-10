from tkinter import *

menu_inicial = Tk()
menu_inicial.title("AULA 16")
menu_inicial.geometry("500x300")

texto = StringVar()
texto.set("Novo Texto")

label_1 = Label(menu_inicial,
                text=texto,         # Atribui a localização da variavel, não o valor
                font="Times 20",
                bg="yellow")

label_2 = Label(menu_inicial,
                textvariable=texto, # Atribui o valor da variável.
                font="Arial 20",
                bg='red',
                fg="white")

label_1.pack()
label_2.pack()



menu_inicial.mainloop()