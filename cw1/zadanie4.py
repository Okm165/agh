N = 25

s = 0
SUM = 0
while SUM < N:
    SUM += 2*s+1
    s += 1

if(SUM == N): print(s)
else: print("could not find sqrt")