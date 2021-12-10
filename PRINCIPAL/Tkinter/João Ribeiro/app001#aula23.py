
from tkinter import *

#-------------------------------
#funções
# C = (F-32) * 5/9
def MudarCelsius():
    F = float(textBox_1.get())    
    C = (F -32) * 5/9
    final.set(str(round(C,2)) + "°C")

#-------------------------------
#GUI

root = Tk()
root.title("Aula 23")

final = StringVar()

#---------------------------------
#Widgets
label_1 = Label(root, text="Inserir Fahrenheit:")
textBox_1 = Entry(root)
btn_1 = Button(root, text="Executar",command=MudarCelsius)
label_result = Label(root,textvariable=final)


#------------------------------------
#Layout
label_1.grid()
textBox_1.grid()
btn_1.grid()
label_result.grid()


root.mainloop()