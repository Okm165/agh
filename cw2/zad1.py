def is_mul(m):
    a,b = 0,1
    while a*b < m:
        a,b = b,a+b
    if(a*b == m): return True
    return False

print(is_mul(int(input("A:"))))
