'''Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999,
 que é a condição de parada. No final, mostre quantos números 
 foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''
print('\033[36;40m Exercício Python #066 - Varios Números com flag\033[m')
print('\033[36;40m=\033[m' * 44)
cont = soma = num =0

while num != 999:
    num = int(input(f'Digite o {cont + 1} valor: '))
    if num == 999:
         break
    cont +=1 
    soma += num
print(f'Foram digitados {cont} numeros, a soma é {soma}')


