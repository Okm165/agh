def f(x):
    return 1/x

def integral(f,a,b,e):
    ret = 0
    steps = int((b-a)//e)
    for i in range(steps):
        ret += f(a+i*e)*e
    return ret

print(integral(f, 1, 10, 0.001))