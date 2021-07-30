'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''
Geral = dict()
ListaGeral = list()
soma = media = 0
while True:
    Geral.clear()
    Geral['Nome'] = str(input('Nome: '))
    while True:
        Geral['Sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if Geral['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    Geral['Idade'] = int(input('Idade: '))
    soma += Geral['Idade']
    ListaGeral.append(Geral.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(f'Ao todo temos {len(ListaGeral)} pessoas cadastradas.')
media = soma / len(ListaGeral)
print(f'A média de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in ListaGeral:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ', end='')
print()
print('Lista de pessoas que estão acima da média:')
for p in ListaGeral:
    if p['Idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')

