from zad05 import Node

def check(val) -> bool:
    arr = [0]*8
    while val > 0:
        arr[val%8] += 1
        val //= 8
    if arr[5] % 2 == 0: return True
    return False

class LinkedList:
    def __init__(self) -> None:
        self.first = None
        self.last = None
    
    def push(self, val):
        if self.first is None:
            node = Node(val)
            self.first = node
            self.last = node
        else:
            node = Node(val)
            self.last.next = node
            self.last = node
    
    def move(self):
        if self.first is None: return
        prev = self.first
        curr = self.first.next
        while curr is not None:
            if check(curr.val):
                prev.next = curr.next
                tmp = self.first
                self.first = curr
                self.first.next = tmp
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

    def __str__(self) -> str:
        ret = str()
        p = self.first
        while p is not None:
            ret += str(p.val) + ", "
            p = p.next
        return ret

LL = LinkedList()
LL.push(12)
LL.push(12)
LL.push(12)
LL.push(11)
print(LL)