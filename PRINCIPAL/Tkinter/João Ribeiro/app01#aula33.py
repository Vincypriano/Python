from tkinter import *

root = Tk()

lista = Listbox(root, selectmode=EXTENDED)
lista.pack()

#inserir um item de cada vez

lista.insert(END, "Primeiro item da lista")
lista.insert(END, "Segundo item da lista")

#inserir varios itens a partir de uma list

nomes = ['Vinicis', 'Juliana','Nice', 'João']
for nome in nomes:
    lista.insert(END, nome)
    
btn = Button(root, text="Clique", command=lambda : print(lista.get(ACTIVE))).pack()
#lista.delete(0,0)

root.mainloop()