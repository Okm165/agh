class Node:
    def __init__(self, val, cnt=1):
        self.val = val
        self.cnt = cnt
        self.next = None

class LinkedList:
    def __init__(self, first=None, last=None):
        guard = Node(None,None)
        self.first = guard
        self.last = guard
    
    def find(self, val):
        p = self.first
        q = self.first.next
        while q is not None:
            if q.val == val: return (p,q)
            p = q
            q = q.next
        return None

    # czy element należy do zbioru
    def exists(self, val)->bool:
        if self.find(val) is not None: return True
        return False
    
    # wstawienie elementu do zbioru
    def push(self, val):
        f = self.find(val)
        if f is not None:
            f[1].cnt += 1
        else:
            node = Node(val)
            self.last.next = node
            self.last = node
    
    # usunięcie elementu ze zbioru
    def pop(self, val):
        f = self.find(val)
        if f is not None:
            f[1].cnt -= 1
            if f[1].cnt <= 0:
                f[0].next = f[1].next

    # def __str__(self)->str:
    #     ret = ""
    #     p = self.first.next
    #     while p is not None:
    #         ret += f'val: {p.val}, cnt: {p.cnt}\n'
    #         p = p.next
    #     return ret