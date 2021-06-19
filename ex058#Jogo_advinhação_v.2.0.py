print('\033[36;40m Exercício Python #058 - Jogo Advinhação v 2.0\033[m')
print('\033[36;40m=\033[m' * 46)


from random import randint
from time import sleep
cont = 0
computador = randint(0,10)
print('Escolha um número de 0 a 10 e tente advinhar qual o computador pensou!!!')
jogador = int(input('Digite o numero: '))

while computador != jogador:
    print ('Errou!!! Você digitou {} e o computador pensou {}'.format(jogador,computador))
    cont += 1
else:
    print('Você acertou!!!')
    