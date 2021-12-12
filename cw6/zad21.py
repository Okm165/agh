import numpy as np

def row_valid(row:list)->bool:
    return max(row) != -1

def elem_valid(elem:int)->bool:
    return elem != -1

def mark(table:list, row:int, col:int)->list:
    buffer = []
    for col_ind in range(len(table[0])):
        buffer.append(board[row][col_ind])
        board[row][col_ind] = -1
    
    for row_ind in range(len(board)):
        if row != row_ind:
            buffer.append(board[row_ind][col])
            board[row_ind][col] = -1
    return buffer

def unmark(table:list, row:int, col:int, buffer:list):
    for col_ind in range(len(table[0])):
        board[row][col_ind] = buffer[col_ind]
    
    cnt = 0
    for row_ind in range(len(board)):
        if row != row_ind:
            board[row_ind][col] = buffer[len(table[0])-1+cnt]
            cnt += 1

def take(table:list, total:int)->bool:
    if total == 0: return True
    if total < 0: return False

    for row_ind in range(len(table)):
        if row_valid(table[row_ind]):
            for col_ind in range(len(table[row_ind])):
                if elem_valid(table[row_ind][col_ind]):
                    val = table[row_ind][col_ind]
                    buffer = mark(table, row_ind, col_ind)
                    if take(table, total-val): return True
                    unmark(table, row_ind, col_ind, buffer)
    return False


board = [
    [1,5,3,2,4],
    [4,5,2,1,4],
    [2,9,3,7,3],
    [4,8,9,7,2],
    [1,1,7,6,2],
]
print(take(board, 2))