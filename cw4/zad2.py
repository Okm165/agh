def is_odd(n) -> bool:
    ret = True
    while n > 0:
        if ((n%10)%2 == 0): 
            ret = False
            break
        n //= 10
    return ret

def check(T):
    for row in T:
        for elem in row:
            if is_odd(elem): break
        else:
            return False
    return True
