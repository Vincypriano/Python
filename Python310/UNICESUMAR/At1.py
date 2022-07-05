mat = []            
for linha in range(0,2):
    lin = []            
    for coluna in range(0,3):
        lin.append(linha + coluna)
    mat.append(lin)
 
print(mat[0])
print(mat[1])