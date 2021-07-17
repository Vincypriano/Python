'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados , em ordem crescente'''
l_2 = list()                                                                            # Cria Lista com método list()
cont = num = 0                                                                          # Inicia variáveis com valor zero    

while True:                                                                             # Loop infinito
    num = int(input('Digite um valor:'))                                                # Recebe valores na variável
    if num in l_2:                                                                      # Testa se na lista ja existe o valor
        print('Esse número já foi digitado...')
    else:                                                                               # Codição para caso não tenha o mesmo valor dentro da lista
        print('Valor válido')                                                               
        l_2.insert(cont,num)                                                            # Método .insert(pos,valor) para inserir valores novos na lista 
        cont +=1                                                                        # Acrescenta valor na variável contador
    saida = ' '                                                                         # Inicia variável com valor vázio        
    while saida not in 'SN':                                                            # Testa com loop while se na variável (saida) não tem o valor 'SN'
        saida = str(input('Você deseja continuar?? [S/N]')).upper().strip()[0]          # Recebe uma string via teclado para     
    if 'N' == saida:                                                                    # Testa valor 'N' na variável (saida) 
            break                                                                       # Termina o loop caso valor testado seja True
l_2.sort()                                                                              # Coloca valores em ordem crescente dentro da lista
print(f'foram digitados {cont} números validos')
print(f'A lista sem valores duplicados ficou {l_2}')
