'''c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')'''
import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)''''''''''