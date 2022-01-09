from zad05 import Node

class CyclicList:
    def __init__(self, first = None) -> None:
        self.first = first

    def push(self, val) -> bool:
        if self.first is None:
            self.first = Node(val)
            self.first.next = self.first
            return True
        else:
            prev = self.first
            curr = self.first.next
            while True:
                if prev.val[len(prev.val)-1] < val[0] and val[len(val)-1] < curr.val[0]:
                    node = Node(val)
                    node.next = curr
                    prev.next = node
                    self.first = node
                    return True
                if curr == self.first: break
                prev = curr
                curr = curr.next
            return False

    def __str__(self) -> str:
        ret = self.first.val
        curr = self.first.next
        while curr != self.first:
            ret += " -> "
            ret += curr.val
            curr = curr.next
        ret += ";"
        return ret

cc = CyclicList()
print(cc.push("bartek"))
print(cc.push("zosia"))
print(cc.push("leszek"))
print(cc.push("marek"))
print(cc.push("ola"))
print(cc.push("ala"))
print(cc)
