'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
lista = list()                                                      # Cria lista por método list()
for c in range(0,5):                                                # Cria com o loop for 5 valores para o contador (c)        
    num = int(input('Digite um valor: '))                           # Recebe valore inteiro pelo teclado
    if c == 0 or num > lista[-1]:                                   # Testa se na variavel (c) é o primeiro valor ou o último valor
        lista.append(num)                                           # Caso o teste seja True acrescenta o valor a lista
        print('Adicionado ao final da lista...')                    
    else:
        pos = 0                                                     # Cria variável na posição (0)
        while pos < len(lista):                                     # Loop da primeira a última posição do indice 
            if num <= lista[pos]:                                   # Testa se o valor é menor ou igual ao valor na lista por indice
                lista.insert(pos,num)                               # Caso o teste seja True coloca com método .insert(posição, número)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1                                                # acrescenta + 1 na variável pos   
print(f'Os Valores digitados em ordem foram {lista}')