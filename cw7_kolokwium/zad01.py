def even(num:int)->int:
    ret = 0
    while num > 0:
        if (num % 5) % 2 == 0: ret += 1
        num //= 5
    return ret

def is_valid(tab2:list, row, col)->bool:
    return row >= 0 and row < len(tab2) and col >= 0 and col < len(tab2)

def search(tab1:list, tab2:list)->bool:
    for i in range(-len(tab1)+1,len(tab2)+len(tab1)-1):
        for j in range(-len(tab1)+1,len(tab2)+len(tab1)-1):
            overlap_cnt = 0
            match_cnt = 0
            for k in range(len(tab1)):
                for l in range(len(tab1)):
                    rel_row = i+k
                    rel_col = j+l
                    if is_valid(tab2, rel_row, rel_col):
                        overlap_cnt += 1
                        if even(tab1[k][l]) == even(tab2[rel_row][rel_col]):
                            match_cnt += 1
            if (match_cnt / overlap_cnt)*100 >= 33: return True
    return False

