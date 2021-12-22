'''
Listas em Python
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
'''
from random import randint
from typing import overload

text_1 = "Value"
list_1 = [1, 2, 3, 4, 'Vinicius', True, 10.5]
print(list_1[randint(0, len(list_1)-1)]) #Imprime indice de forma randomica
print(list_1[5])
list_1[5] = False #Troca de valores em list
print(list_1[5])
print(list_1[0:5:2]) #Fatiamento de List onde [inicio:fim:passo]
print(list_1[-1]) #Imprime último item da list
print(list_1[::-1]) #Imprime de forma invertada a list (serve para strings)

list_2 = ['Juliana','Corona', 'João', 1980, False, 2021, 3.1415 ]

print(list_1)
list_2.append('Stella') #comando append adiciona item ao final da lista
print(list_2)
list_3 = list_1 + list_2 # soma as listas em uma outra lista
print(list_3) 
print(len(list_3))
list_3.extend(list_1) #adiciona uma lista ao final
print(list_3[:15])
list_1.insert(2, 'a') #insere caracter "a" na posição desejada na lista ou qualquer coisa que quiser
print(list_1)
print(list_3)
list_3.pop() # deleta ultimo elemento da lista
print(list_3)
del(list_3[15:18]) # deleta indices nas listas
print(list_3)
list_4 = list(range(100,350,6)) # cria uma lista com os números interaveis em range
print(max(list_4)) #imprime maior valor numérico na lista (não funciona com boleanos nem strings)
print(min(list_4)) #imprime menor valor numérico na lista (não funciona com boleanos nem strings)
for valor in list_4:
    print(valor, end=' ')
    
list_5 = ['String', True, 10, -20.5]
for elem in list_5:
    print(f'\nO tipo de elemento é {type(elem)} e seu valor é {elem}')

secret = 'perfume'
digitadas = []
naovalidas = []

while True:
    letra = input('Digite uma letra: ')
    
    if len(letra) >1:
        print("Não vale digitar mais de uma letra...")
        continue
    
    digitadas.append(letra)

    if letra in secret:
        print(f'a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'A letra "{letra}" NÃO EXITE na palavra secreta.')
        naovalidas.append(letra)
        digitadas.pop()
        
    secret_temp = ''    
    for letra_secreta in secret:
        if letra_secreta in digitadas:
            secret_temp += letra_secreta
        else:
            secret_temp += "*"
            
    print(secret_temp)
    if secret_temp == secret:
        print('Você acertou a palavra secreta!!')
        break
print(f'foram digitadas {len(naovalidas)} letras inválidas.')
print("Fim!!")