def dia_semana(dia):
    if dia ==1:
        return "Domingo"
    elif dia == 2:
        return "Segunda"
    elif dia == 3:
        return "Terça"
    elif dia == 4:
        return "Quarta"
    elif dia == 5:
        return "Quinta"
    elif dia == 6:
        return "Sexta"
    elif dia == 7:
        return "Sábado"
    else:
        return f"Valor {dia} inválido"
    


print(dia_semana(dia=8))
import os
import sys

print(os.path.dirname(sys.executable))