# def calc(a,b,n):
#     val = str(a*(10**n)//b)
#     return val[:len(val)-n]+","+val[len(val)-n:]

def calc(a ,b, n):
    quo = a//b
    rem = (a-b*quo)*(10**n)
    rozw = rem//b
    return(quo, rozw)


print(calc(
    int(input("A:")),
    int(input("B:")),
    int(input("N:"))
))