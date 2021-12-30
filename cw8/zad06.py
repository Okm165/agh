from zad5 import Node

def push(first, val):
    if first is None:
        first = Node(val)
        return
    while first.next is not None:
        first = first.next
    first.next = Node(val)
