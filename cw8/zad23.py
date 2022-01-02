def count_cycle(first) -> int:
    p = first
    cycle_visit = False
    cnt = 0
    while p is not None:
        cnt += 1
        if p.next.prev is not p:
            if cycle_visit is False:
                cycle_visit = True
                cnt = 0
            else: return cnt
        p = p.next