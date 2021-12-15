def prim_fact(val:int)->list:
    ret = []
    n = 2
    while val > 1:
        if not val % n:
            while not val % n:
                val //= n
            ret.append(n)
        else: n += 1
    return ret

# nie używam rekurencji bo wydaje mi się mocno zbędna

def sm(prim_fact:list)->int:
    ret = 0
    for i in range(1, 2**len(prim_fact)):
        cnt = 0
        sub = 1
        while i > 0:
            if i % 2: sub *= prim_fact[cnt]
            i //= 2
            cnt += 1 
        print(sub)
        ret += sub
    return ret

print(sm(prim_fact(60)))