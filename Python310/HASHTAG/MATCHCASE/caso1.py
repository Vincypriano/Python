def dia_semana(dia):
    match dia:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda"
        case 3:
            return "Terça"
        case 4:
            return "Quarta"
        case 5:
            return "Quinta"
        case 6:
            return "Sexta"
        case 7:
            return "Sábado"
        case outro_caso:
            return f"Valor {dia} inválido"
print(dia_semana(6))