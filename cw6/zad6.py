def find(lista:list, sum_val:int, sum_ind:int, ind:int)->int:
    if sum_val == sum_ind and sum_ind != 0: return sum_ind
    if ind >= len(lista): return 0
    return find(lista, sum_val, sum_ind, ind+1) or find(lista, sum_val+lista[ind], sum_ind+ind, ind+1)

print(find([1,7,3,5,11,2], 0, 0, 0))