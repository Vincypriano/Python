from math import hypot
cato = float(input('Digite o valor do cateto oposto: '))
cata = float(input('Digite o valor do cateto adjacente: '))
print ('De acordo com os numeros digitados o comprimento da hipotenusa é {:.2f}'.format(hypot(cato,cata)))
