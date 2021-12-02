def cost(T:list, k:int, r:int=0)->int:
    branches = []
    if n == 7:
        if k-1 >= 0: branches.append(T[r][k])
        if k+1 < len(T): branches.append(T[r][k])
        branches.append(T[r][k])
        return min(branches)
    
    if k-1 >= 0: branches.append(cost(T, k-1, r+1) + T[r][k])       #left_forward
    if k+1 < len(T): branches.append(cost(T, k+1, r+1) + T[r][k])   #right_forward
    branches.append(cost(T, k, r+1) + T[r][k])                      #forward
        
    return min(branches)