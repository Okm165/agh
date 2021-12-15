def prime_fact(N:int)->list:
    N_orig = N
    ret = []
    n = 2
    while N > 1 and n != N_orig:
        if not N % n:
            ret.append(n)
            N //= n
        else: n += 1
    return ret

def path(table:list, pos:int)->bool:
    if pos == len(table)-1: return True
    elif pos >= len(table): return False

    for fact in prime_fact(table[pos]):
        if path(table, pos+fact): return True
    return False

T = [9,6,5]
print(path(T,0))