s1 = {1,2,3,4,5,6}
s2 = set()
print(s1)
s2.add(('vinicius','Juliana','Vanda','Nice'))
print(s2)
s2.update([1,2,3])
for v in s1:
    print(v)
s2.discard(1)
print(s2)
s2.add(('João'))
print(s2)
s3 = s1 | s2
print(s3)
s3 = s1 & s2
print(s3)
s3 = s1 - s2
print(s3)
s3 = s2 - s1
print(s3)
s3 = s1 ^ s2
print(s3)
 