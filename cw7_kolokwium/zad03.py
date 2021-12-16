def sub_list(table:list)->int:
    ch_ind = [0]
    prev = table[0]
    for ind in range(len(table)):
        if table[ind] != prev:
            prev = table[ind]
            ch_ind.append(ind)
    ch_ind.append(len(table)-1)

    diff_ind = [0]*(len(ch_ind)-1)
    for ind in range(len(ch_ind)-1):
        diff_ind[ind] = ch_ind[ind+1]-ch_ind[ind]
    
    max_val = max(diff_ind)
    if len([x for x in diff_ind if x == max_val]) > 1: return 0
    return max_val

print(sub_list([1,3,3,3,5,7,11,13,13,1,2,2,2,2,3]))