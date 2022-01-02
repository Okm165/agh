def count_outofcycle(first) -> int:
    p = first
    cycle_visit = False
    total = 0
    cnt = 0
    while p is not None:
        if cycle_visit is False: total += 1
        cnt += 1
        if p.next.prev is not p:
            if cycle_visit is False:
                cycle_visit = True
                cnt = 0
            else: return total-cnt
        p = p.next