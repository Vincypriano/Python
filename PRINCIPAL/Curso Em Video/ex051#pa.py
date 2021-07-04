print('\033[36;40m Exercício Python #051 - Progração Aritmética \033[m')
print('\033[36;40m=\033[m' * 46)

pt = int(input('Digite o Primeiro termo da PA: '))
raz = int(input('Digite a Razão da PA: '))
dec =   pt + (10-1) * raz
print('(',end='')
for c in range (pt,dec + raz,raz):
    print('{},'.format(c),end='')
    if c == (dec + raz):
        print('{})'.format(c))
#print(')')