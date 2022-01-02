from zad05 import Node, LinkedList

def reduce(first):
    if first is None or first.next is None: return

    curr = first
    while curr is not None:
        sprev = first
        scurr = first.next
        while scurr is not None:
            if scurr is not curr and scurr.val[1] >= curr.val[0] and scurr.val[0] <= curr.val[1]:
                curr.val = (min(scurr.val[0], curr.val[0]), max(scurr.val[1], curr.val[1]))
                sprev.next = scurr.next
                scurr = scurr.next
                continue
            sprev = scurr
            scurr = scurr.next
        curr = curr.next


LL = LinkedList()
LL.push((15,19))
LL.push((2,5))
LL.push((7,11))
LL.push((8,12))
LL.push((5,6))
LL.push((13,17))
print(LL)
reduce(LL.first)
print(LL)