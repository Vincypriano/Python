'''Faça um programa que leia 5 valores numéricos e guarde - os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
l_1 = list()                                                                        # Criando lista com método list()

for c in range(0,5):                                                                # Loop criado com 5 indices para inserir valores na lista l_1
    num = input('Digite o {} número: '.format(c +1))
    l_1.insert(c,num)
    if c == 0:                                                                      # Se o contador estiver no primeiro indice ( 0 ) ambos os valores maior 
        maior = menor = l_1[c]                                                       # e menor recebem o primeiro valor        

maior = max(l_1)                                                                    # Metodo max() para inserir na variavel o maior valor da lista
menor = min(l_1)                                                                    # Metodo min() para inserir na variável o menor valor da lista
print(maior,menor)
print('O maior número digitado foi {} nas posições '.format(max(l_1)),end='')       # Imprime com método format() o maior valor da lista
for i , v in enumerate(l_1):                                                        # Loop criado para receber o indice (i) e valor (v) com metodo enumerate ()  
    if v == maior:                                                                  # Testa se na variavel (maior) tem o mesmo valor no loop  
        print(f'{i}...',end='')                                                     # Imprime valor do indice sem pular linha com método end=
print(f'O Menor número digitado foi {min(l_1)} nas posições ',end='')               # Imprime com método f o menor valor da lista
for i, v in enumerate(l_1):                                                         # Loop criado para receber o indice (i) e valor (v) com método enumerate ()
    if v == menor:                                                                  # Testa se na variável (menor) tem o mesmo valor no loop
        print(f'{i}...', end='')