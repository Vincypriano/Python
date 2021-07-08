with open("c:/Users/Elisabeth/Desktop/VINI/Python/PRINCIPAL/Let's Code/Parte 1/Tipos_de_Variáveis.txt",'w',encoding='utf-8')as arquivo:
    arquivo.write('''Variáveis
Variáveis são pedacinhos de memória onde armazenamos valores. Sempre que referenciamos o nome de uma variável, o valor é acessado. Definimos uma variável dando um nome a ela e usando o sinal de igual (=) para atribuir um valor.

x = -10 # uma variável do tipo inteiro (int)
y = 3.14 # uma variável do tipo real (float)
escola = "Let's Code" # uma variável literal (string)
primeiraAula = True # uma variável lógica (booleana)
Note que o operador igual (=) NÃO possui o mesmo comportamento da matemática. Na matemática, ele é um operador bidirecional: x = 2y seria a mesma coisa que 2y = x. No Python, ele é o que chamamos de um operador de ATRIBUIÇÃO: A expressão à direita do sinal é resolvida e seu resultado é armazenado na variável à esquerda.

Comentários
# Linhas iniciadas com # são comentários.
# Comentários são ignorados pelo Python e servem para explicar o código.
''''''
O símbolo # é um comentário de apenas 1 linha.
Usando 3 aspas simples consecutivas é possível abrir um bloco de comentário
de múltiplas linhas. O bloco se encerra com outras 3 aspas simples.'''
'''
Obs: Os cursos digitais dos processos seletivos não contêm os exercícios citados pelo instrutor.''')
with open("c:/Users/Elisabeth/Desktop/VINI/Python/PRINCIPAL/Let's Code/Parte 1/Tipos_de_Variáveis.txt",'r',encoding='utf-8') as arquivo:
    print(arquivo.read(),end='')