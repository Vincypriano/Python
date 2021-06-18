'''Escrteva um programa que leia um numero inteiro qualquer e peça para o usuario
escolher qual será a base de conversão:
1 para binario 2 para octal 3 para hexadecimal'''
num = int(input('Digite um numero inteiro: '))
print ('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL  ''')
opção = int(input('Sua opção: '))
if opção == 1:
    print ('o numero {} em binario fica {}'.format(num,bin(num)[2:]))
elif opção == 2:
    print( 'O Numero {} em OCTAL fica {}'.format(num,oct(num)[2:]))
elif opção == 3:
    print('O Numero {} em HEXADECIMAL fica {}')