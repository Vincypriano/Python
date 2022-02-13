'''
    CONDIÇÕES - > IF, ELIF, ELSE
'''
if False:
    print("Condição verdadeira")
elif True:
    print("Segunda condição...")
else:    
    print("Ainda estou no bloco!")
    
'''
    OPERADORES RELACIONAIS -> ==, >, >=, <, <=, !=
    OBS: = -> ATRIBUIÇÃO
    == DIFERENTE VARIAVEL = VALOR
'''
a=2
b=2
c=3
d=0

if a != d:
    print("verdadeiro")
else:
    print("falso")
"""
    OPERADORES LÓGICOS -> AND, OR, NOT, IN, NOT IN   
"""

#(Verdadeiro E Verdadeiro) = TRUE
#(Verdadeiro E Falso) = FALSE
#(Verdadeiro OU Falso) = TRUE
#(Verdadeiro Ou Verdadeiro) = TRUE
#(Falso OU Falso) = TRUE
#(not) INVERTE
#(IN) ESTA EM

a=2
b=2
c=3
d=0 # "", {}, [], FALSO -> VERDADEIRO

if a == b and b != c:
    print("verdadeiro")
else:
    print("falso")

print()
nome = str(input("Digite seu nome: ")).capitalize().strip()
idade = int(input("Digite sua idade: "))
if idade >= 18:
   valor = float(input("Digite o valor do sem empréstimo: R$"))
   if idade < 30:
        print(f'Sr.(a){nome}, com base nos nossos calculos o valor final do empréstimo é R${valor * 2.35}')
        if idade >= 31  <= 60:
             print(f'Sr.(a){nome}, com base nos nossos calculos o valor final do empréstimo é R${valor * 3.87}')
        #else:    
            #print(f'Sr.(a){nome}, com base nos nossos calculos o valor final do empréstimo é R${valor * 4.22}')
else:
     print("Idade insuficiente para o emprestimo...")