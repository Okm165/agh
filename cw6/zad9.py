T = [1,2,4,8,16,32]

def check(weights:list, w_left:int, ind:int = 0)->bool:
    if w_left == 0: return True
    elif ind >= len(weights)-1: return False
    if check(weights, w_left, ind+1):
        return True
    if check(weights, w_left-weights[ind], ind+1):
        print ("left dish: "+ str(weights[ind]))
        return True
    if check(weights, w_left+weights[ind], ind+1):
        print ("right dish: "+ str(weights[ind]))
        return True

print(check(T, 17))