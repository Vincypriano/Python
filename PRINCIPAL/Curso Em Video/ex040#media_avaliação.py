n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) /2
if media >= 7:
    print('Você esta APROVADO!!!\nSua media foi {}'.format(media))
elif media > 5.0 or media < 6.9:
    print('Você esta em recuperação!!\nSua media foi {}'.format(media))
else:
    print('Você foi REPROVADO!!!\nSua média foi {}',format(media))