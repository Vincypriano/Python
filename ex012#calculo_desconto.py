'''Faça um algoritimo que leia o preço de um produto e mostre o novo preço com 5% de desconto'''
pre = float(input('Digite o valor do produto: R$'))
print ('O produto que custava R${:.2f}, agora na promoção ficou com o valor de R${:.2f}'.format(pre,(pre -(pre * 0.05))))