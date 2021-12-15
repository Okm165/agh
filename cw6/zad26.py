def is_comp(N:int)->int:
    if N == 1 or N == 2: return 0
    n = 2
    while n*n <= N:
        if not N % n: return 1
        n += 1
    return 0

def comp(A:int, B:int)->int:
    return find(A-1, B, 1)

def find(A:int, B:int, val:int)->int:
    if not A and not B: return is_comp(val)
    if A < 0 or B < 0: return 0
    return find(A, B-1, val*2) + find(A-1, B, (val*2+1))
    
print(comp(2, 3))