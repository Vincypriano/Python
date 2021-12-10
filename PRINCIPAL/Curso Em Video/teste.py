'''def cont(contIn, contFin,contPass):
    while contIn  < contFin:
        contIn  += contPass
        print(contIn, end=' ' )
    print('\nLoop Encerrado!')
    
inicio = int(input('Digite o Valor inicial: ')) 
final = int(input('Digite o Valor final: '))
passo = int(input('Digite o passo: '))

cont(inicio, final, passo)'''
alunos = ['ALUNO_30',
          'ALUNO_01',
          'ALUNO_101',
          'ALUNO_20',
          'ALUNO_10',
          'ALUNO_100'
          ]
print(sorted(alunos))
print(sorted(alunos,key=lambda x: int(x[6:])))

func = [
    lambda x: x ** 2,
    lambda x: x ** 3,
    lambda x: x ** 4,
]

for f in func:
    print(f(5))


def f1(x): return x ** 2
def f2(x): return x ** 3
def f3(x): return x ** 4

func = [f1, f2, f3]

for f in func:
    print(f(10))
