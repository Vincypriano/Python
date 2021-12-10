from tkinter import *

menu_inicial = Tk()
menu_inicial.title("AULA 15")
menu_inicial.geometry("500x300",)

label_1 = Label(menu_inicial,
                text="Texto Label_1",
                foreground= "blue",
                relief="raised",
                cursor="watch"
                
                )

label_1.pack()

btn = Button(menu_inicial,
             text="BOTÃO TESTE",
             activebackground="black",
             activeforeground="yellow",
             bd=4,
             font="Times",
             cursor="heart",
             highlightcolor="red")
btn.pack()
for item in label_1.keys():
    print(item, " : ", label_1[item])

menu_inicial.mainloop()








