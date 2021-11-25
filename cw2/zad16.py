def prim_fact(N)->list:
    ret = []
    x = 2
    a = N
    while N > 1 and x*x <= a:
        if N%x == 0:
            ret.append(x)
            N //= x
        else:
            x += 1
    if N != 1: ret.append(N)
    return ret

def prim_fact_sum(prim_fact_list:list):
    prim_sum = 0
    for elem in prim_fact_list:
        while elem > 0:
            prim_sum += elem%10
            elem //= 10
    return prim_sum

def search_smith():
    for i in range(1000000):
        prim_sum = prim_fact_sum(prim_fact(i))
        val_sum = 0
        i_copy = i
        while i_copy > 0:
            val_sum += i_copy%10
            i_copy //= 10
        
        if val_sum == prim_sum:
            print(i)

search_smith()