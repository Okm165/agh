T = [10,5,12,4,2]

def count(T:list, ind:int, trg:int, curr:int)->int:
    if trg == curr: return 1
    elif curr > trg or ind >= len(T): return 0
    return count(T, ind+1, trg, curr) + count(T, ind+1, trg, curr*T[ind])
    
print(count(T, 0, 10, 1))