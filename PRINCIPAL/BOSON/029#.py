'''Funções - Recursividade'''
def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatorial(num -1)

fat = int(input("Digite um número para calcular seu fatorial: "))
res = fatorial(fat)
print("O Fatorial de %d é %d" % (fat,res))
print(f"O Fatorial de {fat} é {res}")
print("O Fatorial de {} é {}".format(fat,res))

def fibonacci (num):
    if num <= 1:
        return num
    else:
        return fibonacci(num -1) + fibonacci(num -2)


x = int(input("Digite um número para calcular seu fibonacci: "))
res = fibonacci(x-1)
print('O Fibonacci de %d é %d' % (x,res))
print("O Fibonacci de {} é {}".format(x,res))
print(f'O Fibonacci de {x} é {res}')