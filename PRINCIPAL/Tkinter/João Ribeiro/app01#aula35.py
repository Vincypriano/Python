from tkinter import *

root = Tk()
root.geometry("400x300")

t = Message(root, text="Este é o texto do message widget", width=100)
t.pack()

root.mainloop()