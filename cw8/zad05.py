class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    # wstawienie elementu do zbioru
    def push(self, val):
        if self.first is None:
            node = Node(val)
            self.first = node
            self.last = node
        else:
            node = Node(val)
            self.last.next = node
            self.last = node
    
    def __str__(self) -> str:
        ret = str()
        p = self.first
        while p is not None:
            ret += str(p.val)+", "
            p = p.next
        return ret

def divide(list1) -> list:
    ret = [LinkedList() for _ in range(10)]
    while list1 is not None:
        id = list1.val % 10
        ret[id].push(list1.val)
        list1 = list1.next
    return [i for i in ret if i.first is not None]

def merge(list):
    for i in list:
        list[0].last.next = i.first
        list[0].last = i.last
    return list[0]