'''Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.'''
vel = float(input('Digite a velocidade atual do seu carro: KM/h '))
if vel >= 81:
    print('Você foi multado...')
    print('o Valor da sua multa será: R${:.2f}'.format((vel-80)*7))
else:
    print('Tenha um bom dia! Dirija com segurança!!')