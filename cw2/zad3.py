# def is_palindrome(a) -> bool:
#     if(a == a[::-1]): return True
#     return False

# def to_binary(a) -> str:
#     return bin(a)[2:]

# print(is_palindrome(str(value)))
# print(is_palindrome(to_binary(value)))

# def is_palin(a) -> bool:
#     tmp = a
#     tmp2 = 0

#     while tmp > 0:
#         tmp2 += (tmp%10)
#         tmp //= 10
#         tmp2 *= 10
#     tmp2 //= 10

#     if(a == tmp2): return True
#     return False

# def is_palin_bin(a) -> bool:
#     tmp = a
#     tmp2 = 0
#     while(tmp > 0):
#         tmp2 += (tmp%2)
#         tmp = tmp >> 1
#         tmp2 = tmp2 << 1
#     tmp2 = tmp2 >> 1

#     if(a == tmp2): return True
#     return False

def is_palin_univ(a, system) -> bool:
    tmp1 = a
    tmp2 = 0

    while tmp1 > 0:
        tmp2 += tmp1%system
        tmp1 //= system
        tmp2 *= system
    tmp2 //= system

    if(a == tmp2): return True
    return False

value = int(input("A:"))
print(is_palin_univ(value, 2))