'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    saida = str(input('Você deseja continuar?? [S/N]: ')).strip().upper()[0]
    if 'N' in saida:
        break
if 5 in lista:
    print('Valor 5 está na lista')
else:
    print('Valor 5 não está na lista...')
print(f'Foram {len(lista)} números digitados...')
lista.sort(reverse=True)
print(f'A lista em forma decrescente fica {lista}')

