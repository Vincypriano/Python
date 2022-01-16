from random import randint

lista = list()
lista_2 = []
lista_3 = []
for i in range (0,20):
    lista.append(randint(0,10))
print(lista)

# list comprehension 
[(lista_2.append(randint(0,10)))for i in range(20)]
print(lista_2)
[i for i in range(20)]
print([_**2 for _ in range(20)])

[lista_3.append(num) for num in lista if num % 2 == 0]
print(lista_3)

var = 'P4yth)on] &l@ang**uage'
var_3 = [i for i in var if i.isalpha() or i.isspace()]
print(''.join(var_3))

from datetime import datetime

datas_string = ['01/08/2021', '17/08/2000', '04/05/1997', '31/01/2000', '26/10/2010']

dt_str = [datetime.strptime(i, '%d/%m/%Y') for i in datas_string]
dt_str.sort()
print(type(dt_str))


