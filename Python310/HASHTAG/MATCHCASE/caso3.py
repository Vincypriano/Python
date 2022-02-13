def contas(centros):
    match centros:
        case [area, centro]:  # Apenas 1 centro de custo
            print(f"A área {area} possui o centro de custo {centro}")

            
        
        case [area, *centros]: # 2 ou mais centros
            print(f"A área {area} possui os centros de custo abaixo:")
            for centro in centros:
                print(f'    *{centro}')
            
            
contas(['Financeiro', 'ABC'])
contas(['Financeiro', 'ABC', 'XYZ', 'HJG'])