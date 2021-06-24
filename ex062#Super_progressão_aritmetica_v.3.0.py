print('\033[36;40m Exercício Python #062 - Super Progressão Aritmetica v3.0\033[m')
print('\033[36;40m=\033[m' * 46)
p1 = int(input('Digite o Primeiro Termo: '))
raz = int(input('Digite a razão: '))
dec = p1
cont = 1
tot = 0
mais = 10
while mais != 0:
    tot += mais
    while cont <= tot:
        print('{} ¬ '.format(dec),end='')
        dec += raz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('PA Finalizada com {} termos mostrados'.format(tot))

