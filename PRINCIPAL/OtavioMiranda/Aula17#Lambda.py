#-------------------------------
#def

def func(arg,arg2):
    return arg * arg2

var = func(2,2)
print(var)
#--------------------------------
#lambda

a = lambda num1,num2: num1 * num2
print(a(3,5))

def func2(item):
    return item[1]
lista = [
    ['P1', 20],
    ['P2', 100],
    ['P3', 13],
    ['P4', 15],
    ['P5', 40]
]
print(lista)
lista.sort(key=func2, reverse=True)
print(lista)

lista.sort(key=lambda x: x[1] )
print(lista)
print(sorted(lista, key=lambda x: x[0]))
print(lista)