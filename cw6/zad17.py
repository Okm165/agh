def is_prime(N)->bool:
    if N == 2 or N == 3: return True
    if not N % 2 or N < 2 : return False
    for i in range(3, int(N**0.5)+1, 2):
        if not N % i: return False
    return True

def listify(val:int)->list:
    lst = []
    while val > 0:
        lst.append(val % 10)
        val //= 10
    return lst

def valuefy(lst:list)->int:
    val = 0
    for i in range(len(lst)):
        val *= 10
        val += lst[len(lst)-i-1]
    return val

def count(val1:list, val2:list, cnt1:int, cnt2:int, val:list)->int:
    if cnt1 == len(val1)-1 and cnt2 == len(val2)-1:
        if is_prime(valuefy(val)): return 1
        return 0
    elif cnt1 >= len(val1) or cnt2 >= len(val2): return 0
    return count(val1, val2, cnt1+1, cnt2, [*val, val1[cnt1]]) + count(val1, val2, cnt1, cnt2+1, [*val, val2[cnt2]])

print(count(listify(123), listify(75), 0, 0, []))