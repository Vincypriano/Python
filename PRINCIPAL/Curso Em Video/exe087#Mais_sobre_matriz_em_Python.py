'''Aprimore o daesafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna
C) O maior valor da segunda linha'''
lista = [[0,0,0],[0,0,0],[0,0,0]]
SomaPares = maior = SomaCol = 0
for p in range (0,3):
    for c in range(0,3):
        lista[p][c] = int(input(f'Digite um valor para [{p},{c}]: '))
for p in range(0,3):
    for c in range(0,3):
        print(f'[{lista[p][c]:^5}]', end='')
        if lista[p][c] % 2 == 0:                                            # Testa se o valor que esta sendo impresso na tela é par
            SomaPares += lista[p][c]                                        # Se True soma o valor a variável SomaPares

    print()
print('-='*30)
print(f'A soma dos valores PARES é {SomaPares}')
for p in range(0, 3):                                                       # Loop de 3 indices dentro da coluna 3
    SomaCol += lista[p][2]                                                  # Soma valores digitados para a coluna 3 mudando apenas a linha
print(f'A soma da 3° coluna é {SomaCol}')
for c in range (0,3):
    if c == 0 or lista[1][c] > maior:
        maior = lista[1][c]

