print('\033[36;40m Exercício Python #057 - Validação de dados\033[m')
print('\033[36;40m=\033[m' * 46)
sexo = ''
sexo = str(input('Digite o "SEXO"[M/F] : ')).upper().strip()
while sexo not in 'MmFf':
   sexo = str(input('Dados Inválidos. Por favor, informe seu sexo:')).strip(). upper()
print('Voce digitou {}'.format(sexo))