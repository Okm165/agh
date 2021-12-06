import math
import random
import numpy as np

horse_moves = [
    # row, col relative movements
    (-1,-2),
    (-2,-1),
    (-2,1),
    (-1,2),
    (1,2),
    (2,1),
    (2,-1),
    (1,-2)
]

def possib(board:list, pos:tuple)->list:
    possible = []
    for move in horse_moves:
        new_pos = (pos[0] + move[0], pos[1] + move[1])
        if (new_pos[0] >= 0 and 
            new_pos[0] < len(board) and 
            new_pos[1] >= 0 and 
            new_pos[1] < len(board[0]) and 
            board[new_pos[0]][new_pos[1]] == 0):
            possible.append(new_pos)
    return possible

def sort_possib(new_positions:list, possib_of_new_pos: list):
    ind = 0
    while ind < len(possib_of_new_pos)-1:
        if possib_of_new_pos[ind] > possib_of_new_pos[ind+1]:
            possib_of_new_pos[ind], possib_of_new_pos[ind+1] = possib_of_new_pos[ind+1], possib_of_new_pos[ind]
            new_positions[ind], new_positions[ind+1] = new_positions[ind+1], new_positions[ind]
            if ind > 0: ind -= 1
            else: ind += 1
        else: ind += 1

def fill(board:list, pos:tuple, cnt:int)->bool:
    board[pos[0]][pos[1]] = cnt
    if np.min(board) > 0: return True
    for new_pos in possib(board, pos):
        if fill(board, new_pos, cnt+1): return True
    board[pos[0]][pos[1]] = 0
    return False

def fill_heuristic(board:list, pos:tuple, cnt:int)->bool:
    board[pos[0]][pos[1]] = cnt
    if np.min(board) > 0: return True

    new_positions = possib(board, pos)
    possib_of_new_pos = []
    for new_pos in new_positions:
        possib_of_new_pos.append(len(possib(board, new_pos)))
    sort_possib(new_positions, possib_of_new_pos)

    for new_pos in new_positions:
        if fill(board, new_pos, cnt+1): return True
    board[pos[0]][pos[1]] = 0
    return False

# setup chessboard
N = 5
board = np.zeros((N,N), dtype=int)

# select random start point
start = (random.randrange(0, N), random.randrange(0, N))
print(fill(board, start, 1))
print(board)