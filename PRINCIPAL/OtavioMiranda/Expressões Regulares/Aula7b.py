#re.A → ASCII
#re.I → IGNORECASE
#re.M → Multiline
#re.S → Dotall

import re

cpf = '''
135.826.356-50
004.989.680-00
055.123.060-50
'''

print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', cpf, flags=re.M))

texto2 = 'O joão gosta de folia \nE adora ser amado'
print(re.findall(r'^o.*o$',texto2, flags=re.I| re.S))