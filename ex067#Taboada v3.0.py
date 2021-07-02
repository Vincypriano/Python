''' Faça um programa que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário. O programa será interrompido quando 
o número solicitado for negativo.'''
print('\033[36;40m Exercício Python #067 - Taboada v3.0\033[m')
print('\033[36;40m=\033[m' * 44)
print ('-' * 20)
while True:
    num = int(input('\nDe qual número você \nquer saber a taboada: '))
    if num < 0:
        break
    for cont in range (1,11):
        print (f'{num} x {cont} = {(cont * num)}')
print ('Taboada encerrada!!!')
