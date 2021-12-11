T = [1,2,4,8,16,32]

def check(weights:list, w_left:int, ind:int = 0)->bool:
    if w_left == 0: return True
    elif ind >= len(weights)-1: return False
    return (check(weights, w_left, ind+1) or
            check(weights, w_left-weights[ind], ind+1) or
            check(weights, w_left+weights[ind], ind+1))

print(check(T, 17))