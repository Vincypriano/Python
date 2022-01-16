num = 11

print('Par') if num % 2 == 0 else print('Impar')

from random import randrange
lista = [randrange(-1000,1000) for i in range(10)]
lista_2 = ['Saque' if i > 0 else 'Depósito' for i in lista]
print(lista_2)