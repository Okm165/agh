def del_even(first):
    curr = first
    while curr.next is not None:
        tmp = curr.next
        curr.next = curr.next.next
        curr = tmp.next
        if curr is None: return

