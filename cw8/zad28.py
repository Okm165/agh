from typing import NoReturn
from zad05 import LinkedList, Node

def delete(first_s, first_r) -> int:
    cnt = 0
    prev_r = None
    curr_r = first_r
    while curr_r is not None:
        prev_s = None
        curr_s = first_s
        while curr_s is not None and curr_r.val < curr_s.val:
            prev_s = curr_s
            curr_s = curr_s.next
        if curr_s is not None and curr_s.val == curr_r.val:
            cnt += 1
            if prev_s is None: first_s = curr_s.next
            else: prev_s.next = curr_s.next
            if prev_r is None: first_r = curr_r.next
            else: prev_r.next = curr_r.next
            curr_r = curr_r.next
        else:
            prev_r = curr_r
            curr_r = curr_r.next
    return cnt