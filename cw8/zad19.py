def delete(first) -> int:
    if first is None or first.next is None: return 0
    deleted = 0
    prev = first
    curr = first.next
    while curr is not None:
        sprev = curr
        scurr = curr.next
        flag_deleted = False
        while scurr is not None:
            if curr.val == scurr.val:
                sprev.next = scurr.next
                scurr = scurr.next
                flag_deleted = True
                deleted += 1
            else: break
        if flag_deleted:
            prev.next = curr.next
            curr = curr.next
            continue
        
        prev = curr
        curr = curr.next
    return deleted

