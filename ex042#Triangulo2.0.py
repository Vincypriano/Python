print(' * '*20)
print('ANALISADOR DE TRIANGULOS v2.0')
print(' * '*20)
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < (r2 + r3) and r2 < (r1 +r3) and r3 < (r1 + r2):
    print('Essas retas formam um triangulo!!',end=' ')
    if r1 == r2 == r3:
        print('Triangulo EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('Triangulo ESCALENO!') 
    else:
        print('Triangulo ISOCELES')
else:
    print('Essas retas não formam um triangulo!!')