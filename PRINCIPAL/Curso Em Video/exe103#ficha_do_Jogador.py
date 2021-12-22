'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opicionais: 
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(nome, gols):
    print(40*'-=')  
    lista = [nome,gols]
    if lista[0] == '':
        lista[0] = "Desconhecido"
    else:
        lista[0] = nome
    if lista[1] == '':
        lista[1] = 0
    else:
        lista[1] = int(gols)        
    return print(f'o Jogador {lista[0]} fez {lista[1]} gols na temporada')


print(30*'-=-')
nome = str(input("Digite o nome do jogador: ")).capitalize().strip()
gols = str(input("Digite quantos gols esse jogador fez: ")).strip()
ficha(nome, gols)