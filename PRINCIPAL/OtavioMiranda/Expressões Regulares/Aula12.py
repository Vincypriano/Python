import re

senhas = '''
VÁLIDAS
"Lv1h12As<W&
{no0MRjE81=<
O9tL^T-1rr5/
pk|t.OP^888A
n54R5:;AbY|f

SEM MINÚSCULAS
X6':7DU2T]8>
$3A#R 469PP:
:73]TD86?VG.
<0'D0W^S,43F
X5;7LT0P9?"?

SEM MINÚSCULAS E NÚMEROS
X$_E|J}QU;H[
I}B_AD`~}I[G
$T>A@K;^WLG^
Z?<Z!<[)CILF
OY*^X`S\Y}K>

SEM NÚMEROS CARACTERES E MINÚSCULAS
WWIOAIVLFWLA
LYMANBPGOTPW
NUJSMBKIUEFH
BULYCKXTECZS
KXDJFZHCNEAR

QUANTIDADE INVÁLIDA (6)
j"D74d
9;zv6B
]9ar8M
O8\q5y
/Yd2c0
'''

search_senhas = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{12,}')
search_senhas2 = re.findall(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{12,}',senhas)
for i in search_senhas2:
    print(i)