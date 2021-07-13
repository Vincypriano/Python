import requests as r
import datetime as dt
import csv

CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4
url = 'https://api.covid19api.com/dayone/country/brazil'
resp = r.get(url)
print(resp.status_code)
raw_data = resp.json()
print(raw_data[0])
final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'],obs['Recovered'], obs['Active'], obs['Date']])
final_data.insert(0,['Confirmados', 'Obitos','Recuperados','Ativos','Data'])

for i in range(1,len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]
#print(final_data)
'''print(dt.time(12,6,21,7), 'Hora:minuto:segundo.microsegundo')
print('----')
print(dt.date(2020,4,25), 'Ano-mês-dia')
print('----')
print(dt.datetime(2020,4,25,12,6,21,7), 'Ano-mês-dia Hora:minuto:segundo.microsegundo')'''
natal = dt.date(2020,12,25)
reveillon = dt.date(2021,1,1)

print(reveillon - natal)
print((reveillon - natal).days)
print((reveillon - natal).seconds)
print((reveillon - natal).microseconds)

with open ('Brasil_covid.csv','w') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)
    for i in range(1,len(final_data)):
        final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d' )
print(final_data)  