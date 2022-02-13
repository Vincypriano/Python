def fim_semana(dia):
    match dia:
        case 'Domingo' | 'Sábado':
            return "Fim de Semana"
        case _:
            return "Dia útil"
        
print(fim_semana('Domingo'))
print(fim_semana('Sábado'))
print(fim_semana('Segunda'))