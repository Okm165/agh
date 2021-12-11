T = [10,5,12,4,2]

def count(T:list, ind:int, trg:int, curr:int)->int:
    if trg == curr: return 1
    elif curr > trg or ind >= len(T): return 0
    one = count(T, ind+1, trg, curr)
    two = count(T, ind+1, trg, curr*T[ind])
    if two:
        print(T[ind])
        return 1
    if one: return 1
    return 0

count(T, 0, 10, 1)