#frase = str(input('Digite uma frase: ')).title().strip()
#print(frase,len(frase), frase.split(),'-'.join(frase))
#s = "hello"
#print('{} and {}'.format(s[len(s)-1],s[-1]))
'''list = [0,0,0]
print('{} {} {}'.format(list[0],list[1],list[2]))
list3 = [1,2,[3,4,'hello']]
list4 = list3[-1]
list4[-1] = 'goodbye' 
list3[-1] = list4
print(list3)'''
'''list5 = [8,6,4,3,2,9]
list5.sort ()
print(list5)
d = {'key1':{'key2':'hello'}}
d2 = d['key1']
print(d2['key2'])
'''
'''d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d2 = d['k1'][0]
d3 = d2['nest_key']
d4 = d3[1]
print (d4)'''
#d = 'hello'
#print(d[::-1])
##a = d[1:4]
#print(a)
'''list = [1,2,[3,4,'hello']]
list [2][2] = 'goodbye'
print (list)'''
#from typing import List


#list = [1,2,2,33,4,4,11,22,3,3,2]
#print(sorted(list))
'''minha_string = str(input('Digite uma frase: '))
tamanho_string = len(minha_string)

c = 0
contagem = 0
letra = ''

while c < tamanho_string:
    conta = minha_string.count(minha_string[c])

    if contagem < conta and minha_string[c].strip ():
        letra = minha_string[c]
        contagem = conta
    c += 1
print(f'{letra} {contagem} ')'''
lista_nomes = ['vinicius','silvia','juliana','cassio','Nice','João']
lista_nomes.sort ()
lista_nomes.append('Elaine')
print(lista_nomes[::-1])
print(lista_nomes[0])
lista = lista_nomes 
lista.remove('silvia')
print(lista)
if 'silvia' in lista:
    print('Faz parte da familia!!!')
else:
    print('Foi removida com .remove()')
print(lista_nomes)
print(len(lista_nomes))
lista.pop()
print(len(lista_nomes))
print(lista_nomes)
print(lista[::-1])
print(len(lista))
lista_nomes.insert(0, 'Vanda')
print(lista)
nome_removido = lista_nomes.pop(3)
print(nome_removido)
nome_familia = ('Pito','Lu','Mano','Paty')
print(nome_familia)
lista2 = list(nome_familia)
for c in range (0,4):
    lista.insert(-1,lista2[c])
print(len(lista),'\n',*lista)
n = len(lista)
c = 0
t_1 = '',
while c < n:
    t_1 = tuple(lista[c])
    print(*t_1,c,type(t_1))
    c += 1

