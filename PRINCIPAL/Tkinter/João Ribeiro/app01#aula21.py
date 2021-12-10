# exercicio 01

from tkinter import *

#----------------------------------------------------------
#Funções

def mostrarNome():
    nome = textBox_1.get().strip().capitalize()
    label_final = Label(root, text="O teu nome é " + nome)
    label_final.grid()
    
#-----------------------------------------------------------    
# GUI
root = Tk()
root.title("AULA 21")
root.geometry("200x100")

# Criar Widgets

label_1 = Label(root, text="Digite seu nome:")

textBox_1 = Entry(root)

bnt_1 = Button(root,text="Executar", command= mostrarNome)

# Organização das grids
label_1.grid()

textBox_1.grid()

bnt_1.grid()

root.mainloop()