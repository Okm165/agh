# global list T[8][8]
# king can go down or to the right
# in other words increment row or/and column if possible
import math

def get_first_digit(val)->int:
    num_of_digits = math.floor(math.log10(val))
    return val // 10**num_of_digits

# board dimensions
N = 8
# dst = (7,7)

# possible relative movements
moves = ((1,0), (0,1), (1,1))

def find(board:list, w:int, k:int)->bool:
    if w == N-1 and k == N-1: return True
    if w >= N or k >= N: return False

    curr = board[w][k] % 10
    for d_w, d_k in moves:
        if get_first_digit(board[w+d_w][k+d_k]) == curr:
            if find(board, w+d_w, k+d_k): return True
    return False