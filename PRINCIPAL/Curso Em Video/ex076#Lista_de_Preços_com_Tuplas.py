'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
l_1 = 'Lápis', 1.17, 'Borracha', 2, 'Caderno', 10, 'Mochila', 120.50, 'Estojo', 32.70,
for c in range(0,len(l_1)):
    if c % 2 == 0:
        print(f'{l_1[c]:.<40}',end='')
    else:
        print(f'R$ {l_1[c]:>6.2f}') 