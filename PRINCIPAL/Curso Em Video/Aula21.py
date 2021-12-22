def contador(i,f,p):
    """[contador () é uma função que recebe 3 números inteiros onde i = inicio, f = final e p = passo ]

    Args:
        i ([int]): [inicio]
        f ([int]): [final]
        p ([int]): [passo]
        
        return: sem retorno
        
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print("FIM!!")
    
    
contador(2,10,2)
help(contador)

def somar(a=0,b=0,c=0):
    s = a + b + c
    return s
    

resp1 = somar(9,8,4)
resp2 = somar(3,1)
print(f'Os cálculos deram {resp1}, {resp2}')

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
    
    
a = 5
teste(a)
print(f'A fora vale {a}')

def fatorial (num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f"\nO fatorial dos números digitados são: {f1}, {f2} e {f3}")

def par (n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    

num = int(input("Digite um número: "))
if par(num):
    print("É Par!!")
else:
    print("É Impar!!")