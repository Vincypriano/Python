lista = ['a', 'b', 'c', 'd']
novaLista = []
for j in lista:
    novaLista.append(j)
    print(novaLista)    
for i in lista:
    novaLista.pop()
    print(*novaLista)