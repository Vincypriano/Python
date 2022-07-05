import os

var = os.environ
for v,k in os.environ.items():
    print(f'{v} = {k}')