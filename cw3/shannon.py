import math

def shannon(lista:list)->float:
    inf = 0
    p = 1/len(lista)
    for _ in range(len(lista)):
        inf -= p*math.log2(p)
    return inf

print(shannon([0,1,2,3,4,5,6,7,8,9]))