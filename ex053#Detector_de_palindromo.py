print('\033[36;40m Exercício Python #053 - Detector de Palindromo\033[m')
print('\033[36;40m=\033[m' * 46)
frase = str(input('Digite uma Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto [::-1]
'''for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print('O Inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!!')
else:
    print('Não é um PALÍNDROMO...')