def sqrt(a,e):
    ret = a/2
    n_ret = (ret+a/ret)/2
    while abs(ret-n_ret)>e:
        ret = n_ret
        n_ret = (ret+a/ret)/2
    return ret

def find_divisors(A):
    T = []
    for i in range(1, int(sqrt(A,0.0001)+1)):
        if(A%i == 0):
            T.append(i)
            m = A//i
            T.append(m)
    T.sort()
    return T

print(find_divisors(int(input("A:"))))