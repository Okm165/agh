from zad05 import Node, LinkedList

def merge_it(first_a, first_b):
    if first_a is None or first_b is None: return first_a
    master = first_a
    slave = first_b
    if first_a.val > first_b.val: 
        master = first_b
        slave = first_a
    master_prev = master
    master = master.next
    while master is not None and slave is not None:
        if master.val >= slave.val:
            tmp = slave.next
            slave.next = master
            master_prev.next = slave
            master_prev = slave
            slave = tmp
        else:
            master_prev = master
            master = master.next
    if slave is not None:
        master_prev.next = slave
    return first_a

def _merge_re(prev_a, a, b):
    if b is None: return
    if a is None: 
        prev_a.next = b
        return
    if a.val >= b.val:
        tmp = b.next
        b.next = a
        prev_a.next = b
        prev_a = b
        b = tmp
    else:
        prev_a = a
        a = a.next
    _merge_re(prev_a, a, b)

def merge_re(first_a, first_b):
    master = first_a
    slave = first_b
    if first_a.val > first_b.val:
        master = first_b
        slave = first_a
    _merge_re(master, master.next, slave)

LL1 = LinkedList()
LL1.push(1)
LL1.push(4)
LL1.push(4)

LL2 = LinkedList()
LL2.push(1)
LL2.push(3)
LL2.push(3)
LL2.push(4)
LL2.push(7)
LL2.push(13)

merge_re(LL1.first, LL2.first)
print(LL1)