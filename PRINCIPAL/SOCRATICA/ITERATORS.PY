#
from unicodedata import digit
from matplotlib import ticker
from pyrsistent import b

list = ["CX32", "GSOF", "Emily", "Franz", "Rex"]
for element in list:
    print(element)
print()    
for element in ("José", "Boh", "Rusti"):
    print(element)
print()
for letter in "Socratica":
    print(letter)
print()  
for byte in b"Binary":
    print(byte)
print()
#for digit in 299792458:
#    print(digit)

c = 29792458
digits = [int(d) for d in str(c)]
[print(digit) for digit in digits]
print()
    
usernames = ('Rainer', 'Alfons', 'Flatsheep')
looper1 = usernames.__iter__()
print(type(looper1))
print()
print(looper1.__next__())
print(looper1.__next__())
print(looper1.__next__())
print()
print(usernames)
looper2 = iter(usernames)
print(next(looper2))
print(next(looper2))
print(next(looper2))
print()
users = ['laust', 'LeoMoon', 'JennaSys', 'dgletts']
#for user in users:
#    print(user)
looper = iter(users)
while True:
    try:
        user = next(looper)
        print(user)
    except StopIteration:
        break
print()
class Portifolio:
    def __init__(self):
        self.holdings = {} # Key = ticker, Value = number of shares
    
    def buy(self, ticker, shares):
        self.holdings[ticker] = self.holdings.get(ticker,0) + shares
        
    def sell(self, ticker, shares):
        self.holdings[ticker] = self.holdings.get(ticker,0) - shares
        
    def __iter__(self):
        return iter(self.holdings.items())
    
p = Portifolio()
p.buy('ALPHA', 15)
p.buy('BETA', 23)
p.buy('GAMMA',9)
p.buy('GAMMA', 20)

[print(ticker, shares) for (ticker, shares)in p]

import itertools

ranks = list(range(2,11)) + ['J', 'Q', 'K', 'A']
ranks = [str(rank) for rank in ranks]

print(ranks)