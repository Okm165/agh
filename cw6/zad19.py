import math

# board dimensions
N = 8
# destinations
dst = (
    (0,0),
    (0,N-1),
    (N-1,0),
    (N-1,N-1),
)
# possible relative movements for dst
moves = (
    ((-1,0),(-1,-1),(0,-1)),
    ((-1,0),(-1,1),(0,1)),
    ((1,0),(1,-1),(0,-1)),
    ((1,0),(1,1),(0,1)),
)

def get_first_digit(val)->int:
    num_of_digits = math.floor(math.log10(val))
    return val // 10**num_of_digits

def pos_valid(w:int, k:int, dim:int)->bool:
    if w >= dim or k >= dim or w < 0 or k < 0: return False
    return True


def find(board:list, w:int, k:int, dst_ind:tuple)->bool:
    if w == dst[dst_ind][0] and k == dst[dst_ind][1]: return True

    curr = board[w][k] % 10
    for d_w, d_k in moves[dst_ind]:
        if (pos_valid(w+d_w, k+d_k, N) and 
            get_first_digit(board[w+d_w][k+d_k]) == curr):
            if find(board, w+d_w, k+d_k, dst_ind): return True
    return False

def var_dst(board: list, w:int, k:int):
    for dst_ind in range(len(dst)):
        if find(board, w, k, dst_ind): return True
    return False
