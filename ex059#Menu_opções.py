print('\033[36;40m Exercício Python #059 - Menu Opções\033[m')
print('\033[36;40m=\033[m' * 46)

num_1 = float(input('Digite o Primeiro Numero: '))
num_2 = float(input('Digite o Segundo Numero: '))
opção = 0
while opção != 5:
    print('''Qual operação você gostaria de executar:
    OPÇÔES:
    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opção = int(input('Qual sua opção: '))
    if opção == 1:
        print('A Soma dos numeros {} e {} é igual a {}'.format(num_1,num_2,(num_1+num_2)))
    elif opção == 2:
        print('A multiplicação dos numeros {} e {} é igual a {}.'.format(num_1,num_2, (num_1*num_2)))
    elif opção == 3:
        if num_1 > num_2:
            num_3 = num_1
        else:
            num_3 = num_2
        print('Entre {} e {} o maior é {}'.format(num_1, num_2,num_3))
    elif opção == 4:
        num_1 = float(input('Digite o Primeiro Numero: '))
        num_2 = float(input('Digite o Segundo Numero: '))
        print('''Qual operação você gostaria de executar:
        OPÇÔES:
        [1]SOMAR
        [2]MULTIPLICAR
        [3]MAIOR
        [4]NOVOS NÚMEROS
        [5] SAIR DO PROGRAMA''')
        opção = int(input('Qual sua opção: '))
    elif opção == 5:
        print('Fim do Programa')
    else:        
        print('Opção inválida. Tente novamente...')
print('Finalizando...')


    


