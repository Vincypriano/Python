import re
from pprint import pprint

from matplotlib.pyplot import text
texto = '''
ONLINE 192.168.0.1 GHIJK active
OFFLINE 192.168.0.2 GHIJK inactive
OFFLINE 192.168.0.3 GHIJK active
ONLINE 192.168.0.4 GHIJK active
ONLINE 192.168.0.5 GHIJK inactive
OFFLINE 192.168.0.6 GHIJK active
'''
#Positive Lokahead
lista_positive = re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(\w+)',texto)
#Negative Lokahead
lista_negative = re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)',texto)

ativosdict = {}
lista_positive2 = list()
lista_negative2 = list()
print(lista_positive)
for ip, status in lista_positive:
    ativosdict.clear()
    if status == 'active':
        ativosdict['IP'] = ip
        ativosdict['STATUS'] = status
        lista_positive2.append(ativosdict.copy())
    else:
        ativosdict['IP'] = ip
        ativosdict['STATUS'] = status
        lista_negative2.append(ativosdict.copy())
        
print(lista_positive2)
print(lista_negative2)
print()
print(re.findall(r'(?=.*[^in]active).+', texto))
print()
# Positive Lookbehind
print(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+.\d+.\d+)\s+\w+\s+\w+', texto))
# Negative Lookbehind
print(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+.\d+\.\d+)(?:\s+\w+)(\s+\w+)', texto))
var = re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+.\d+\.\d+)(?:\s+\w+)(\s+\w+)',texto)
[print(i,type(i))for i in var]
print(type(var))