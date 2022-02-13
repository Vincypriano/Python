# Meta caracteres: ^ $
# [@#a-zA-z0-9]
# (Vinicius|Vasconcellos)+
import re

texto = '''
<p>Frase 1</p> <p>Eita </p> <p>Qualquer Frase</p> <div>1</div>
'''

print(re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', texto))
tags = re.findall(r'(<([dpiv]{1,3})>(.+?)<\/\2>)',texto)
[print(tag1,tag3)for tag1, tag2, tag3 in tags]

cpf = '001.875.590-80'
c1 = re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})',cpf)
cpf2 = str(c1[0])
cpf2 = cpf2.replace('.','')
cpf2 = cpf2.replace('-','')
[print("Valido", cpf2)if len(cpf2) == 11 else print("Inválido")]
print()
print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)',r'"\3"',texto))
