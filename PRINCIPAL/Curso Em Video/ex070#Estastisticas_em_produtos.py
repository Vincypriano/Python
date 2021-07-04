'''Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

prod1000 = soma = mbarato = 0
while True:
    prod = str(input('Digite o Nome do Produto: '))
    preço = float(input('Digite o Valor do produto: R$'))
    nome_mais_barato = prod
    soma += preço
    if preço > 1000:
        prod1000 += 1
    if preço < mbarato:
        mbarato = preço
        nome_mais_barato = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Gostaria de continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
    
print(f'o Valor total gasto foi R${soma:.2f}')
print(f'foram {prod1000} produtos acima de R$1000')
print(f'O produto mais barato foi {nome_mais_barato}')