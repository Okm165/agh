import math

def change_base(val, base):
    alphabet = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    length = math.floor(math.log(val)/math.log(base))+1
    ret = [""]*length
    c = 0
    while val > 0:
        ret[c] = alphabet[val%base]
        val //= base
        c += 1
    return ret

print(change_base(12344, 15))