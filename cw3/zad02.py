def listify(val) -> list:
    dig = [0]*10
    while val > 0:
        dig[val%10] += 1
        val //= 10
    return dig

a = int(input("A:"))
b = int(input("B:"))

l_a = listify(a)
l_b = listify(b)

if l_a == l_b:
    print("Yup")
else:
    print("Nope")