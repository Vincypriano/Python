# Meta caracteres: ^ $ ( )
# 


import re
texto = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div></div> 
'''

lista1 = re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', texto)
lista2 = re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', texto)
lista3 = re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', texto)
for i,v in enumerate(lista1):
    print(f'indice ',i,v)
print()
[print(f'indice ',i,v) for i,v in enumerate(lista2)]
print()
[print(f'indice ',i,v) for i,v in enumerate(lista3)]