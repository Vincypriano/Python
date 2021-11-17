def contar(valor=11, caractere = "+"):
    for i in range(1,valor):
        print(caractere, end=' ')
contar()
print('\nPassando um caractere diferente "&"')
contar(caractere="&")
print('\nPassando um valor diferente "5"')
contar(valor=5)
print('\nPassando valor e caractere diferente "6" "$"')
contar(6,'$')
print('\nPassando valores invertidos')
contar(caractere='*',valor=4)
