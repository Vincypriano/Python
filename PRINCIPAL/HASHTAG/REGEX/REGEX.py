import re

# . - Entende qualquer valor exceto uma nova linha
# \. - para buscar o caracter "."
texto = 'arara'
t = re.compile(r'a...a')
check = t.findall(texto)
print(check)

# ^ - Irá testar o início da string
# [^] - urá considerar todos os caracteres EXETO o indicado
texto = 'babaca'
p1 = re.compile('^b')
p2 = re.compile('[^a]')
check = p1.findall(texto)
check2 = p2.findall(texto)
print(check)
print(check2)

# \d - Qualquer caracter que SEJA um algarismo de 0 a 9
# \D - Qualquer caracter que NÃO SEJA  um algarismo de 0 a 9
texto = 'arara1992'
p1 = re.compile(r'\d')
p2 = re.compile(r'\D')
check1 = p1.findall(texto)
check2 = p2.findall(texto)
print(check1)
print(check2)
print()

# \s - Qualquer caracter que SEJA vazio
# \S - Qualquer caracter que NÃO SEJA vazio
texto = '''
arara 1992

'''
p1 = re.compile(r'\s')
p2 = re.compile(r'\S')
check1 = p1.findall(texto)
check2 = p2.findall(texto)
print(check1)
print(check2)
print()

# \w - Qualquer caracter que SEJA alfanumérico
# \W - Qualquer caracter que NÃO SEJA alfanumérico
texto = '''

_arara@ 1992_

'''
p1 = re.compile(r'\w')
p2 = re.compile(r'\W')
check1 = p1.findall(texto)
check2 = p2.findall(texto)
print(check1)
print(check2)
print()

#============================================
# MATCH
texto = 'arara'
p1 = re.compile(r'r')
check_findall = p1.findall(texto)
check_match = p1.match(texto)
check_search = p1.search(texto)
check_finditer = p1.finditer(texto)
print(check_findall)
print(check_match)
print(check_search)
print(check_finditer)
[print(i, v) for i, v in enumerate(check_finditer)]
print()

texto = '''
Arara 1992
'''
p = re.compile(r'[a-zA-Z]+ [0-9]+')
c = p.finditer(texto)
for i in c:
    print(i)
print('* - zero ou mais')
# * - 0 ou mais

texto = '''
Arara
'''
p = re.compile(r'[ra]*')

correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)
    
print(' + - 1 ou mais')  
# + - 1 ou mais
texto = '''
Arara
'''

p = re.compile(r'[ra]+')

correspondencias = p.finditer(texto)
[print(correspondencia) for correspondencia in correspondencias]

print('? - 0 ou um')
# ? - 0 ou um
texto = '''
Arara
'''
p = re.compile(r'[r]?[a]?')

correspondencias = p.finditer(texto)
[print(correspondencia) for correspondencia in correspondencias]

print('{3} - número exato de repetições')
texto = '''
Arara
'''
p = re.compile(r'[ra]{4}')
correspondencias = p.finditer(texto)
[print(correspondencia)for correspondencia in correspondencias]

print('{3,4} - de 3 a 4 min e max')
texto = '''
Arara
'''
p = re.compile(r'[ra]{3,4}')
correspondencias = p.finditer(texto)
[print(correspondencia)for correspondencia in correspondencias]

print('()GRUPOS')
#()GRUPOS
texto = '''
Arara 1992
arara 1993
'''
p = re.compile(r'(A|a)?[a-z]{4} [0-9]+')
correspondencias = p.finditer(texto)
[print(correspondencia,'\n',correspondencia.group(0),'\n',correspondencia.group(1)) for correspondencia in correspondencias]

#TEXTOS:
print('TEXTOS')
texto1 = '''
Sites diversos:
https://google.com
https://www.gov.br
https://www.kaimaba.com.br
http://www.faetec.rj.gov.br
'''
p = re.compile(r'https?://(www\.)?([a-zA-Z0-9]+\.)+(com.br|gov.br|com)')
correspondencias = p.finditer(texto1)
for correspondencia in correspondencias:
    print(correspondencia)
    print(correspondencia.group(0))
    print(correspondencia.group(1))
    print(correspondencia.group(2))
    print(correspondencia.group(3))
    
print('EMAILS')
emails = '''
Vários e-mails:
daniel@dominio.com
daniel.candiotto@dominio.com.br
DANIEL.CANDIOTO@gov.br
danielcandiotto1@dominio1.co
daniel_candiotto_1@dominio-dominio.net
'''
p = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+')
correspondencias = p.finditer(emails)
for correspondencia in correspondencias:
    print(correspondencia)
    print(correspondencia.group(0))
    #print(correspondencia.group(1))
    #print(correspondencia.group(2))
    #print(correspondencia.group(3))
