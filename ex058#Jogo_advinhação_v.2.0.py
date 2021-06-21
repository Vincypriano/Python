print('\033[36;40m Exercício Python #058 - Jogo Advinhação v 2.0\033[m')
print('\033[36;40m=\033[m' * 46)


from random import randint
from time import sleep
cont = 0
computador = randint(0,10)
print('Escolha um número de 0 a 10 e tente advinhar qual o computador \U0001f5a5\uFE0F  pensou!!!')
jogador = int(input('\U0001f579\uFE0F  Digite o numero \U0001f3b0 : '))

while computador != jogador:
    print('\U0001f6a8Errou\U0001f6a8!!!')
    sleep(1)
    if jogador > computador:
        print('Você digitou um numero maior!!',end='')
        
    elif jogador < computador:
        print('Você digitou um número Menor!!',end='')
        
    jogador = int(input((' Digite outro Numero: '.format(jogador,computador))))
    cont += 1

print('Você acertou com {} tentativas!!!'.format(cont))
