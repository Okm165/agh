def crt(a,e):
    ret = a/2
    n_ret = (2*ret+a/(ret*ret))/3
    while abs(ret-n_ret)>e:
        ret = n_ret
        n_ret = (2*ret+a/(ret*ret))/3
    return ret

print(crt(10, 0.000001))