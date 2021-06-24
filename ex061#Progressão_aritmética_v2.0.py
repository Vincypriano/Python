print('\033[36;40m Exercício Python #060 - Progressão Aritmetica v2.0\033[m')
print('\033[36;40m=\033[m' * 46)
p1 = int(input('Digite o Primeiro Termo: '))
raz = int(input('Digite a razão: '))
dec = p1
cont = 1
while cont <= 10:
    print('{} ¬ '.format(dec),end='')
    dec += raz
    cont +=1
print('FIM!!')

