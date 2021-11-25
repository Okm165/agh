def checkifdiff(a,b,i):
    a_list = [0 for _ in range(17)]
    while a > 0:
        a_list[a%i] += 1
        a //= i
    while b > 0:
        if a_list[b%i] != 0: return False
        b //= i
    return True

A, B = 123,522
for i in range(2, 17):
    if checkifdiff(A,B,i): 
        print(i)
        break
else: print("no base")
