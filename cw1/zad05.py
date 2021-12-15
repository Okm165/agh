def sqrt(a,e):
    ret = a/2
    n_ret = (ret+a/ret)/2
    while abs(ret-n_ret)>e:
        ret = n_ret
        n_ret = (ret+a/ret)/2
    return ret

print(sqrt(10, 0.000001))