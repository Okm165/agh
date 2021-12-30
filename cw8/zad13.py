def delete(first):
    if first is None: return
    prev = first
    curr = first.next
    while curr is not None:
        if curr.val < prev.val:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next