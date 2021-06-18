print('_*'*20)
print('ESCOLHA A FORMA DE PAGAMENTO')
print('_*'*20)
valor = float(input('Digite o valor do produto: R$ '))
print('''Agora escolha a forma de pagamento
[1] Pagamento à vista
[2] Pagamento Debito
[3] Pagamento em 2x no Crédito
[4] Pagamento em 3x no Crédito''')
escolha = int(input('Digite aqui: '))
if escolha == 1:
    print('pagamento A VISTA, valor agora é: R${:.2f}'.format(valor - (valor* 0.10)))
elif escolha == 2:
    print('pagamento DÉBITO, valor agora é: R${:.2f}'.format(valor - (valor*0.05)))
elif escolha == 3:
    print('Pagamento CRÉDITO 2X, do valor de R${:.2f}'.format(valor),end=' ')
    print('e o valor da parcela ficou R${:.2f}'.format(valor / 2))
elif escolha == 4:
    print('Pagamento CRÉDITO 3X, o valor agora é: R${:.2f}'.format((valor +(valor * 0.2))),end=' ')
    print('e o valor da parcela ficou: R${:.2f}'.format((valor+(valor*0.2))/3))
else:
    print('FORMA DE PAGAMENTO INVALIDA!!')