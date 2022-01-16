#==============================
# LAÇO FOR COM RANGE E LEN

pessoas = ["Fabio", "Josi", "Fulano", "Ciclano"]
idades = [29, 27, 34, 21]
maior_idade = 0
for i in range (len(pessoas)):
    idade = idades[i]
    if idade > maior_idade:
        pessoa_mais_velha = pessoas[i]
        maior_idade = idade
        
print(f"Pessoa mais velha: {pessoa_mais_velha}")

#================================
# ENUMERATE

maior_idade = 0 
for i, pessoa in enumerate(pessoas):
    idade = idades[i]
    if idade > maior_idade:
        pessoa_mais_velha = pessoa
        maior_idade = idade
print(f"Pessoa mais velha: {pessoa_mais_velha}")

#===================================
# ZIP
menor_idade = idades[0]
for idade, pessoa in zip(idades, pessoas):
    if idade < menor_idade:
        pessoa_mais_nova = pessoa
        menor_idade = idade
print(f'a Pessoa mais nova: {pessoa_mais_nova}')
print(list(zip(pessoas, idades)))

from collections import Iterator
pares = zip(pessoas, idades)
print(isinstance(pares, Iterator))
print(next(pares), next(pares))
print(next(pares), type(next(pares)))