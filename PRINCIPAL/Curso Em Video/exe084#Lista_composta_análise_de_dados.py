'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final mostre:
A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pessadas
C) Uma listagem com as pessoas mais leves'''
temp = list()                                                   # Cria uma lista auxiliar com método list()
principal = list()                                              # Cria uma lista que será usada para armazenar os dados 
maior = menor = 0                                               # Variáveis que levarão o valor do maior e do menor peso respectivamente
while True:                                                     # Loop Infinito
    temp.append(str(input('Nome:')))                            # Adiciona no primeiro indice da lista (temp)
    temp.append(float(input('Peso: ')))                         # Adiciona no segundo indice da lista (temp)
    if len(principal) == 0:                                     # Testa se a lista principal esta no primeiro indice
        maior = menor = temp[1]                                 # Se True carrega em ambas as variáveis o primeiro valor registrado         
    else:                                                       
        if temp[1] > maior:                                     # Testa se o peso registrado no segundo indice da lista é maior que o valor na variável
            maior = temp[1]                                     # Se True substitui o valor da lista por um novo
        if temp[1] < menor:                                     # Testa se o valor resgistrado no segundo indice da lista é menor que o valor na variável
            menor = temp[1]                                     # Se True substitui o valor da lista por um novo
    principal.append(temp[:])                                   # Após os testes, adiciona os valores da lista (temp) na lista (principal)
    temp.clear()                                                # Apaga valores registrados na lista (temp) com metodo .clear()
    resposta = str(input('Quer continuar? [S/N'))               # Cria Flag para sair do loop infinito
    if resposta in 'Nn':                                        # No caso de True para 'Nn'
        break                                                   # Encerra o loop
print(f'Ao todo, voce cadastrou {len(principal)} pessoas.')     # Imprime pelo método len() a quantidade de valores na lista (principal)
print(f'O maior peso foi de {maior}Kg. Peso de ',end='')        # Imprime o valor do maior peso registrado na variável (maior)
for p in principal:                                             # Loop for para testar os valores do segundo indice da lista digitada é igual ao da variável        
    if p[1] == maior:                                               
        print(f'[{p[0]}] ', end='')                             # Caso True, imprime o nome se o valor for correspondente
print()                                                         # Imprime uma lista vazia   
print(f'O menor Peso foi de {menor}Kg Peso de ',end='')         # Imprime o valor do menor peso registrado na variável (menor)
for p in principal:                                             # Loop for para testar os valores do segundo indice da lista digitada é igual ao da variável
    if p[1] == menor:                                           
        print(f'[{p[0]} ', end='')                              # Caso True, imprime o nome se o valor for correspondente    
print()                                                         # IMprime uma lista vazia
