def cos(x, n):
    ret = 1
    fact = 1
    sign = 1
    ex = 1
    for i in range(1,n+1):
        if(i%2): sign = -1
        else: sign = 1

        fact *= 2*i*(2*i-1)
        ex *= x*x

        ret += (sign/fact)*ex
    return ret

print(cos(3.14159265359, 100))