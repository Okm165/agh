class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.prev = None
        self.next = None

def count_ones(val) -> int:
    cnt = 0
    while val > 0:
        val &= val-1
        cnt += 1
    return cnt

def check(val) -> bool:
    return (count_ones(val) % 2) == 1

class LinkedListBidirectional:
    def __init__(self) -> None:
        self.first = None
        self.last = None
    
    def push(self, val):
        node = Node(val)
        if self.first is None:
            self.first = node
            self.last = node
        else:
            node.prev = self.last
            self.last.next = node
            self.last = node

    def insert(self, pos, val):
        curr = self.first
        if pos == 0:
            tmp = self.first
            self.first = Node(val)
            self.first.next = tmp
            tmp.prev = self.first
            return
        
        while curr is not None and pos > 1:
            curr = curr.next
            pos -= 1

        if curr.next is None:
            node = Node(val)
            node.prev = curr
            curr.next = node
        else:
            node = Node(val)
            node.prev = curr
            node.next = curr.next
            curr.next.prev = node
            curr.next = node
    
    def __str__(self) -> str:
        ret = str()
        p = self.first
        # Debug mode
        while p is not None:
            if p.prev is not None: ret += str(p.prev.val)
            else: ret += "None"
            ret += "<-" + str(p.val) + "->"
            if p.next is not None: ret += str(p.next.val)
            else: ret += "None,"
            ret += "  "
            p = p.next
        return ret

    # funkcja z zadania
    def delete(self):
        p = self.first
        while p is not None:
            if check(p.val):
                if p.prev is not None and p.next is not None:
                    p.prev.next = p.next
                    p.next.prev = p.prev
                elif p.prev is None and p.next is not None:
                    p.next.prev = None
                    self.first = p.next
                elif p.prev is not None and p.next is None:
                    p.prev.next = None
                    self.last = p.prev
                else:
                    self.first = None
                    self.last = None
            p = p.next
