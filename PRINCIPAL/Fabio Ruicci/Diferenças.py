notas_fabio = [9, 8, 10]
notas_josi = [10, 10, 9]

print(notas_fabio == notas_josi)
print(notas_fabio is notas_josi)

notas_vini = [ 9, 8, 10]
notas_ju = [9, 8, 10]

print(notas_vini == notas_ju)
print(notas_vini is notas_ju)

print(id(notas_ju))
print(id(notas_vini))
print(id(notas_vini)== id(notas_ju))

notas_joao = [9, 8, 10]
notas_nice = notas_joao

print(notas_joao == notas_nice)
print(notas_joao is notas_nice)

print(id(notas_joao))
print(id(notas_nice))
print(id(notas_joao) == id(notas_nice))

print(5 == 5)
print(5 != 5)
print([1, 2, 3]== [1, 2, 3])
print([1, 2] == [1, 2, 3] )
print()
print(None is None)
print(None is not None)
print()

#Chamada 1
resposta_da_api = {
    "title" : "The Catcher in the Rye",
    "author": "J.D. Salinger",
    "published": "July 16, 1951"
}

titulo = resposta_da_api.get("title")

if titulo is not None:
    print(f"Busca Realizada com sucesso.")
else:
    print(f"Nada encontrado.")
print()   
resposta_da_api1 = {}
titulo = resposta_da_api1.get("title")

if titulo is not None:
    print(f"Busca realizada com sucesso.")
else:
    print(f"Nada encontrado.")
print()

x = 42
y = 42
print(x == y)
print(x is y)
print()

v = 257
z = 257

print(v == z)
print(v is z)
print()

for i in range(-8, 260):
    resp = i is int(str(i))
    if not resp:
        print(f"{i} is {i}: {resp}")