from tkinter import *

#====================================
#Functions 

class MyFrame(Frame):
    def __init__(self, parent):
        super().__init__()
        self['height'] = 200
        self['width'] = 400
        self['bg'] = "green"

#=====================================
#GUI

root = Tk()

#=====================================
#widget

frm1 = MyFrame(root)
frm2 = MyFrame(root)

#=======================================
#layout

frm1.grid()
frm2.grid()

root.mainloop()