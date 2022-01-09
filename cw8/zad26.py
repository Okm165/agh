from zad05 import Node, LinkedList

def consists(first_a, first_b) -> bool:
    if first_a is None or first_b is None: return False
    curr_a = first_a
    curr_b = first_b
    while True:
        tmp_b = first_b
        while curr_a is not None and tmp_b is not None and curr_a.val == tmp_b.val:
            curr_a = curr_a.next
            tmp_b = tmp_b.next
        if tmp_b is None: return True

        tmp_a = first_a
        while curr_b is not None and tmp_a is not None and curr_b.val == tmp_a.val:
            curr_b = curr_b.next
            tmp_a = tmp_a.next
        if tmp_a is None: return True

        if curr_a is not None and curr_b is not None: 
            curr_a = curr_a.next
            curr_b = curr_b.next
        else: break
    return False

LL1 = LinkedList()
LL1.push(1)
LL1.push(4)

LL2 = LinkedList()
LL2.push(1)
LL2.push(4)
LL2.push(13)
LL2.push(7)

print(consists(LL1.first, LL2.first))