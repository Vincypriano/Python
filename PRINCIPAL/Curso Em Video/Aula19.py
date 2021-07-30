'''      DICIONÁRIOS     '''
dados = {}
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
dados['sexo'] = 'M'
print(*dados.items())
print(dados.keys())
print(dados.values())
filme = {'titulo': 'Stars Wars', 'ano': 1997, 'Diretor': 'George Lucas'}
for k,v in filme.items():
    print(f'o {k} é {v}')
locadora = list()
locadora.append(filme)
print(locadora)
dados_1 = dict()
dados_2 = dict()
dados_1 = {'titulo': 'Avengers', 'ano': 2012, 'Diretor': 'Joss Whedon'}
dados_2 = {'titulo': 'Matrix', 'ano': 1999, 'Diretor': 'Wachowski'}
locadora.append(dados_1)
locadora.append(dados_2)
print(locadora[0]['ano'])