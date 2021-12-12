import math

# 701
# 6K2
# 543

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
    ((-1,0),(-1,1),(0,1)),   #  0,1,2
    ((0,1),(1,1),(1,0)),     #  2,3,4
    ((1,0),(1,-1),(0,-1)),   #  4,5,6
    ((-1,0),(-1,-1),(0,-1)), #  6,7,8
)

def get_first_digit(val)->int:
    num_of_digits = math.floor(math.log10(val))
    return val // 10**num_of_digits

def pos_valid(w:int, k:int, dim:int)->bool:
    if w >= dim or k >= dim or w < 0 or k < 0: return False
    return True


def find(board:list, w:int, k:int, dst_ind:tuple, path:list)->bool:
    if w == dst[dst_ind][0] and k == dst[dst_ind][1]: return path

    curr = board[w][k] % 10
    for m_id in range(len(moves[dst_ind])):
        new_w = w + moves[dst_ind][m_id][0]
        new_k = k + moves[dst_ind][m_id][1]
        if (pos_valid(new_w, new_k, N) and 
            get_first_digit(board[new_w][new_k]) == curr):
            path.append(2*dst_ind + m_id)
            if tmp := find(board, w+d_w, k+d_k, dst_ind, path): return tmp
            path.pop()
    return False

def var_dst(board: list, w:int, k:int):
    for dst_ind in range(len(dst)):
        if find(board, w, k, dst_ind): return True
    return False
