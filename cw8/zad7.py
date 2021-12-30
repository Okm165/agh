def pop(first):
    if first is None: return
    if first.next is None: 
        first = None
        return
        
    prev = first
    curr = first.next
    while curr.next is not None:
        prev = curr
        curr =  curr.next
    prev.next = None