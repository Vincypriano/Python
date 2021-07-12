sexo = str(input('Digite seu sexo [F/M] :')).capitalize().strip()[0]
while True:
    if sexo not in 'FM':
        print('Digite valor válido [F/M]:')
        sexo = str(input('Digite seu sexo [F/M] :')).capitalize().strip()[0]
    elif sexo in 'FM':
        idade = int(input('Digite sua idade: '))
        if idade < 18:
            print('Você é menor de idade...')
            break
        elif idade >= 18:
            print('Perfeito, vc é maior de idade...')
            break
print('fim do programa...')