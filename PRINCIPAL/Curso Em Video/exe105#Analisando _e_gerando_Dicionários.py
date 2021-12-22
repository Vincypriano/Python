'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média de turma
- A situação (opcional)

adicione também as docstrigns a função.'''

def notas(*notas,sit=False):
    lista_notas = list()
    for n in notas:
        lista_notas.append(n)
    lista_notas.sort()
    print(lista_notas)
    print(sit)
    notas_dic = dict()
    notas_dic['maior'] = lista_notas[-1]
    notas_dic['menor'] = lista_notas[0]
    notas_dic['media'] = lista_notas(sum) / len(lista_notas)
    return print(f"A maior nota digitada foi {notas_dic['maior']}")
sit = str(input("Você deseja saber a situação da turma? [Sim/Não] ")).capitalize().strip()
while sit is not "SN":
    if sit[0] == 'S':
        sit = True
        break
    if sit[0]== 'N':
        sit = False
        break
    print('Você precisa digitar Sim ou Não...')
    sit = str(input('Deseja saber a situação da turma? [Sim/Não] ')).capitalize().strip()
    
nota = str(input("Digite a(s) nota(s): "))
s_ou_n = str(input("Deseja continuar? [S/N] ")).capitalize().strip()
lista_notas = []
while s_ou_n != 'SN':
    if s_ou_n == 'N':
        break
    if s_ou_n == 'S':
        lista_notas.append(nota)
        continue
    else:
        s_ou_n = str(input("Deseja continuar? [S/N] ")).capitalize().strip()
    nota = str(input('Digite a(s) nota(s): '))
print(lista_notas)
        
 

    

