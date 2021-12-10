from tkinter import *

class MyFrame(Frame):
    def __init__ (self, parent):
        super().__init__()
        
        self["bd"] = 5
        self["relief"] = "raised"
        self["cursor"] = "watch"
        
        self.label_1_text = StringVar()
        self.text_1_text = StringVar()
        
        #widgets
        
        self.label_1 = Label(self, textvariable= self.label_1_text).grid()
        text_1 = Entry(self,textvariable = self.text_1_text).grid()
        btn_1 = Button(self, text="Clique", command=self.Execute).grid()
        
    def Execute(self):    
        self.label_1_text.set("Hello, " + self.text_1_text.get().capitalize() + ".")
        
root = Tk()
root.geometry("300x150")

frm1 = MyFrame(root).grid()

root.mainloop()