N = 100000
a,b = 0,1
for i in range(N):
    a,b = b,a+b
print(b/a)