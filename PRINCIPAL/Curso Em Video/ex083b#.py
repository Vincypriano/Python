lista = list()
expre = (str(input('Digite a expressão: '))).split('*')
lista.append(expre)
print(lista,lista.count('('),lista.count(')'))