f = lambda num1, num2: num1 + num2
print(f(10,5))

lista = [10,20,30,40,50]
#---------------------------------
# exemple filter
'''def more_30(num):
    return num > 30
    
    
f_list = list(filter(more_30, lista))
print(f_list)'''

#------------------------------------
#exemple with lambda

f_list_2 = list(filter(lambda m30: m30 < 30, lista))
print(f_list_2)
