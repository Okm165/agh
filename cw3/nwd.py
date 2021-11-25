# def nwd(a,b):
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a

def nwd(a:int,b:int)->int:
    while b > 0: a,b = b, a%b
    return a

def lcm(a:int,b:int)->int:
    return (a*b)//nwd(a,b)

def nwd3(a:int,b:int,c:int)->int:
    return nwd(nwd(a,b),c)

def nwd4(a:int,b:int,c:int,d:int)->int:
    return nwd(nwd(nwd(a,b),c),d)

print(nwd(936, 241230))