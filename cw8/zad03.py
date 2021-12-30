class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        guard = Node(None)
        self.first = guard
        self.last = guard

    # wstawienie elementu do zbioru
    def push(self, val):
        node = Node(val)
        self.last.next = node
        self.last = node
    
    def __str__(self) -> str:
        ret = str()
        p = self.first.next
        while p is not None:
            ret += str(p.val)+", "
            p = p.next
        return ret

def merge(list1, list2) -> Node:
    m_list = LinkedList()
    while list1 is not None and list2 is not None:
        if list1.val > list2.val:
            m_list.push(list2.val)
            list2 = list2.next
        else:
            m_list.push(list1.val)
            list1 = list1.next
    
    while list1 is not None:
        m_list.push(list1.val)
        list1 = list1.next
    
    while list2 is not None:
        m_list.push(list2.val)
        list2 = list2.next

    return m_list.first.next

def _merge_rec(list1, list2, list3):
    if list1 is None:
        while list2 is not None:
            list3.push(list2.val)
            list2 = list2.next
        return
    elif list2 is None:
        while list1 is not None:
            list3.push(list1.val)
            list1 = list1.next
        return
    
    if list1.val > list2.val:
        list3.push(list2.val)
        list2 = list2.next
    else:
        list3.push(list1.val)
        list1 = list1.next
    
    _merge_rec(list1, list2, list3)
    return


def merge_rec(list1, list2) -> Node:
    list3 = LinkedList()
    _merge_rec(list1,list2,list3)
    return list3.first.next