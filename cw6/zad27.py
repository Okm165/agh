def area(square:tuple)->int:
    return (square[1]-square[0])*(square[3]-square[2])

def do_overlap(square1:tuple, square2:tuple)->bool:
    return ((square1[1] > square2[0] and square1[0] < square2[1]) and
            (square1[3] > square2[2] and square1[2] < square2[3]))

def conflicts(squareList:list, square:tuple)->list:
    conflicts = []
    for lsquare in squareList:
        if do_overlap(lsquare, square): conflicts.append(lsquare)
    return conflicts

def search(table:list, squareList:list, area:int, cnt:int)->bool:
    if area == 2012 and len(squareList) == 13: return True
    if table_cnt >= len(table): return False

    #find conflicts
    if conflicts := conflicts(squareList, table[cnt]):
        # ignore conflicting one
        if search(table, squareList, area, cnt+1): return True
        d_area = 0

        # remove conflicted
        # add conflicting one
        for conf in conflicts: 
            squareList.pop(squareList.indexof(conf))
            d_area -= area(conf)
        squareList.append(table[cnt])

        d_area += area(table[cnt])
        if search(table, squareList, area + d_area, cnt+1): return True

        # restore conflicted
        # remove conflicting one
        for conf in conflicts: 
            squareList.append(conf)
        squareList.pop(squareList.indexof(table[cnt]))

        return False
    
    # do NOT add square (no conflicts)
    if search(table, squareList, area, cnt+1): return True
    
    # add square (no conflicts)
    squareList.append(table[cnt])
    if search(table, squareList, area + area(table[cnt]), cnt+1): return True
    squareList.pop()

    return False


