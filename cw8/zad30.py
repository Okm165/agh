from zad05 import LinkedList, Node

def merge(first_s, first_r):
    if first_s is None: return
    curr_r = first_r
    while curr_r is not None:
        prev_s = None
        curr_s = first_s
        while curr_s is not None and curr_s.val < curr_r.val:
            prev_s = curr_s
            curr_s = curr_s.next
        
        if curr_s is None: prev_s.next = Node(curr_r.val)
        else:
            if curr_s.val != curr_r.val:
                if prev_s is None:
                    first_s = Node(curr_r.val)
                    first_s.next = curr_s
                else:
                    node = Node(curr_r.val)
                    node.next = curr_s
                    prev_s.next = node
        curr_r = curr_r.next

LL1 = LinkedList()
LL1.push(2)
LL1.push(3)
LL1.push(5)
LL1.push(7)
LL1.push(11)

LL2 = LinkedList()
LL2.push(8)
LL2.push(2)
LL2.push(7)
LL2.push(4)

merge(LL1.first, LL2.first)
print(LL1)
