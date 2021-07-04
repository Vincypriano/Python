from time import sleep
from random import randint
item = ('PEDRA \U0001f44a','PAPEL \U0001f590\uFE0F','TESOURA \u270C\uFE0F')
comp = randint(0,2)
print('''Escolha uma opção
[0] PEDRA \U0001f44a
[1] PAPEL \U0001f590\uFE0F
[2] TESOURA \u270C\uFE0F''')
2
jog = int(input('Digite sua escolha: '))

print('JAN')
sleep(1)
print('KEN')
sleep(1)
print('PON!!!!')
print('=-'*11)
if comp == 0:#computador jogou PEDRA
    if jog == 0:
        print('o Computador jogou {}'.format(item[comp]))
        print('Você jogou {}'.format(item[jog]))
        print('EMPATE')
    elif jog == 1:
        print('o Computador jogou {}'.format(item[comp]))
        print('Você jogou {}'.format(item[jog]))
        print('GANHOU!')
    elif jog == 2:
        print('o Computador jogou {}'.format(item[comp]))
        print('Você jogou {}'.format(item[jog]))
        print('PERDEU')
    else:
        print('JOGADA INVALIDA!!!')
elif comp == 1: # COMPUTADOR JOGOU PAPEL
    if jog == 0:
        print('o Computador jogou {}'.format(item[comp]))
        print('Você jogou {}'.format(item[jog]))
        print('PERDEU!!')
    elif jog == 1:
        print('o Computador jogou {}'.format(item[comp]))
        print('Você jogou {}'.format(item[jog]))
        print('EMPATE!!')
    elif jog == 2:
        print('o Computador jogou {}'.format(item[comp]))
        print('Você jogou {}'.format(item[jog]))
        print('GANHOU!!')
    else:
        print('JOGADA INVALIDA!!!')
elif comp == 2: # COMPUTADOR JOGOU TESOURA
    if jog == 0:
        print('o Computador jogou {}'.format(item[comp]))
        print('Você jogou {}'.format(item[jog]))
        print('GANHOU!!')
    elif jog == 1:
        print('o Computador jogou {}'.format(item[comp]))
        print('Você jogou {}'.format(item[jog]))
        print('PERDEU!!')
    elif jog == 2:
        print('o Computador jogou {}'.format(item[comp]))
        print('Você jogou {}'.format(item[jog]))
        print('EMPATE!!')
    else:
            print('JOGADA INVALIDA!!!')
print('=-'*11)