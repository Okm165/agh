import math

def period(a):
    dig = math.floor(math.log10(a))+1
    digits = [0]*dig

    # fill list, digits
    cnt = 0
    while a>0:
        digits[dig-cnt-1] = a%10
        a //= 10
        cnt += 1

    result = 0
    cnd = []
    for i in range(len(digits)):
        
        cnd_to_be_poped = []
        for c in range(len(cnd)):
            if digits[cnd[c][0] + (i-cnd[c][1])] != digits[i]: cnd_to_be_poped.append(cnd[c])
            if i - cnd[c][1] >= cnd[c][1] - cnd[c][0]:
                result = cnd[c]
                break

        for p in range(len(cnd_to_be_poped)):
            cnd.pop(cnd.index(cnd_to_be_poped[p]))

        for x in range(len(digits[:i])):
            if digits[x] == digits[i]: cnd.append((x, i))

    rozw = str()
    for i in range(result[0]):
        rozw += chr(digits[i]+48)
    rozw += '('
    for o in range(result[0], result[1]):
        rozw += chr(digits[o]+48)
    rozw += ')'
    return rozw

# def calc(a ,b, n):
#     quo = a//b
#     rem = (a-b*quo)*(10**n)
#     rozw = rem//b
#     return(quo, rozw)


# calculated = calc(
#     int(input("A:")),
#     int(input("B:")),
#     int(input("N:"))
# )

# print(calculated)
# print(calculated[0], ",", period(calculated[1]))


# # print(period(27779906842105263157894736842105263157894736842105263157894736842105263157894736842105263157894736842105263))