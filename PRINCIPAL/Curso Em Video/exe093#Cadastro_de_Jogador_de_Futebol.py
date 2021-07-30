'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
lista = dict()
partidas = list()
lista['Nome'] = str(input('Nome do Jogador: '))
n = int(input(f'Quantas partidas {lista["Nome"]} jogou? '))
for c in range(0,n):
   partidas.append(int(input(f'Quantos gols na partida {c + 1}?')))
lista['Gols'] = partidas[:]
lista['Total'] = sum(partidas)
print('-='*17)
for k, v in lista.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*17)
print(f'O Jogador {lista["Nome"]} jogou {len(lista["Gols"])} partidas')
for i, v in enumerate(lista["Gols"]):
    print(f'     -> Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {lista["Total"]} gols')