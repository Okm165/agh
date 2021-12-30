from zad5 import Node

def del_add(first, key):
    found = False
    prev = first
    curr = first.next
    while curr is not None:
        if curr.val == key:
            found = True
            prev.next = curr.next
        prev = curr
        curr = curr.next
    if not found: prev.next = Node(key)