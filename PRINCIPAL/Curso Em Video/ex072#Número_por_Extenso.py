t_1 = 'zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez'
t_2 = 'onze', 'doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'
t_3 = t_1 + t_2

while True:
    num = int(input('Digite um numero inteiro de 0 a 20 para mostrar o nome escrito por extenso:  '))
    if num > 20 or num < 0:
        num = int(input('Digite um numero inteiro de 0 a 20 para mostrar o nome escrito por extenso:  '))
    else:
        print(f'o numero digitado foi {t_3[num]}')
        break
print('Fim do Programa...')
