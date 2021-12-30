from zad3 import Node, LinkedList

def reverse(list1) -> Node:
    prev = list1
    curr = list1.next
    prev.next = None
    while curr is not None:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev

LL = LinkedList()
LL.push(1)
LL.push(2)
LL.push(3)
LL.push(4)
LL.push(5)
print(LL)
node = reverse(LL.first.next)

while node is not None:
    print(node.val)
    node = node.next

