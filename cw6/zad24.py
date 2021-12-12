from math import sqrt

T = [(2,3), (5,2), (1.2,5.2),(4,-13),(-3.5,12)]

def find(table:list, pos_x:int=0, a_cnt:int=0, pos_y:int=0, b_cnt:int=0, cnt:int=0):
    if(cnt == len(table)):
        if not a_cnt or not b_cnt: return None
        return sqrt((pos_x)**2 + (pos_y)**2)

    results = []
    # dont add point
    results.append(find(table, pos_x, a_cnt, pos_y, b_cnt, cnt+1))
    # add point to group a
    results.append(find(table, pos_x+table[cnt][0], a_cnt+1, pos_y+table[cnt][1], b_cnt, cnt+1))
    # add point to group b
    results.append(find(table, pos_x-table[cnt][0], a_cnt, pos_y-table[cnt][1], b_cnt+1, cnt+1))

    cleared = [x for x in results if x is not None]
    if cleared: return min(cleared)
    return None

print(find(T))