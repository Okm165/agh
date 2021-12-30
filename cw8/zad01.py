class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        guard = Node(None)
        self.first = guard
        self.last = guard
    
    def find(self, val):
        p = self.first
        q = self.first.next
        while q is not None:
            if q.val == val: return (p,q)
            p = q
            q = q.next
        if q.val == val: return (p,q)
        return None

    # czy element należy do zbioru
    def exists(self, val)->bool:
        if self.find(val) is not None: return True
        return False
    
    # wstawienie elementu do zbioru
    def push(self, val):
        if self.find(val) is None:
            node = Node(val)
            self.last.next = node
            self.last = node
    
    # usunięcie elementu ze zbioru
    def pop(self, val):
        f = self.find(val)
        if f is not None:
            f[0].next = f[1].next

    # def __str__(self)->str:
    #     ret = ""
    #     p = self.first.next
    #     while p is not None:
    #         ret += f'val: {p.val}, cnt: {p.cnt}\n'
    #         p = p.next
    #     return ret