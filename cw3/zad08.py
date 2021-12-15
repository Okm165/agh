N = [12,13,4,12,55,1]

def prim_fact(N)->list:
    ret = []
    x = 2
    a = N
    while N > 1 and x*x <= a:
        if N%x == 0:
            ret.append(x)
            N //= x
        else:
            x += 1
    if N != 1: ret.append(N)
    return ret

def path_avail(val_list) -> bool:
    bool_list = [False]*len(val_list)
    bool_list[0] = True
    i = 0
    while bool_list[len(bool_list)-1] == False and max(bool_list) == True and i < len(bool_list):
        if bool_list[i] == True:
            for p in prim_fact(val_list[i]):
                if i+p < len(bool_list): bool_list[i+p] = True
            bool_list[i] = False
        i += 1
    
    return bool_list[len(bool_list)-1]

print(path_avail(N))