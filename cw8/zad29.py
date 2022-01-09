from zad05 import LinkedList, Node

def deldiff(first_a, first_b) -> int:
    cnt = 0
    prev_a = None
    curr_a = first_a
    prev_b = None
    curr_b = first_b
    while curr_a is not None and curr_b is not None:
        while curr_b is not None and curr_a.val > curr_b.val:
            cnt += 1
            if prev_b is None:
                first_b = curr_b.next
                prev_b = None
                curr_b = curr_b.next
            else:
                prev_b.next = curr_b.next
                curr_b = curr_b.next
        while curr_a is not None and curr_a.val < curr_b.val:
            cnt += 1
            if prev_a is None:
                first_a = curr_a.next
                prev_a = None
                curr_a = curr_a.next
            else:
                prev_a.next = curr_a.next
                curr_a = curr_a.next
        if curr_a is not None and curr_b is not None and curr_a.val == curr_b.val:
            prev_a = curr_a
            curr_a = curr_a.next
            prev_b = curr_b
            curr_b = curr_b.next

    if prev_a.next is not None:
        tmp_a = prev_a.next
        while tmp_a is not None:
            cnt += 1
            tmp_a = tmp_a.next
        prev_a.next = None
    
    if prev_b.next is not None:
        tmp_b = prev_b.next
        while tmp_b is not None:
            cnt += 1
            tmp_b = tmp_b.next
        prev_b.next = None

    return cnt

LL1 = LinkedList()
LL1.push(1)
LL1.push(2)
LL1.push(6)
LL1.push(7)
LL1.push(8)
LL1.push(9)
LL1.push(10)
LL2 = LinkedList()
LL2.push(1)
LL2.push(2)
LL2.push(4)
LL2.push(5)
LL2.push(6)
LL2.push(7)
LL2.push(8)
print(deldiff(LL1.first, LL2.first))
print(LL1)
print(LL2)