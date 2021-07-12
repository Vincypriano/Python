times_1 = 'Flamengo','Palmeiras','Atlético MG','Atlético PR','Atlético GO','Fluminense','Corintians','Cuiaba','Juventude','Internacional',
times_2 = 'Gremio', 'Cruzeiro', 'Ceara','Fortaleza','Sport','Bragantino', 'Bahia', 'Santos','Chapecoence', 'América MG',
times_3 = times_1 + times_2
print(f'Os 5 primeiros times são {times_3[0:5]}')
print(f'Os 4 últimos colocados são {times_3[-5:-1]}')
print(sorted(times_3))
print(f'A Chapecoence esta na {times_3.index("Chapecoence")+1}° posição')
    