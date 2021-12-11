# pos row/col (x/y)
N = 8
board = [[0 for _ in range(N)] for _ in range(N)]

def set_queen(board:list, pos:tuple, set_unset:int):
    for i in range(pos[0], N): board[i][pos[1]] += set_unset

    for diag in range(pos[0], min(8, N-pos[1]+pos[0])):
        board[(diag)][diag+pos[1]-pos[0]] += set_unset

    for diag in range(pos[0], min(8, 1+pos[1]+pos[0])):
        board[diag][-diag+pos[1]+pos[0]] += set_unset

    board[pos[0]][pos[1]] -= 2*set_unset

def search(board:list, row_cnt:int, queens:list):
    if len(queens) == N: 
        print(queens)
        return 
    
    for i in range(len(board[0])):
        if not board[row_cnt][i]:
            queens.append(i)
            set_queen(board, (row_cnt, i), 1)
            search(board, row_cnt+1, queens)
            queens.pop()
            set_queen(board, (row_cnt, i), -1)

queens = []
search(board, 0, queens)