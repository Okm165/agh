def find_max(E) -> int:
    curr = 0
    max_val = E[curr]
    for i in E:
        if i > max_val:
            max_val = i
            curr = i
    return curr

def find_min(E) -> int:
    curr = 0
    min_val = E[curr]
    for i in E:
        if i < min_val:
            min_val = i
            curr = i
    return curr

def find(T, N) -> tuple:
    row_sum = [0 for _ in range(N)]
    col_sum = [0 for _ in range(N)]

    for i in range(N):
        for j in range(N):
            row_sum[i] += T[i][j]
            col_sum[j] += T[i][j]

    return (find_min(row_sum), find_max(col_sum))
    
