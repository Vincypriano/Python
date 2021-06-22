a = int(input(' Digite o Primeiro valor :'))
b = int(input(' Digite o Segundo valor :'))
c = int(input('Digite o Terceiro valor :'))
menor = a
if a >b and c > b:
    menor = b
if a > c and b >c:
    menor = c
print (' o Menor numero é {}'.format(menor))
maior = a
if a < b and c < b:
    maior = b
if a < c and b < c:
    maior = c
print ('O maior nmero é : {}'.format(maior))