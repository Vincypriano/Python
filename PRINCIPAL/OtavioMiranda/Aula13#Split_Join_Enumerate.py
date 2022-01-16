'''
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list
'''
string = "O Brasil é o pais do futebol, o o o o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')
print(lista_1)
print(lista_2)
for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase.')
palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)
    
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é "{palavra}" ({contagem}x)')
for valor in lista_2:
    print(valor.strip())
string2 = ' '.join(lista_1)
print(string2)
for  i,valor in enumerate(lista_1):
    print(i +1 ,valor)