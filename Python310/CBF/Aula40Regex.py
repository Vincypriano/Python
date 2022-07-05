import re #Regex


texto = "Curso de Python do CFB Cursos, canal do YouTube"

res = re.findall("o", texto)

pesq = input("Pesquisar: ")

print(res, len(res))
res2 = re.findall(pesq, texto)
print(res2, len(res2))