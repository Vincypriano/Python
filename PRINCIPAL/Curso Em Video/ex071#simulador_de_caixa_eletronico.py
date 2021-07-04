'''Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
 e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
saque = int(input('Digite o Valor a ser sacado: R$ '))k
total = saque
v_50 = v_20 = v_10 = v_1 = 0
while True:
    if total == 0:
            break
    v_50 = saque // 50
    total -= (v_50 * 50)
    if saque % 50 != 0:
        v_20 = total // 20
        total -= (v_20 *20)
    if total % 20 != 0:
        v_10 = total // 10
        total -= (v_10 * 10)
    if total % 10 != 0:
        v_1 = total
        while total != 0:                
                total -= 1 
if v_50 != 0:
    print(f'{v_50} notas de R$50,00')
if v_20 != 0:
    print(f'{v_20} notas de R$20,00')
if v_10 != 0:
    print(f'{v_10} notas de R$10,00')
if v_1 !=0:
    print(f'{v_1} notas de R$ 1,00')
print('Fim do Programa')