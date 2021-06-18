from datetime import date   
print('\033[36;40m Exercício Python #054 - Grupo Maior Idade\033[m')
print('\033[36;40m=\033[m' * 46)
cont_maior = 0
cont_menor = 0
data_atual = date.today().year
for c in range(1,8):
    nasc_pessoa = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    x = data_atual - nasc_pessoa
    if x >= 21:
        cont_maior += 1
    else:
        cont_menor += 1
print('temos {} pessoas maiores de idade e {} menores de idade.'.format(cont_maior,cont_menor))