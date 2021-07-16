'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

times_1 = 'Flamengo','Palmeiras','Atlético MG','Atlético PR','Atlético GO','Fluminense','Corintians','Cuiaba','Juventude','Internacional',
'Gremio', 'Cruzeiro', 'Ceara','Fortaleza','Sport','Bragantino', 'Bahia', 'Santos','Chapecoence', 'América MG',
print(f'Os 5 primeiros times são {times_1[0:5]}')
print(f'Os 4 últimos colocados são {times_1[-5:-1]}')
print(sorted(times_1))
print(f'A Chapecoence esta na {times_1.index("Chapecoence")+1}° posição')
