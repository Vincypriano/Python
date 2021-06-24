'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

print('\033[36;40m Exercício Python #064 - Tratando varios valores v1.0\033[m')
print('\033[36;40m=\033[m' * 52)
cont = 0
soma = 0
num = 0
while not num == 999:
    num = int(input('Digite um numero [digite 999 para parar]: '))
    soma += num
    cont += 1
if num == 999:
    cont -= 1
    soma -= num
print('Você digitou {} números...'.format(cont))
print('A soma dos números digitados foi {}'.format(soma))
print('FIM!!!')