from tkinter import *


#-------------------------------------
#funções

#def logIn():




#--------------------------------------
#GUI

root = Tk()
root.title("AULA 25")

#--------------------------------------
#widgets

frame_login = Frame(root)

label_usúario = Label(frame_login, text="Usuário: ")
label_password = Label(frame_login, text="Password: ")
text_usuário = Entry(frame_login)
text_password = Entry(frame_login)
cmd_entrar  = Button(frame_login, text="ENTRAR")

frame_login.grid()


#-------------------------------------
#layout

label_usúario.grid(row=0, column=0)
label_password.grid(row=1, column=0)
text_usuário.grid(row=0, column=1)
text_password.grid(row=1, column=1)
cmd_entrar.grid(row=2, column=1)

root.mainloop()