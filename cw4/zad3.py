def has_even(n)->bool:
    while n > 0:
        if (n%10)%2 == 0: return True
        n //= 10
    else:
        return False

def check(T):
    for row in T:
        for elem in row:
            if not has_even(elem): break
        else: return True
    return False