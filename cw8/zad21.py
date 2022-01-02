from zad05 import LinkedList

class Candidate:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

def del_longest(first):
    if first is None or first.next is None: return
    prev = first
    curr = first.next
    longest = 0
    two_of_them = False
    length = 0
    start = prev
    end = prev
    candidate = Candidate(start, end)
    while curr is not None:
        if prev.val < curr.val:
            length += 1
            end = curr
        else:
            if length == longest:
                two_of_them = True
            elif length > longest:
                candidate.start = start
                candidate.end = end
                longest = length
                two_of_them = False

            start = curr
            end = curr
            length = 0
        
        prev = curr
        curr = curr.next
    
    if length == longest:
        two_of_them = True
    elif length > longest:
        candidate.start = start
        candidate.end = end
        longest = length
        two_of_them = False

    if not two_of_them:
        candidate.start.next = candidate.end.next
        return longest+1
    return 0

LL = LinkedList()
LL.push(1)
LL.push(2)
LL.push(3)
LL.push(4)
LL.push(3)
LL.push(2)
LL.push(3)
LL.push(4)
LL.push(5)
LL.push(6)
LL.push(3)
print(LL)
del_longest(LL.first)
print(LL)
