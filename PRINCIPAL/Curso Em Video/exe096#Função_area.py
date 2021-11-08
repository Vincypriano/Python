'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a área do terreno.'''
def area(a,b):
    f = a * b
    print(f'Somando a largura que é {a:.2f}M e o comprimento que é {b:.2f}M a area é {f:.2f}M²')


a = float(input('Digite o valor da largura: '))
b = float(input('Digite o valor do comprimento: '))
area(a,b)

