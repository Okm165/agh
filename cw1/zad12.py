def sqrt(a,e):
    ret = a/2
    n_ret = (ret+a/ret)/2
    while abs(ret-n_ret)>e:
        ret = n_ret
        n_ret = (ret+a/ret)/2
    return ret

# prime factorization
def prim_factorize(a):
    T = [1]
    k = 1
    while a>1 and k<sqrt(a, 0.1):
        i = 2
        while a%i != 0:
            i += 1
        a = a // i
        T.append(i)
        k += 1
    if(a != 1): T.append(a)
    return T

def gcd3(a,b,c):
    f_a = prim_factorize(a)
    f_b = prim_factorize(b)
    f_c = prim_factorize(c)

    cdiv = 1
    for i in f_a:
        if(i in f_b and i in f_c):
            cdiv *= i
    return cdiv



A = int(input("A:"))
B = int(input("B:"))
C = int(input("C:"))

print(gcd3(A,B,C))