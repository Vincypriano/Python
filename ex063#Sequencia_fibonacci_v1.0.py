print('\033[36;40m Exercício Python #063 - Sequência de Fibonacci v1.0\033[m')
print('\033[36;40m=\033[m' * 52)
num = int(input('Digite um numero para iniciar a sequiencia: '))
n = 0
n2 = 1 
cont = 3
print('{} ¬ {} '.format(n, n2),end='')
while cont <= num:
    n3 = n + n2
    print('¬ {} '.format(n3),end='')
    n = n2
    n2 = n3
    cont += 1
print('¬ FIM')
