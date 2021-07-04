from random import randint 
from time import sleep

computador = randint(0,5)#Faz o computador "PENSAR"
#print('Pensei no numero : {}'.format(computador))
jogador = int(input('Em que numero eu pensei??:'))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABENS!!  Voce conseguiu me vencer!!')
else:
    print("GANHEI!! Eu pensei no numero {} e nao no {}".format(computador,jogador))
