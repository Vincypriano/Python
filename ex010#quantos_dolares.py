''' Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar'''
dol = float(input('Digite quantos R$ voce tem na carteira : R$'))
cot = 5.5
print (' Contando que voce tem R${:.2f} na carteira '.format(dol))
print ('Na cotação atual você tem U${:.2f}'.format((dol/cot)))