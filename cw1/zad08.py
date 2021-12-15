def prim_check(a):
    if(a < 2): return False
    c = 2
    while c*c <= a:
        if(a%c == 0 and a != c): return False
        c += 1
    return True

print(prim_check(541))
