class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.first = None

    def push(self, val) -> bool:
        if self.first is None:
            self.first = Node(val)
            return True
        if val == self.first.val: return False
        if val > self.first.val and self.first.next is None:
            self.first.next = Node(val)
            return True
        if val < self.first.val:
            tmp = self.first
            self.first = Node(val)
            self.first.next = tmp
            return True
        
        prev = self.first
        curr = self.first.next

        while curr is not None:
            if val == curr.val: return False
            if val > prev.val and val < curr.val:
                node = Node(val)
                prev.next = node
                node.next = curr
                return True
            prev = curr
            curr = curr.next
        
        prev.next = Node(val)
        return True

    def __str__(self) -> str:
        ret = str()
        node = self.first
        while node is not None:
            ret += node.val + ", "
            node = node.next
        return ret