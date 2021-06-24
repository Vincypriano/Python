from math import factorial
print('\033[36;40m Exercício Python #060 - Calculo Fatorial\033[m')
print('\033[36;40m=\033[m' * 46)
''''''
num = int(input('Digite um número para \ncalcular seu fatorial:'))
fat = 1
cont = num
print('Calculando {}!= '.format(num),end='')
#while cont > 0:
for cont in range(num,0,-1):
    print('{}'.format(cont), end='')
    print('x'if cont >1 else ' = ',end='')
    fat *= cont
    cont -= 1
print('{}'.format(fat))

