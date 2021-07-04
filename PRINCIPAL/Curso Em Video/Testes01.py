#saque = int(input('Digite o Valor a ser sacado: R$ '))
#print(saque//50, saque / 50, saque % 50)
from typing import ValuesView


d1 = {1:'valor',2: 'valor2',3:'valor3'}
d2 = {
    'str' : 'valor4',
    123 : 'outro valor',
    (1,2,3,4) : 'Tupla'

}
d1.update({4:'another value'})
d1[5] = 'another value 2'
print (d1,d2)
print (d1.get(5), *d1[4],)
string = str( d2['str']).strip(',')
print(string.split(), type(string), d1.values())
print(*d2.keys())
print(type(d2.keys()))
d1[5] = '*'
print(len(d1.values()),d1[5])
for k,v in d1.items():
    print(k,v)
print(v)
t_1 = 'vinicius', 'juliana', 'vanda', 'cassio', 'silvia'

print(type(t_1),t_1,len(t_1))
string_2 = t_1[0]
print(string_2.title(), string_2.istitle())

