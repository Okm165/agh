def check(val) -> bool:
    arr = [0]*3
    while val > 0:
        arr[val % 3] += 1
        arr //= 3
    if arr[1] > arr[2]: return True
    return False

def delete(first):
    prev = first
    curr = first.next
    while curr is not None:
        if check(curr.val):
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next
            