'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma única lista que mantenha
separados os valores. No final mostre os valres pares e impares em ordem crescente'''
lista = [[],[]]                                                 # Cria listas dentro de listas
valor = 0                                                       # Inicia variável
for c in range(0,7):                                            # Loop For para 7 indices
    valor = int(input(f'Digite o {c+1}° valor: '))              # Recebe valor via teclado e coloca na variável 
    if valor % 2 == 0:                                          # Testa por meio da sobra se a divisão do número é igual a zero
        lista[0].append(valor)                                  # Caso True, acrescenta o valor digitado na primeira lista
    else:                                                   
        lista[1].append(valor)                                  # Caso False, acrescenta o valor digitado na segunda lista    
print('-='*30)
lista[0].sort()                                                 # Ordena de forma crescente a lista de valor 0 dentro de lista    
lista[1].sort()                                                 # Ordena de forma crescente a lista de valor 1 dentro de lista    
print(f'Os valores pares digitados foram: {lista[0]}')          # Imprime valores ordenados da primeira lista
print(f'Os valores ímpares digitados foram: {lista[1]}')        # Imprime valores ordenados da segunda lista
    