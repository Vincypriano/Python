#frase = str(input('Digite uma frase: ')).title().strip()
#print(frase,len(frase), frase.split(),'-'.join(frase))
#s = "hello"
#print('{} and {}'.format(s[len(s)-1],s[-1]))
'''list = [0,0,0]
print('{} {} {}'.format(list[0],list[1],list[2]))
list3 = [1,2,[3,4,'hello']]
list4 = list3[-1]
list4[-1] = 'goodbye' 
list3[-1] = list4
print(list3)'''
'''list5 = [8,6,4,3,2,9]
list5.sort ()
print(list5)
d = {'key1':{'key2':'hello'}}
d2 = d['key1']
print(d2['key2'])
'''
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d2 = d['k1'][0]
d3 = d2['nest_key']
d4 = d3[1]
print (d4)
