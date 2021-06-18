print('\033[36;40m Exercício Python #052 - Números Primos \033[m')
print('\033[36;40m=\033[m' * 46)
tot = 0
num = int(input('Digite um Número inteiro: '))
for c in range(1,num +1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO Número {} foi divisível {} vezes'.format(num,tot))
if tot == 2:
    print('E por isso ele É PRIMO!!')
else:
    print('E por isso ele NÃO É PRIMO!!!')
