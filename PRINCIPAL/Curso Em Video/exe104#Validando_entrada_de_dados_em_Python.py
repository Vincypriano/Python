"""Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante á função input()do Python
só que fazendo a validação para aceitar apenas um valor numérico.
Ex:
n = leiaInt('digite um n')"""
def leiaInt(num):
    print('-'*40)
    while num.isnumeric() == False:
        print("\033[31;40m ERRO, você não digitou um número válido!!!\033[m")
        num = str(input("Digite um número: "))
    else:
        return print(f'Você digitou {num}')
     
num = str(input("Digite um número: ")) 
leiaInt(num)