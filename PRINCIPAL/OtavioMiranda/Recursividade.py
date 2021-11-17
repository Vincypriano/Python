'''Funções recursivas em Python'''
def fatorial (n:int) -> int:
    #caso base
    if n == 1:
        return 1
    #caso recursivo
    return n * fatorial(n - 1)


if __name__ == "__main__":
    fat5 = fatorial(5)
    print(fat5)
    