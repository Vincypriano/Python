'''             LISTAS                  '''

lanche = ['Hamburguer','Suco','Pizza','Pudim'] #Criando uma lista com valores
print(lanche[2])            # imprime valor na 2° posição 


'''Métodos para acrescentar valores em listas '''

lanche[3] = 'Picolé'        #substitiu o valor que esta na 3° posição 
print(lanche)
lanche.append('cookie')     #acrescenta um valor a última posição da lista
lanche.insert(0,'Hot Dog')  # insere valores na lista de acordo com o parametro ( posição, valor )

''' Metodos de remoção em listas'''

del lanche[3]               # deleta valor na posição do parametro dentro dos colchetes [posição]
lanche.pop(3)               # deleta valor entre os parenteses ou o último item da lista (posição)
#lanche.remove('Pizza')      # remove valor dentro da lista ('valor') se o valor não estiver dentro da lista retorna erro 
if 'Pizza' in lanche:       # Cria uma condição que procura valor dentro da lista utilizando operador "in"
    lanche.remove('Pizza')  # remove valor dentro da condição
print(lanche)

valores = list(range(4,11)) # Cria uma lista de 7 indices com valores de 4 a 10
valores = [8,2,5,4,9,3,0]   # Valores criados dentro da lista fora de ordem
valores.sort()              # Alinha de forma crescente uma lista desordenada
valores.sort(reverse=True)  # Alinha de forma decrescente uma lista desordenada 
len(valores)                # Retorna quantos indices temos dentro de uma lista (contando de 1 em diante...)

num = [ 2, 5, 9, 1]         # Criando Listas com valores fixos
num[2] = 3                  # Atribuindo um outro valor a posição 2 da lista    
num.append(7)               # Acrescenta valor 7 a última posição da lista criando um novo valor no indice
num.sort()                  # Organiza de forma crescente a lista (menor para maior)
num.sort(reverse=True)      # Organiza de forma Decrescente a lista (maior para menor)
num.insert(2, 2)            # Acrescenta no indice 2 o valor zero movento os valores após o indice 2 para o final
num.pop(2)                  # Remove no indice 2 o valor da lista
num.remove(2)               # Remove o valor que esta dentro dos parenteses .remove(valor)
if 4 in num:                # Cria condição para remoção do valor "4" utilizando o metodo de verificação 'in'
    num.remove(4)
else:
    print("Não achei o número 4...")
print(num)
print(f'Essa lista tem {len(num)} elementos.')  # Mostra quantos indices tem na lista

valor = []                                      # Inicializou uma variavel tipo lista com valor vazio
valor.append(5)             
valor.append(9)
valor.append(4) 

valor_2 = list()
for cont in range(0,5):                         # Com a variável cont acrescentou um valor com o metodo .append() em cada posição da lista
    valor_2.append(int(input('Digite um valor: ')))
for c, v in enumerate(valor_2):                    # Com laço for colocou na variável "v" valores que estão dentro da lista 'valor' 
    print(f'Na posição {c} encontrei o valor {v}...')              # Na variável "c" coloca-se o indice
print("Cheguei ao final da lista...")

print(valor)    
for c, v in enumerate(valor):             # Com laço for colocou na variável "v" valores que estão dentro da lista 'valor' 
    print(f'Na posição {c} encontrei o valor {v}...')              # Na variável "c" coloca-se o indice
print("Cheguei ao final da lista...")


a = [2, 3, 4, 7]
b = a
b[2] = 8                            # Modificando dessa maneira a lista a que esta vinculada a lista b será alterada no indice 2 também
print(f'Lista A: {a}')
print(f'Lista B:{b}')

a = [2, 3, 4, 7]
b = a[:]                            # Cria uma cópia dos valores que estão em lista "a" de forma que não vincula as listas
b[2] = 8                            
print(f'Lista A: {a}')
print(f'Lista B:{b}')