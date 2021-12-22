# List example
prime_numbers = [2, 3, 5, 7, 11, 13, 17]

# Tuple example
perfect_squares = (1, 4, 9, 16, 25, 36)

# Display lengths
print("# Primes = ", len(prime_numbers))
print("# Squares =", len(perfect_squares)) 

for p in prime_numbers:
    print("Prime: ", p)
for n in perfect_squares:
    print("Square: ", n)
    
print("List Methods")
print(dir(prime_numbers))
print(160*'-')
print("Tuple Methods")
print(dir(perfect_squares))
empty_tuple = () # criar uma tupla
test1 = ("a",) # sem colocar depois do dado a virgula, será criada uma string (no caso) e não uma tupla
test2 = ("a", "b")
test3 = ("a", "b", "c")

print(empty_tuple)
print(test1)
print(test2)
print(test3)

test1 = 1,
test2 = 1, 2
test3 = 1,2,3

print(test1)
print(test2)
print(test3)

print(type(test1))
print(type(test2))
print(type(test3))

#(age, country, knows_python)
survey = (27, "Vietnam", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]

print("Age =", age)
print("Country =", country)
print("Knows Python =", knows_python)

survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2

print("Age =", age)
print("Country =", country)
print("Knows Python =", knows_python)