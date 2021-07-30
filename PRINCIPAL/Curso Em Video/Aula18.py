dados = list()                      # Cria uma lista com método list()
pessoas = list()
dados.append('Pedro')               # Coloca primeiro dado na lista
dados.append(25)                    # Acrescenta valor no indice 1 da lista
pessoas.append(dados[:])            # Gera uma copia dos dados em modo de fatiamento dos indices
print(pessoas)
pessoas = [['Pedro',25],['Maria',19],['João',32]]
print(dados[0])
print(dados[1])
print(pessoas)
print(pessoas[0][0])                # Imprime primeiro valor dentro da primeira lista dentro da lista (pessoas)     Pedro
print(pessoas[1][1])                # Imprime o segundo valor dentro da segunda lista dentro da lista (pessoas)     19
print(pessoas[2][0])                # Imprime primeiro valor dentro da segunda lista dentro da lista (pessoas)      João
print(pessoas[1])                   # Imprime ambos os valores dentro da segunda lista                              ['Maria',19]
teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
for p in pessoas:
    print( f'{p[0]} tem {p[1]} anos de idade.')
galera = list()
dado = list()
totmaior = totmenor = 0
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')
