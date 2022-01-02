def check_cycle(first) -> bool:
    p = first
    while p is not None:
        if p.next is None: return False
        elif p.next.prev is not p: return True
        p = p.next
    return False
