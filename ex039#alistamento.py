from datetime import date
data = date.today().year
print('''Escolha uma das Alternativas:
[1] MASCULINO
[2] FEMININO''')
gen = int(input('Qual seu genero:'))
if gen == 1:
    nasc = int(input('Digite o ano em que voce nasceu: '))
    alis = data - nasc
    if alis == 18:
        print('Voce esta na idade de se alistar!!')
    elif alis > 18:
        print('Você deveria ter se alistado a {} anos!!'.format(alis -18))
        print('O seu ano de alistamento foi em {}'.format(data - (alis - 18)))
    elif alis < 18:
        print('Você ainda não tem idade para se alistar!Faltam {} anos para se alistar'.format(18 - alis))
        print('Seu ano de alistamento será {}'.format(data - (alis - 18)))
else:
    print('Você não pode se alistar!!')
2