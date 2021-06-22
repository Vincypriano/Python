import math
ang = float(input('Digite o angulo :'))
print('De acordo com o Numero {:.2f} teremos:'.format(ang))
print('{:.2f} é o Seno'.format(math.sin(math.radians(ang))))
print('{:.2f} é o Cosseno'.format(math.cos(math.radians(ang))))
print('{:.2f} é a Tangente'.format(math.tan(math.radians(ang))))
print ('raiz de 2 sobre dois é {}'.format((math.sqrt(2)/2)))