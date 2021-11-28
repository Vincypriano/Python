from tkinter import *
from tkinter import font

menu_inicial = Tk()
menu_inicial.title("Titulo")
menu_inicial.geometry("500x300")

# Labels
label_1 = Label(menu_inicial, 
                text = "Este é o label 1.RAISED\nEste é o label 1 numa nova linha",
                relief="raised",
                bd=10,
                bg="#f10000",
                fg="black",
                font="Verdana 20 overstrike",
                width=30,
                height=3
                )

label_2 = Label(menu_inicial, 
                text= "Este é o label 2. SUNKEN",
                relief="sunken",
                bd=6,
                fg="blue",
                font="Times 15 underline")

label_3 = Label(menu_inicial, 
                text= "Este é o label 3. FLAT",
                relief="flat",
                bd=6,
                fg="blue",
                font="Times ")

label_4 = Label(menu_inicial, 
                text= "Este é o label 4. GROOVE",
                relief="groove",
                bd=6,
                fg="blue",
                font="Times")

label_5 = Label(menu_inicial, 
                text= "Este é o label 5. SOLID",
                relief="solid",
                bd=6,
                fg="blue",
                font="Times")

label_6 = Label(menu_inicial, 
                text= "Este é o label 6. RIDGE",
                relief="ridge",
                bd=6,
                fg="blue",
                font="Times")

btn = Button(menu_inicial, 
             text="Executar",
             relief="raised",
             bd=4,
             bg="#aa0000",
             fg="black",
             font="Arial 20 bold italic underline",)


# Pack
label_1.pack()
label_2.pack()
label_3.pack()
label_4.pack()
label_5.pack()
label_6.pack()
btn.pack()

menu_inicial.mainloop()