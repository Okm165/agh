def A(val:int)->int: #0
    return val+3

def B(val:int)->int: #1
    return val*2

def C(val:int)->int: #2
    cnt = 0
    val_copy = val
    while val_copy > 0:
        if (val_copy % 10) % 2 == 0:
            val += 10**cnt
        val_copy //= 10
        cnt += 1
    return val

def trans(X:int, Y:int, N:int, cnt:int=0, prev:int=-1)->int:
    if X == Y:
        # because C(X) not always changes value of X
        if cnt < N and prev != 2:
            return 1 + trans(C(X), Y, N, cnt+1, prev=2)
        else: return 1
    if cnt >= N: return 0

    su = 0
    if prev != 0: su += trans(A(X), Y, N, cnt+1, prev=0)
    if prev != 1: su += trans(B(X), Y, N, cnt+1, prev=1)
    if prev != 2: su += trans(C(X), Y, N, cnt+1, prev=2)
    return su

print(trans(11, 31, 4))
