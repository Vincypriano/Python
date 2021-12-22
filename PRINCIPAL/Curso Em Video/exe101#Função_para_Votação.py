'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou  OBRIGATÓRIO nas eleições.'''
def voto():
    import datetime as dt
    nome = str(input("Digite seu nome: "))
    nasc = int(input("Digite seu ano de nascimento: "))
    ano_atual = dt.date.today().year
    idade = ano_atual - nasc
    if idade > 18 and idade < 65:
        print("-="*20)
        print(f"{nome}")
        print(f"com {idade} anos: VOTO OBRIGATÓRIO")
    elif idade < 16:
        print("-="*20)
        print(f"{nome}")
        print(f"com {idade} anos: VOTO NEGADO")
    else:
        print("-="*20)
        print(f"{nome}")
        print(f"com {idade} anos: VOTO OPCIONAL")
    
    
    
voto()