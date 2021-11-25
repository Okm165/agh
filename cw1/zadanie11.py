def sqrt(a,e):
    ret = a/2
    n_ret = (ret+a/ret)/2
    while abs(ret-n_ret)>e:
        ret = n_ret
        n_ret = (ret+a/ret)/2
    return ret

def find_divisors(s):
    T = []
    for i in range(1, int(sqrt(s,0.0001)+1)):
        if(s%i == 0):
            T.append(i)
            m = s//i
            if(m == i): continue
            T.append(m)
    return T

ZAP = []
AVOID = []
c = 4
while c < 1000000:
    if((c not in AVOID)):
        D = find_divisors(c)
        D.sort()
        a = sum(D[:-1])

        if(c == a):
            c+=1
            continue

        A = find_divisors(a)
        A.sort()
        b = sum(A[:-1])

        if(c == b and c != a):
            ZAP.append((c,a))
            AVOID.append(a)
            print(c,a)
    c+=1 
print(ZAP)