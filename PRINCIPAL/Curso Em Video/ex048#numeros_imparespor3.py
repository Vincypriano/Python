s = 0
c = 0
for n in range(1,501,2):
    if n % 3 == 0:
        s += n
        c += 1
print('foram {} e a soma é {}'.format(c,s))
print("fim!!")