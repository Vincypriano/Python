dias = int(input('Digite quantos dias você vai alugar o carro:'))
km = float(input('Digite a distancia em km:'))
total = (dias * 60)+ (km *0.15)
print('o Total do seu aluguel será de R${:.2f}'.format(total))