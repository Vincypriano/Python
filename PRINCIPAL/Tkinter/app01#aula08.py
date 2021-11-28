from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Centrar Screen")
#menu_inicial.geometry("500x300+450+250")

# Dimensões da janela
largura = 500
altura = 300

# Resolução do nosso sistema
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()

posx = int(largura_screen / 2 - largura/2)
posy = int(altura_screen /2 - altura/2)
menu_inicial.geometry("%dx%d+%d+%d" %(largura, altura, posx, posy))
print(posy,posx)

menu_inicial.mainloop()