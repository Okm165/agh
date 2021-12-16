# example data for test
N = 5
# T[N][N]
T = [
    [7,8,9,10,11],
    [3,9,11,14,20],
    [1,4,7,11,12],
    [1,1,1,1,1],
    [11,12,13,14,15]
]

sort_list = [0]*(N*N)

def linearize(table:list, sort_list:list)->None:
    ind = [0]*len(table)
    cnt = 0
    while min(ind) < N:
        minimal = 0
        stack = []

        for i in range(len(ind)):
            if ind[i] > N-1: continue

            if not minimal or minimal > table[i][ind[i]]:
                minimal = table[i][ind[i]]
                stack.clear()
            
            ind_tmp = ind[i]
            while ind_tmp < N and minimal == table[i][ind_tmp]:
                stack.append(i)
                ind_tmp += 1

        for s in stack:
            ind[s] += 1
            sort_list[cnt] = minimal
            cnt += 1

linearize(T, sort_list)
print(sort_list)