def find(table:list, k:int, cnt:int=0,
        a_sum:int=0, a_cnt:int=0, b_sum:int=0, b_cnt:int=0)->bool:
    if a_cnt+b_cnt > k: return False
    if a_cnt+b_cnt == k and a_sum == b_sum: return True
    if cnt >= len(table): return False

    return (
        find(table, k, cnt+1, a_sum, a_cnt, b_sum, b_cnt) or
        find(table, k, cnt+1, a_sum+table[cnt], a_cnt+1, b_sum, b_cnt) or
        find(table, k, cnt+1, a_sum, a_cnt, b_sum+table[cnt], b_cnt+1)
    )
