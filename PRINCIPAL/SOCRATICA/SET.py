example = set() # cria uma set (conjunto) vazio
for i in dir(example): # função dir serve para listar os métodos que podem ser aplicados a função
    print(i)
print(help(example.difference_update)) 
example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium") # método add serve para inserir dados nos sets (conjuntos)

print(example)
example.add(42) #Sets não armazena elementos duplicados
print(len(example))
example.remove(42) # método remove serve para tirar um elemento existente da lista retorna erro caso o elemento não esteja presente
example.discard(50) # método discard remove elemento do conjunto mas não retorna erro caso o elemento não exista 
example_2 = set([28, True, 2.71828, "Helium"])
print(len(example_2))
example_2.clear()
print(len(example_2))

odds = set([1, 3, 5 , 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set ([4, 6, 8 , 9 , 10])

print(odds.union(evens))
print(odds.intersection(primes))
print(primes.intersection(evens))
print(evens.intersection(odds))
print( 2 in primes)
print( 6 in odds)
print( 9 not in evens)
set_2 = odds.union(evens)
print(set_2)
print(evens.issubset(set_2))
print(evens.difference(composites))
