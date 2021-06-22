'''Escreva um programa para aprovar crédito bancario para compra de uma casa.
O programa deve perguntar o valor da casa, o salario do comprador e em quantos anos ele vai quitar
Calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salario ou entao, o 
credito será negado'''
nome = str(input('Qual seu nome: '))
print('Olá, {}!!Gostaria de inciar com algumas perguntas'.format(nome))
casa = float(input('Qual o valor da casa que você quer adquirir: R$'))
sal = float(input('Qual seu sálario: R$'))
pres = int (input('E por último, em quantas prestações vc pretende pagar: '))
if (casa / pres) >= (sal * 0.30):
    print('Desculpa, mas seu crédito não será liberado.')
elif (casa / pres) <= (sal * 0.30):
    print('Seu crédio foi aprovado!!! Sua prestação ficou R${:.2f}'.format(casa / pres))
    print('Você vai quitar a casa em {:.2f} anos!! Boa sorte!!'.format(pres/12))