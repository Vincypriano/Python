'''Faça um programa que leia a altura e a largura de uma parede, calcule sua area e a quantidade de tinta
necessaria para pintala. Sabendo se que cada litro de tinta pinta uma area de 2M²'''
alt = float(input('Digite a Altura da parede:'))
lar = float (input('Digite a largura dessa parede:'))
area = alt * lar
print ('De acordo com os seguintes dados')
print ('sabendo que a altura é {}\ne a largura é {}'.format(alt,lar))
print ('Sera necessario {} para pintar a area de {}M²'.format((area*2),(area)))
