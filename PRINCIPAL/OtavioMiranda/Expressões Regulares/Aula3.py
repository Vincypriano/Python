# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
# {n}
# {min,max} 
#{10,} 10 ou mais
#{,10} de zero a 10
#{10} especificamente 10 vezes
# {5,10} De 5 a 10
#()+ [a-zA-Z0-9_]+
import re
from sys import flags

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970, 
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa ainda faz aquele café com pão de quaijo nas tardes de domingo.
Também né! Sendo a boa mineira que é, nucna esquece seu famoso
pão de queijo.
Não canso de ouvir Maria:
"Joooooooooãooooooooo, o café ta prontinho aqui. Veeemm"!

'''
print(re.findall(r'jo+ão+', texto, flags=re.I))
print(re.sub(r'jo+ão+','Vinicius', texto, flags=re.I))
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))

texto2 = 'João ama ser amado'
print(re.findall(r'ama[od]{0,2}', texto2, flags=re.I))

