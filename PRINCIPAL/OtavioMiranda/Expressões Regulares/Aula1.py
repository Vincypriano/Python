# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto


import re

# findall serve para encontrar todas as ocorrencias de uma expressão 
# search retorna um objeto MACTH na primeira ocorrencia da expressão
# sub serve para substituir uma expressão
# compile serve para compilar uma expressão

string = 'Este é um teste de expressões teste regulares.'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'ABCD', string,count=1))

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF', string))