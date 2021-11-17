'''Desempacotar e Empacotar '''


def listar (w,x,y,z):
    print(w,x,y,z)


lista = [30,27,25,24]

listar(*lista)

def somar (*args):
    soma = 0 
    for i in range(0, len(args)):
        soma += args[i]
    return soma

print(somar(1,2,3,4,5,6,7,8,9,10))
print(somar (77,23))