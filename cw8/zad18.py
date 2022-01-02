from zad05 import LinkedList

def uniq(first):
    if first is None or first.next is None: return
    
    prev = first
    curr = first.next
    while curr is not None:
        sprev = curr
        scurr = curr.next
        flag_delete = False
        while scurr is not None:
            if scurr.val == curr.val:
                sprev.next = scurr.next
                scurr = scurr.next
                flag_delete = True
            else:
                sprev = scurr
                scurr = scurr.next
        if flag_delete:
            prev.next = curr.next
            curr = curr.next
            continue
        
        prev = curr
        curr = curr.next

LL = LinkedList()
LL.push(10)
LL.push(12)
LL.push(14)
LL.push(14)
LL.push(17)
LL.push(17)
LL.push(14)
LL.push(17)
LL.push(13)
print(LL)
uniq(LL.first)
print(LL)