'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''
l_1 = list()
l_i = []
l_p = []
while True:
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        l_p.append(num)
    else:
        l_i.append(num)
    l_1.append(num)
    saida = str(input('Você deseja continuar?? [S/N]')).upper().strip()[0]
    if saida == 'N':
        break
    
print(f'A lista criada foi {l_1} com todos os valores...')
print(f'Os números PARES digitados foram {l_p}')
print(f'Os números IMPARES digitados foram {l_i}')