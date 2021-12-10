from tkinter import*

#------------------------------------
# My Widget

class FramName(Frame):
    def __init__(self, mymaster):
        super().__init__()
        self['height'] = 150
        self['width'] = 200
        self['bd'] = 2
        self['relief'] = "solid"
        
        label_nome = Label(self, text="Nome: ")
        text_nome = Entry(self)
        label_nome.grid(row=0, column=0)
        text_nome.grid(row=0, column=1)

#------------------------------------
#GUI

root = Tk()
root.title("AULA 27")


##------------------------------------
#Widget

frame_name_1 = FramName(root).grid()
frame_name_2 = FramName(root).grid()


root.mainloop()