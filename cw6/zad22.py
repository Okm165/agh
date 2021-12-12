def prim_fact(N:int)->list:
    ret = []
    n = 2
    while N > 1:
        if not N % n:
            ret.append(n)
            N //= n
        else: n += 1
    return ret

def roam(table:list, pos: int, jumps:int = 0)->bool:
    if pos == len(table)-1: return jumps
    if pos >= len(table): return 0

    for p in prim_fact(table[pos]):
        if jumps := roam(table, pos+p, jumps+1): return jumps
    return 0

T = [3,2,6,1,4]
print(roam(T, 0, 0))