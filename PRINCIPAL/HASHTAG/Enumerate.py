vendedores = ["Marcus", "Amanda", "Ale", "Carol"]
vendas = [15, 20, 10, 30]
print('N°| Nome   Qtd Vds')
for i, v in enumerate(vendedores):
    print(f"{i +1} | {v:8} = {vendas[i]}")