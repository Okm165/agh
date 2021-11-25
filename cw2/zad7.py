def if_in_serie(N):
    n = 1
    while N >= n:
        n = n*n+n+1
        if(N%n == 0): return True
    return False

print(if_in_serie(183))