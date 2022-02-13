import re

cel = '''
(21) 9 8852-5214
(11) 9955-1231
(35) 9 9975-4521
(31) 3851-2587
9 8571-5213
1234-5647
'''

cel_reg_exp = re.findall(r'^((\(\d{2}\)\s)(9\s)(\d{4}-\d{4}))$',cel,flags=re.M)
for telefone in cel_reg_exp:
    telefone_completo, ddd, nove, número = telefone
    print(telefone_completo)
    print(telefone)
    
cel_reg_exp = re.findall(r'^(?:\(\d{2}\)\s)(?:9\s)(?:\d{4}-\d{4})$',cel,flags=re.M)
for telefone in cel_reg_exp:
    print(telefone)