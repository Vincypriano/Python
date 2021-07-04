'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
print('\033[36;40m Exercício Python #065 - Maior e Menor valor\033[m')
print('\033[36;40m=\033[m' * 44)
'''maior = 0
menor = 0
media = 0

print('Se desejar sair digite [999]')

while  num != 999:
    
    num = int(input('Digite o número : '))
    cont += 1
    maior = num
    menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

    
media = (maior + menor) / 2
soma = maior + menor
print('Você digitou {} Numeros'.format(cont))
print('O Maior numero digitado foi {}'.format(maior))
print('O Menor numero digitado foi {}'.format(menor))
print('A SOMA dos números foi {}'.format(soma))
print('A MEDIA foi {}...'.format(media))'''
resp = 'S'
soma = quant = media = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma/quant
print (f'o último número digitado foi {num}')
print(f'Foram digitados {quant} números...')
print(f'E a soma deu {soma}')