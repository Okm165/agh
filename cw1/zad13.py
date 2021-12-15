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

def lcm3(a,b,c):
    f_a = prim_factorize(a)
    f_b = prim_factorize(b)
    f_c = prim_factorize(c)
    
    for i in f_a:
        if i in f_b:
            f_b.pop(f_b.index(i))
        if i in f_c:
            f_c.pop(f_c.index(i))
    
    for i in f_b:
        if i in f_c:
            f_c.pop(f_c.index(i))
            
    comm = 1

    for i in f_a: 
        comm *= i
    for i in f_b: 
        comm *= i
    for i in f_c: 
        comm *= i
    
    return comm

    

A = int(input("A:"))
B = int(input("B:"))
C = int(input("C:"))

print(lcm3(A,B,C))