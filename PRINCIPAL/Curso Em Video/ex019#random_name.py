import random
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarton nome: '))
lista = [n1, n2, n3, n4]
ran = random.choice (lista) 
print ('o aluno sorteado foi:',ran)