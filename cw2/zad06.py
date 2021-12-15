import math

def fact(a)->tuple:
    b = math.floor(math.sqrt(a))
    c = a//b
    return (b,c)

print(fact(120))