lista_precos = [500, 1500, 2000, 100, 25]
nova_lista_precos = [i * 2 for i in lista_precos]
print(nova_lista_precos)
imposto = [i * 0.5 for i in lista_precos if i > 1000 ]
print(imposto)