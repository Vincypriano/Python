from tkinter import *

root = Tk()
root.geometry("300x200")



slide = Scale(root, 
              from_=0, 
              to=100, 
              orient=HORIZONTAL, 
              resolution=0.5,
              command=lambda v: print(v))
slide.pack()

btn = Button(root, text="Ver Valor", command= lambda : print(slide.get()))
btn.pack()


root.mainloop()