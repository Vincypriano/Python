def area(h,b):
    s=(h * b)
    print(f"A area de um terreno {h:.2f}m²x{b:.2f}m² é de {s:.2f}m²")
    

print("Controle de Terrenos")
print("-"*30)
h = float(input("Digite a largura do terreno: "))
b = float(input("Digite o cumprimento do terreno: "))
area(h,b)


def escreva(msg):
    print("~"*len(msg))
    print(msg)
    print("~"*len(msg))
    

mensagem = str(input("Digite o texto para ir na mensagem adaptavel: "))

escreva(mensagem)

from time import sleep

def contador(i,f,p):
    if i > f:
        p *=-1
    if p == 0:
        p = 1
    
        
    for c in range (i,f+1,p):
        sleep(0.3)
        print(c,end=" ",flush=True)
    print("FIM!!")
        

contador(1,10,1)
contador(10,0,2)
print("Agora sua vez de criar a contagem...")
i = int(input("Digite o primeiro número: "))
f = int(input("Digite o número final: "))
p = int(input("Digite o Passo: "))

contador(i,f,p)
    
    
def maior(lista):
    tam = len(lista)
    numeromaior = max(lista)
    for valor in lista:
        if valor == 0:
            print("Valor Nulo... ")
        
            
        
    
    print(f"os numeros passados foram {lista} no total de {tam} números")
    print(f"E o maior número é {numeromaior}")
    
    
    
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)    