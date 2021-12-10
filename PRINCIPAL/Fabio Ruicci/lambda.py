from typing import List



alunos = [
    "ALUNO_20",
    "ALUNO_30",
    "ALUNO_100",
    "ALUNO_1",
    "ALUNO_10",
    "ALUNO_101",
]

print(sorted(alunos)) # ordena lista de forma normal relevando apenas as strings
print(sorted(alunos, key=lambda x: int(x[6:]) )) # cria uma chave para ler apenas os numeros (a partir da 6° string)

func = [
    lambda x: x**2,
    lambda x: x**3,
    lambda x: x**4
]

for f in func:
    print(f(5))
    
def f1(x): return x ** 2
def f2(x): return x ** 3
def f3(x): return x ** 4

func = [f1, f2, f3]

for f in func:
    print(f(10))
#map com lambda  
names_upper = map(lambda x: x.upper(), ["juliana", "vinicius"])
print(list(names_upper))

#map com def
def trans_capital(x): return x.upper()

names_upper = map(trans_capital, ["Nice", "João"])
print(list(names_upper))

#método nativo utilizando map
other_names = map(str.upper, ["helena", "stela"])
print(list(other_names))


#list compreension
print([x.upper() for x in ["mano", "paty"]])

#método para filtrar uma lista com lambda
names_with_a = filter(lambda x: "o" in x, ["pito", "lu"])
print(list(names_with_a))

#método com função def utilizando filter
def had_a(x): return "a" in x

names_with_a = filter(had_a, ["vinicius", "juliana"])
print(list(names_with_a))

#list compreession 
print([x for x in ["silvia", "cassio"]if "v" in x])

# onde fica dificil idenficar o códico porém é valido

f = lambda x,y: x if x < y else y
print(f(2,5))

# igual ao codigo anterior, utilizando def

def menor(x,y): 
    if x < y:
        return x
    return y


print(menor(10,5))

# socratica lambda

f = (lambda a,b,c: lambda x: a*x**2 + b*x + c) (2,1,2)
print(f(1))


# função quadrática (mesmo exemplo anterior porém com def)
def create_func_quadrática(a,b,c):
    return lambda x: a*x**2 + b*x + c


f = create_func_quadrática(2,1,2)
print(f(0))
print(f(1))
print(f(2))


