a = input('Digite Algo :')
print('O tipo primitivo desse valor é : ',type (a))
print('É apenas espaços digitados??',a.isspace())
print('É numerico??',a.isnumeric())
print('É Alfabetico??',a.isalpha())
print('É Alfanumerico??? ',a.isalnum())
print('Esta em minusculas??',a.islower())
print('Esta em MAIUSCULAS??',a.isupper())
print('Esta Capitalizada???',a.istitle())
print('oque é??',a.isidentifier())
print(a.zfill(20))