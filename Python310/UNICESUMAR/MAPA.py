# =============================================
# MENU
import os


def Menu():
    print("\033[1;30;44m Unicesumar \33[m")
    print('''
==~==PROGRAMA CADASTRO DE LIVROS==~==

[ 1 ] Inserir cadastro
[ 2 ] Mostrar Todos os cadastros
[ 0 ] Sair
        ''')

# ==============================================
# LÓGICA


def cad():
    while True:
        op = str(input("Digite sua opção: ")).strip()
        if op in '012':
            break
        print("Opção Inválida!!")

    if op == '1':
        r = "S"
        while r == 'S':
            if r == 'N':
                break
            if len(Cod) >= 5:
                print('''\nSistema de cadastro lotado. 
                      \nNão é possível armazenar mais informações\n''')
                os.system('pause')
                break
            Cadastro['Nome'] = str(input('\nNome do Autor: ')).capitalize()
            Cadastro['Obra'] = str(input('Nome da Obra: ')).capitalize()
            Cadastro['Editora'] = str(input('Nome da Editora: ')).capitalize()
            Cod.append(Cadastro.copy())
            r = str(input("Quer continuar? [S/N] ")).upper().strip()

        os.system("cls")
        Menu()
        cad()

    elif op == '2':
        if len(Cod) == 0:
            print("\nCadastro vazio.\n")
            continua()

        else:
            for i, v in enumerate(Cod):
                print(f'\nCod : {i+1}')
                for v, k in v.items():
                    print(f'{v} : {k}')
        continua()
    else:
        print("\nFIM DO PROGRAMA!!!")

# ==========================================================
# Continua


def continua():
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
        if resp in 'SN':
            break
        print('\nErro! Responda apenas S ou N.\n')
    if resp == 'N':
        os.system("cls")
        Menu()
        cad()

    if resp == 'S':
        os.system("cls")
        Menu()
        cad()


# ==========================================================
# PROGRAMA

os.system("cls")
Menu()
Cadastro = {}
Cod = []
cad()
