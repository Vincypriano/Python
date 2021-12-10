from tkinter import *

root = Tk()

def show():
    print(valor_check.get())
#---------------------
#checkButton

valor_check = IntVar()
check = Checkbutton(
    root,
    text="Esta é uma CheckBox",
    variable=valor_check,
    command=lambda : print(valor_check.get())
    ).pack()

valor_check = IntVar()
check = Checkbutton(
    root,
    text="Esta é outra CheckBox",
    variable=valor_check,
    command=show
    ).pack()

root.mainloop()