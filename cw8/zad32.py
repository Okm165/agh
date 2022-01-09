from zad05 import LinkedList, Node

def poly_sub(a,b) -> Node:
    if a is None or b is None: return None
    res = Node(a.val - b.val)
    curr = res
    a = a.next
    b = b.next
    while a is not None and b is not None:
        curr.next = Node(a.val - b.val)
        curr = curr.next
        a = a.next
        b = b.next
    while a is not None:
        curr.next = Node(a.val)
        curr = curr.next
        a = a.next
    while b is not None:
        curr.next = Node(- b.val)
        curr = curr.next
        b = b.next
    return res

LL1 = LinkedList()
LL1.push(0)
LL1.push(2)
LL1.push(6)

LL2 = LinkedList()
LL2.push(0)
LL2.push(2)
LL2.push(7)
LL2.push(1)

node = poly_sub(LL1.first, LL2.first)
while node is not None:
    print(node.val)
    node = node.next
print(LL1)
print(LL2)