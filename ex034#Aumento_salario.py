salario = float(input('Digite o salario Atual\033[0;30;41m : R$'))
if salario <= 1250:
    print('o Salario anterior que era {} passa para {}'.format(salario,(salario +(salario * 0.15))))
else:
    print(' o Salario anterior que era {} passa para {}'.format(salario,(salario + (salario * 0.10))))