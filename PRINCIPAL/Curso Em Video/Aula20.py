'''def mostralinha(msg):
    print('-'*len(msg))
    print(msg)
    print('-'*len(msg))
    

mensagem = str(input('Digite o texto desejado: '))
mostralinha(mensagem)'''
'''def soma(a=0, b=0,c=0):
    s = a + b
    print(f'A soma de {a} + {b} é igual a {s}')
    

soma(4, 5)
soma(8, 9)
soma(1, 2)'''

def contador (*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')
    
    
contador(2,1,7)
contador(8,0)
contador(4,4,7,6,3)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos += 1
        

valores = [0,9,4,7,2,3]
dobra(valores)
contador(valores)
print(valores)

def soma (* valores):
    s = 0 
    for num in valores:
        s+= num
    print(f"Somando os valores {valores} temos {s}")
    
    
soma(5,2)
soma(2,9,5)