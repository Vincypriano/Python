with open ("c:/Users/Elisabeth/Desktop/VINI/Python/PRINCIPAL/Let's Code/Projeto_Parte_1.txt",'w', encoding='utf-8') as arquivo:
    arquivo.write('''Datetime
Para treinar o uso da biblioteca datetime, execute as funções do código a seguir, tentando prever os seus resultados:

import datetime

d = datetime.date(2001, 9, 11)
tday = datetime.date.today()
print(tday, d)


# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

tdelta = datetime.timedelta(hours=12)
print(tday + tdelta)


bday = datetime.date(2016, 9, 24)
till_bday = bday - tday
print(till_bday.days)

dt_agora = datetime.datetime.now()
print(dt_agora.strftime('%B %d, %Y'))

dt_str = 'July 24, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime - Datetime para String
# strptime - String para Datetime''')
with open("c:/Users/Elisabeth/Desktop/VINI/Python/PRINCIPAL/Let's Code/Projeto_Parte_1.txt",'r', encoding='utf-8') as arquivo:
    print(arquivo.read(),end='')