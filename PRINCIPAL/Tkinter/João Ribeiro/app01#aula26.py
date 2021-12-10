from tkinter import *
from typing import Collection

#----------------------------------
#Funções



#----------------------------------
#GUI
root = Tk()
root.title("AULA26")


#----------------------------------
#widgets
frame_1 = Frame(root)

label_1 = Label(frame_1, text="NOME: ")
label_2 = Label(frame_1, text="SOBRENOME: ")
text_box1 = Entry(frame_1)
text_box2 = Entry(frame_1)

frame_2 = Frame(root)

label_3 = Label(frame_2, text="ENDEREÇO: ")
label_4 = Label(frame_2, text="CIDADE: ")
text_box3 = Entry(frame_2)
text_box4 = Entry(frame_2)

btn = Button(root, text="SALVAR")
#-----------------------------------
#layout

label_1.grid(row=0, column=0)
label_2.grid(row=1, column=0)
text_box1.grid(row=0, column=1)
text_box2.grid(row=1, column=1)

label_3.grid(row=0, column=0)
label_4.grid(row=1, column=0)
text_box3.grid(row=0, column=1)
text_box4.grid(row=1, column=1)

frame_1.grid(row=0, column=0)
frame_2.grid(row=0, column=1)

btn.grid()

root.mainloop()
