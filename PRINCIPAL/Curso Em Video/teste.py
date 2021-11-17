def cont(contIn, contFin,contPass):
    while contIn  < contFin:
        contIn  += contPass
        print(contIn, end=' ' )
    print('\nLoop Encerrado!')
    
inicio = int(input('Digite o Valor inicial: ')) 
final = int(input('Digite o Valor final: '))
passo = int(input('Digite o passo: '))

cont(inicio, final, passo)