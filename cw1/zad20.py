def sqrt(a,e):
    ret = a/2
    n_ret = (ret+a/ret)/2
    while abs(ret-n_ret)>e:
        ret = n_ret
        n_ret = (ret+a/ret)/2
    return ret

def cong(a,b,e):
    a,b = sqrt(a*b,0.01), (a+b)/2
    while abs(a-b) > e:
        a,b = sqrt(a*b,0.01),(a+b)/2
    return (a+b)/2

print(cong(10,100, 0.01))

