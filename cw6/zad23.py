def find(table:list, res:int, cnt:int, pos:int)->bool:
    if res == 0 and cnt == 3: return True
    if res < 0 or cnt > 3 or pos >= len(table): return False

    return find(table, res, cnt, pos+1) or find(table, res-table[pos], cnt+1, pos+1)