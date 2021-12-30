class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    # inicjalizującą tablicę
    def __init__(self):
        guard = Node(None)
        self.first = guard

    def find(self, ind):
        p = self.first.next
        while ind > 0:
            if p is None: return None
            p = p.next
            ind -= 1
        return p
    
    # zwracającą wartość elementu o indeksie n
    def ind(self, n):
        f = self.find(n)
        if f is not None: return f.val
        return None
    
    # podstawiającą wartość value pod indeks n
    def subs(self, val, n):
        f = self.find(n)
        if f is not None: f.val = val