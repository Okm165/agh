def before_cycle(first):
    p = first
    while p is not None:
        if p.next.prev is not p: return p.next.prev
        p = p.next
    return False