import numpy as np

N = 16
T = np.zeros((N,N), dtype=int)

def fill_spiral(T,N):
    x,y = N//2, N//2
    
    direction = -1
    natural = 2
    move = 1

    T[x][y] = 1
    while True:
        for i in range(move):
            x += direction
            if x > N-1 or x < 0: return
            T[y][x] = natural
            natural += 1

        for i in range(move):
            y += direction
            if y > N-1 or y < 0: return
            T[y][x] = natural
            natural += 1

        direction *= -1
        move += 1
        
fill_spiral(T,N)
print(T)
