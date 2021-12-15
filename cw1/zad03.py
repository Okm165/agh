F = [0,1,1]
SUM = 2

A = 4181

while True:
    if SUM == A:
        print(F)
        break
    elif len(F) == 1: 
        break
    elif(SUM < A):
        n = F[-1] + F[-2]
        F.append(n)
        SUM += n
    elif(SUM > A):
        SUM -= F[0]
        F.pop(0)