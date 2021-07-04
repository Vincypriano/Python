
mulheres = homens = cont = 0


while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [F/M]')).upper().strip()[0]
    if idade >= 18:
        cont += 1
    if  sexo == 'F' and idade < 20:
        mulheres +=1
    if sexo == 'M':
        homens += 1
    saida = ' '
    while saida not in 'SN':
        saida = str(input('Deseja continuar?? [S/N]')).strip().upper()[0]
    if saida == 'N':
        break
print(f'Foram digitados {cont} MAIORES DE IDADE\n{homens} homens \n{mulheres} mulheres MENOR de 20 anos')     

