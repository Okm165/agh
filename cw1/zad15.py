def sqrt(a,e):
    ret = a/2
    n_ret = (ret+a/ret)/2
    while abs(ret-n_ret)>e:
        ret = n_ret
        n_ret = (ret+a/ret)/2
    return ret

e = 0.00001
def calculate_series(n):
    ret = sqrt(0.5,e)
    last = ret
    for i in range(n):
        last = sqrt(0.5+0.5*last, e)
        ret *= last
    return ret

print(2/calculate_series(10))