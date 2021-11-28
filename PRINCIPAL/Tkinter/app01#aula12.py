from tkinter import *
from tkinter.font import Font

screen_princ = Tk()
screen_princ.title("AULA 13")
screen_princ.geometry("500x300")

label_1 = Label(
    screen_princ,
    text="FRASE DE TESTES",
    font="Arial 20",
    bd=1,
    relief="solid",
    width=25,
    height=2,
    anchor=CENTER   
).pack()

screen_princ.mainloop()