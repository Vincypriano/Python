from tkinter import *

root = Tk()
root.title("Aula 37 SPINBOX")
root.geometry("300x200")

s1 = Spinbox(root, from_=0, to=10)
s1.pack()

s2 = Spinbox(root, values=(10,20,30,40,50), wrap=True)
s2.pack()

s3 = Spinbox(root, values=("Vinicius", "Juliana", "João"))
s3.pack()

bnt = Button(root, text="Click", command= lambda : print(s2.get()))
bnt.pack()


root.mainloop()
