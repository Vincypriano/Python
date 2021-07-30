nome = str(input('Nome:'))
if nome.isalpha():
    print('1')
elif nome.isnumeric():
    print('2')
else:
    print('3')