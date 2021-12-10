from tkinter import *
#-------------------------------------
#funções

def executar():
    l1['text'] = t_1.get()
    l2['text'] = t_2.get()
    l3['text'] = t_3.get()
    
#-------------------------------------
#GUI

root = Tk()
root.title("Aula 24")


#-------------------------------------
#Widgets

t_1 = Entry(root)
t_2 = Entry(root)
t_3 = Entry(root)
l1 = Label(root)
l2 = Label(root)
l3 = Label(root)
btn = Button(root, text="Executar",command=executar)
#------------------------------------
#layout

t_1.grid()
t_2.grid()
t_3.grid()

l1.grid()
l2.grid()
l3.grid()

btn.grid()

t_1.focus()


root.mainloop()