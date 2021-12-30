from zad5 import LinkedList

def add(first1, first2):
    sum = LinkedList()
    curr1 = first1
    curr2 = first2
    carry = 0
    while curr1 is not None or curr2 is not None:
        sum.push(carry)
        if curr1 is not None:
            sum.last.val += curr1.val
            curr1 = curr1.next
        if curr2 is not None:
            sum.last.val += curr2.val
            curr2 = curr2.next
        if sum.last.val // 10:
            carry = sum.last.val // 10
            sum.last.val %= 10
        else: carry = 0
    if carry: sum.push(carry)
    return sum

LL1 = LinkedList()
LL1.push(9)
LL1.push(7)
LL1.push(3)

LL2 = LinkedList()
LL2.push(1)
LL2.push(2)

print(add(LL1.first, LL2.first))