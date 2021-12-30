from zad5 import Node, LinkedList

def _add1(elem):
    if elem.val // 10:
        elem.val %= 10
        if elem.next is not None:
            elem.next.val += 1
            _add1(elem.next)
        else: elem.next = Node(1)

def add1(first):
    first.val += 1
    _add1(first)

LL = LinkedList()
LL.push(9)
LL.push(9)
LL.push(9)
LL.push(9)
print(LL)
add1(LL.first)
print(LL)