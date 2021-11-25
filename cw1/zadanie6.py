def func(x):
    return x**x-2020

a,b = 0,5
def findroot(s,e,f,d): # start, end, function, dokładność
    m = (s+e)/2
    x = f(m)
    while abs(x) > d:
        if(x*f(s) < 0):
            s,e=s,m
        if(x*f(e) < 0):
            s,e=m,e
        m = (s+e)/2
        x = f(m)
    return m


print(findroot(a, b, func, 0.00001))