print('\033[36;40m Exercício Python #050 - Soma dos pares \033[m')
print('=' * 40)
s = 0
c = 0
for n in range (0,6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        s += num
        c += +1
        if s or c == 0:
          print('Não foram digitados numeros pares!!')
print('A soma dos numeros pares é {} e foram {} numeros pares digitados'.format(s,c))   
print(num)
print('FIM!!') 