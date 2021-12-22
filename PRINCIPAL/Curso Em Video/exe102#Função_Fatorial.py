'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado 
show(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial'''

def fatorial(num = 1, show=False):
    from time import sleep
    """[Função que retorna valor do Fatorial do número digitado e mostra pelo metodo show
    se o calculo será mostrado ou não...]

    Args:
        num (int, optional): [description]. Defaults to 1.
        show (bool, optional): [description]. Defaults to False.

    Returns:
        [int]: [Fatorial]
    """
    f = 1
    cont = num
    print(f'Calculando {num}! = ', end='')
    if show == True:
        while cont > 0:
            if show:
                sleep(0.5)
                print(f' {cont}', end='', flush=True)
                print(f' x ' if cont > 1 else ' = ', end='')
                f *= cont
                cont -=1
    else:
        f *= cont
        cont -= 1
    print(f)
                   
                    
num = int(input("Digite o Número que quer calcular o Fatorial: "))
show = bool(input("Digite True para mostrar o calculo e False para não mostrar: ").capitalize())           
    
fatorial(num, show)
    