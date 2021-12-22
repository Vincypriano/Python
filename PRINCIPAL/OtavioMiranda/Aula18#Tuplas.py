tupla = (1,2,3,0,"a","Tupla")

print(type(tupla))
print(tupla[-1])
print(len(tupla))
for t in tupla[2:]:
    print(t)

tupla2 = 1,2,3,5,"b","Tupla2"
print(help(tupla.index))

t3 = tupla + tupla2

n1,n2,n3,*_ = t3
print(*_)
