def uniq(N:int)->int:
    if N < 2: return 0
    uniq = 0
    n = 2
    while N > 1 and n*n <= N:
        if N%n == 0: uniq += 1
        while N > 1 and N%n == 0:
            N //= n
        n += 1
    if N != 1: uniq += 1
    return uniq

def check(T:list)->bool:
    U = [0]*len(T)
    for i in range(len(T)):
        U[i] = uniq(T[i])
    if sum(U)%3: return False
    length = sum(U)//3

# not finished

    