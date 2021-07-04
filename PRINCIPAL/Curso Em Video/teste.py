#from tkinter import *
#import pygame
import uuid 
#root = Tk()
#root.title('Codemy.com MP3 Player')
#root.iconbitmap('c:/gui/codemy.ico')
#root.geometry("500x300")
#print(uuid.uuid1())
frase = str(input('digite uma frase: '))
nova_string = ''
c = 0
while c < len(frase):
    if frase[c] == 'r':
        pass
    else:
        nova_string += frase[c]

    c += 1
print(nova_string)