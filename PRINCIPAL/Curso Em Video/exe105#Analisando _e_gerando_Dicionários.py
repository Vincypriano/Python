'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média de turma
- A situação (opcional)

adicione também as docstrigns a função.'''
def notas(*lista,sit=False):
    n = dict()
    n['Maior'] = max(nota_lista)
    n['Menor'] = min(nota_lista)
    n['Quant'] = len(nota_lista)
    n['Média'] = sum(nota_lista)/len(nota_lista)
    if sit:
        if n['Média'] >= 7:
            n['Situação'] = 'Boa'
        elif n['Média'] >= 5:
            n['Situação'] = 'RAZOAVEL'
        else:
            n['Situação'] = 'RUIM'    
    return print(n)

nota = str(input("Digite as notas: "))
while nota.isnumeric():
    nota_lista = list()
    nota_lista.append(nota)
    cond = str(input("Deseja continuar?[S/N] ")).strip().upper()[0]
    while cond != 'SN':
        while cond not in 'SN':
            print('Opção Inválida!!!')
            print('Digite apenas S ou N...')
            cond = str(input("Deseja continuar?[S/N] ")).strip().upper()[0]
        if cond == 'S':
            nota = float(input('Digite as notas: '))
            nota_lista.append(nota)
            cond = str(input("Deseja continuar?[S/N] ")).strip().upper()[0]
        else:
            break    
    else:            
        print('Valor Inválido!!')
        nota = str(input('Digite as notas: '))

 
print(nota,max(nota_lista),min(nota_lista),len(nota_lista))      
notas(nota)

        
    