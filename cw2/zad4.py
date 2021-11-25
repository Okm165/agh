import math

def prim_factorize(a):
    F = []
    e = 2
    while a>1 and e <= math.sqrt(a):
        if(a%e == 0):
            F.append(e)
            a = a//e
            continue
        e += 1
    if(a != 1): F.append(a)
    return F

def search(N):
    result = 1
    for i in range(2, N+1):
        factors = prim_factorize(i)
        flag = (2 in factors) and (3 in factors) and (5 in factors)
        factors = [a for a in factors if (a != 2) and (a != 3) and (a != 5)]
        if(not factors and flag):
            result += 1
    return result

print(search(100))
print(prim_factorize(100))