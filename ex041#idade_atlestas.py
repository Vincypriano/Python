from datetime import date
atual = date.today().year
print('_*_'*24)
print('''Digite no próximo campo o ano do seu nascimento para poder identificar
o a sua categoria...''')
print('_*_'*24)
nasc = int(input('Digite o seu ano de nascimento: '))
calc = atual - nasc
if calc >= 25:
    print('Sua categoria é MASTER...')
elif calc > 19 or calc == 24:
    print('Sua categoria é SENIOR...') 
elif calc >14 or calc == 19:
    print('Sua categoria é JUNIOR...')
elif calc >9 or calc == 14:
    print('Sua categoria é INFANTO... ')
else:
    print('Sua categoria é MIRIN...')