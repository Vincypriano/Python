from tkinter import *
from tkinter import font
'''PADDING E JUSTIFICAÇÃO DE TEXTO NUM LABEL'''
menu_principal = Tk()
menu_principal.title("AULA 14")
menu_principal.geometry("400x300+300+250")

#Label
label_1 = Label(
    menu_principal,
    text="frase de testes\noutra frase de testes".upper(),
    bd=3,
    relief="solid",
    background="black",
    fg="yellow",    
    font="Times 15",
    padx=10,
    pady=5,
    width=30,
    height=3,
    justify=LEFT,
    anchor=NW
).pack()



menu_principal.mainloop()