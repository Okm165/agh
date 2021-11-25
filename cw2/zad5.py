def cut_one(a):
    ret = []
    for i in range(len(a)):
        sub = a[0:i]+a[i+1:]
        if sub != '': ret.append(sub)
    return ret


def sub_num(a, ret):
    num = a
    if(num not in ret): ret.append(num)
    sub = cut_one(num)
    for j in sub:
        sub_num(j, ret)

def checkdiv(a,d):
    ret = []
    for i in a:
        if(int(i)%d == 0): ret.append(i)
    return ret
        

ret = []
sub_num(str(2315), ret)
print(checkdiv(ret, 7))
