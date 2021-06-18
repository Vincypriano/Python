print('¬¬ '*20)
print('CALCULO DE IMC')
print(' ¬¬'*20)
alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (alt **2)
print('Seu IMC é : {:.2f}'.format(imc))
if imc < 18.5:
    print('Você esta abaixo do peso:')
elif imc < 24:
    print('Você esta com o peso ideal: ')
elif imc < 30:
    print('Você esta com sobrepeso!!')
elif imc < 40:
    print('Você esta com grau 1 de obesidade...')
else:
    print('Você esta com grau 2 de obesidade...')