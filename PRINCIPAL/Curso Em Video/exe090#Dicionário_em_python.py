'''Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo na estrutura de tela'''
Aluno = dict()
while True:
    Aluno['Nome'] = str(input('Digite seu nome: '))
    Aluno['Nota'] = float(input(f'Digite a sua média {Aluno["Nome"]}: '))
    if Aluno['Nota'] <= 6.9:
        print(f'{Aluno["Nome"]} sua média de {Aluno["Nota"]} não foi suficiente...')
        print('REPROVADO')
    else:
        print(f'{Aluno["Nome"]} sua média foi {Aluno["Nota"]}')
        print('APROVADO!')
    saida = str(input('Você deseja continuar?? [S/N]: ')).upper().strip()[0]
    while saida not in 'SN':
        saida = str(input('Você deseja continuar?? [S/N]: ')).upper().strip()[0]
    if saida == 'N':
        break
print('Fim do programa...')