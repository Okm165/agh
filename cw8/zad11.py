from zad05 import Node

def del_add(first, key):
    prev = first
    curr = first.next
    while curr is not None:
        if curr.val == key:
            prev.next = curr.next
            return
        prev = curr
        curr = curr.next
    prev.next = Node(key)