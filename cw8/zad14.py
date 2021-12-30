def delete(first):
    if first is None: return
    curr = first
    pro = first.next
    while pro is not None:
        if pro%curr == 0:
            curr.next = pro.next
            pro = pro.next
        else:
            curr = pro
            pro = pro.next