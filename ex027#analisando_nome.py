nome = str(input('Digite seu nome completo: '))
list = nome.split()
ultimo = len(list)
print ('Seu primeiro nome é {} e seu ultimo nome é {}'.format(list[0:-1]))