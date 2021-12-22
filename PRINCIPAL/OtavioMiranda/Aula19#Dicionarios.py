# Cria um dicionário vazio
d1 = {}
# Um dos métodos de criar dicionários com valores
d2 = dict(chave2='V2', chave3='V3')
print(type(d1))
print('-='*30)
d1 = {'chave1':"valor da chave"}
d1['nova_chave'] = "Valor da nova chave"
print(d1, d1['chave1'])
print(d2)
print('-='*30)
# método para atualizar valor existente
d1["chave1"] = "Outro valor de chave"
print(d1['chave1'])
print('-='*30)
# *.update({keys:values}) para criar novo valor
d1.update({'nova_chave': 'novo_valor'})
# deleta chaves e valores
del d2['chave2']
print(d1)
print('-='*30)
# Testa se chave existe com método get()
if d1.get('nova_chave') is not None:
    print(d1.get('nova_chave'))
print(d2)
print('-='*30)
# Métodos para encontrar valores em dicionários
print('chave3' in d2)
print('chave3' in d2.keys())
print('V3' in d2.values())
print('-='*30) 
# Método len() le tamanho de key:value 
print(len(d1))
print('-='*30)
for k in d1:
    print(k)
print('-='*30)
for v in d1.values():
    print(v)
print('-='*30)
for k,v in d1.items():
    print('{',k,'=',v,'}')
print('-='*30)
for k in d1.items():
    print(k[0], k[1])
print('-='*30)

Clientes = {
    'Cliente1': {
        'Nome' : 'Vinicius',
        'Sobrenome' : 'Vasconcellos',
    },
    'Cliente2' : {
        'Nome' : 'Juliana',
        'Sobrenome' : 'Kuhne',
    },
}

for clientesk, clientev in Clientes.items():
    print(f'Exibindo {clientesk}')
    for dadosk, dadosv in clientev.items():
        print(f'\t{dadosk} = {dadosv}')

print('-='*30)
# Método para não associar os dicionários, pois apenas associando eles são copias identidas e todas modificações
# que são feitas em um, a copia associa também.
import copy

d1 = {1:'a', 2:'b', 3:'c', 'd' : ['Vini', 'Juliana']}
v = d1.copy()
v[1] = 'Vini'
v2 = copy.deepcopy(d1)
v2['d'][0] = 'Joãozinho'

print(d1)
print(v)
print(v2)
print('-='*30)
print(dir(d1))
print(help(d1.fromkeys))
# Converte listas em dicionarios *(se os dados forem compativeis com dicionarios)
lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d1 = dict(lista)
print(d1)
print('-='*30)
# Converte listas com tuplas em dicionários *(se os dados forem compatíveis com dicionários)
lista = [
    ('c1', 1),
    ('c2', 2),
    ('c3', 3),
]

d2 = dict(lista)
print(d2)
print('=-'*30)
d2.pop('c1')
print(d2)
print('=-'*30)
d1.popitem()
print(d1)