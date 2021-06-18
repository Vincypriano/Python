print('\033[36;40m Exercício Python #055 - Maior e Menor da sequência\033[m')
print('\033[36;40m=\033[m' * 46)
maior_peso = 0
menor_peso = 0 

for c in range(1,6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(c)))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
        
print('o maior peso digitado foi {}KG e o menor foi {}KG'.format(maior_peso,menor_peso))