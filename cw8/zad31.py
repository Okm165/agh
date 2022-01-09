from zad05 import LinkedList, Node

def split(first, res_ep, res_on) -> int:
    cnt = 0
    prev = None
    curr = first
    while curr is not None:
        if curr.val > 0 and curr.val%2 == 0:
            if res_ep.next is None: 
                res_ep.next = Node(curr.val)
            else:
                while res_ep.next is not None:
                    res_ep = res_ep.next
                res_ep.next = Node(curr.val)
            
            prev = curr
            curr = curr.next
            
        elif curr.val < 0 and curr.val%2 == 1:
            if res_on.next is None: 
                res_on.next = Node(curr.val)
            else:
                while res_on.next is not None:
                    res_on = res_on.next
                res_on.next = Node(curr.val)

            prev = curr
            curr = curr.next
            
        else:
            cnt += 1
            if prev is None:
                first = curr.next
                prev = None
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next
    return cnt

LL1 = LinkedList()
LL1.push(-11)
LL1.push(2)
LL1.push(3)
LL1.push(4)
LL1.push(6)
LL1.push(-12)
LL1.push(-13)
LL1.push(-15)

res_ep = Node("guard")
res_on = Node("guard")

cnt = split(LL1.first, res_ep, res_on)
print()
print(cnt)
print()
while res_ep is not None:
    print(res_ep.val)
    res_ep = res_ep.next
print()
while res_on is not None:
    print(res_on.val)
    res_on = res_on.next