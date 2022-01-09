from typing import DefaultDict
from zad05 import Node

class CyclicList:
    def __init__(self, first = None) -> None:
        self.first = first
        self.last = first

    def push(self, val) -> bool:
        if self.first is None:
            self.first = Node(val)
            self.first.next = self.first
            self.last = self.first
        else:
            node = Node(val)
            node.next = self.first
            self.last.next = node
            self.last = node

    def __str__(self) -> str:
        ret = str(self.first.val)
        curr = self.first.next
        while curr != self.first:
            ret += " -> "
            ret += str(curr.val)
            curr = curr.next
        ret += ";"
        return ret

# very bad alg, no hash_map available :(
def del_cyclic(first, k):
    if first is None: return
    curr = first
    while curr.next != first:
        tmp = curr
        cnt = 0
        while tmp.next != curr:
            if tmp.val == curr.val: cnt += 1
            tmp = tmp.next
        if tmp.val == curr.val: cnt += 1
        if cnt == k:
            prev = curr
            ncc = curr.next
            while ncc != curr:
                if ncc.val == curr.val:
                    prev.next = ncc.next
                    ncc = ncc.next
                else:
                    prev = ncc
                    ncc = ncc.next
            if ncc == first:
                first = ncc.next
            prev.next = ncc.next
        curr = curr.next
    return first

cc = CyclicList()
cc.push(1)
cc.push(2)
cc.push(3)
cc.push(4)
cc.push(1)
cc.push(1)
cc.push(3)
print(cc)

first = del_cyclic(cc.first, 3)
curr = first
ret = str(first.val)
curr = first.next
while curr != first:
    ret += " -> "
    ret += str(curr.val)
    curr = curr.next
ret += ";"
print(ret)