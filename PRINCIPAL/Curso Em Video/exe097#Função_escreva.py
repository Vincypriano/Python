'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
ex:
escreva('Olá, Mundo!')
saida:
-------
Olá, Mundo!
------- '''
def escreva(str):
    print('-'*30)
    print(str)
    print('-'*30)


mensagem = str(input('Digite sua mensagem: '))
escreva(mensagem)