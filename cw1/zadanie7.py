A = int(input("A:"))

a,b = 0,1
while a*b < A:
    a,b = b,a+b
if(a*b == A): print(a,b)