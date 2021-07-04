'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final mostrea media de idade
qual é o nome do homem mais velho e quantas mulheres tem menos de 20 anos'''
print('\033[36;40m Exercício Python #056 - Maior e Menor da sequência\033[m')
print('\033[36;40m=\033[m' * 46)

soma_idade = 0
media = 0
maior_idade_homem = 0
nome_velho = ''
cont_mulher_20 = 0


for n in range (1, 5):
    print('---------{}° PESSOA --------'.format(n))
    nome = str(input('Nome:')).strip ()
    sexo = str(input('Genero [M/F]: ')).strip ()
    idade = int(input('Idade: '))
    soma_idade += idade
    if  n == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
        cont_mulher_20 += 1
    if sexo in 'Ff' and idade > 20:
        cont_mulher_20 += 1
media = soma_idade / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem, nome_velho))
print('O total de mulheres com menos de 20 anos é {}'.format(cont_mulher_20))
