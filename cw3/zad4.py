def calc(N):
    val = [0]*(N+1)
    sub = [0]*N
    val[0] = 2
    sub[1] = 1

    fact_cnt = 2
    fact = 2

    while max(sub) > 0:
        p = 10
        for i in range(N):
            sub[i] = p // fact
            p = p%fact * 10
        
        fact_cnt += 1
        fact *= fact_cnt

        for i in range(N-1, -1, -1):
            val[i] += (val[i+1] + sub[i])//10
            val[i+1] = (val[i+1] + sub[i])%10
        
    return val


print(calc(1000))

