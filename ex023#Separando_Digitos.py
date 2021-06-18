numero = int(input('Digite um numero de 4 digitos: '))
'''lista = str(numero)
print('Analisando o numero {}...'.format(numero))
print('Unidade: {}'.format(lista[0]))
print('Dezena: {}'.format(lista[1]))
print('Centena: {}'.format(lista[2]))
print('Milhar: {}'.format(lista[3]))'''
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print ('Analisando o {}'.format(numero))
print ('Unidade {}'.format(u))
print ('Unidade {}'.format(d))
print ('Unidade {}'.format(c))
print ('Unidade {}'.format(m))