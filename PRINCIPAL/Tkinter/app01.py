from tkinter import *

menu_inicial = Tk() # Cria a janela com método da biblioteca Tkinter
menu_inicial.title('First App') # Muda nome na barra de cima do programa
menu_inicial['bg'] = "black"


menu_inicial.geometry("500x250+350+250") # Define as dimesões da aplicação e posição na tela
menu_inicial.resizable(width= True, height= True) # Define se a tela pode ser redimensionada ou não (booleano)
menu_inicial.iconbitmap("icon.ico") # Muda o Icone do canto esquerdo da tela

'''menu_inicial.minsize(width= 500, height= 250) # Define tamanho minimo da Janel
menu_inicial.maxsize(width= 700, height= 400) # Define tamanho maximo da Janela'''

menu_inicial.state("zoomed") # Define o estado da tela 'zoomed' maximizado e 'iconic' minimizado

def btn_Click(msg):
    print(msg)

#Botton
btn = Button(menu_inicial, text= "Executar", command=lambda: btn_Click("Nova Mensagem")) # Cria e mostra nome do botão
btn.pack() # Define se o botão apareçe na tela

cmd = Button(menu_inicial, text= "Clicar", command=lambda: btn_Click("ok") )
cmd.pack()    
menu_inicial.mainloop() # Cria um loop que permite a janela permanecer aberta