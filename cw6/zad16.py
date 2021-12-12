vowels = ["a", "e", "i", "o", "u", "y"]

def check(w_s1:tuple, s2:str, w_s2:tuple, new_s2:str, cnt:int=0)->bool:
    if w_s1 == w_s2:
        print(new_s2)
        return True
    elif cnt >= len(s2) or w_s1[0] < w_s2[0] or w_s1[1] < w_s2[1]: return False
    
    vow = 0
    if s2[cnt] in vowels: vow = 1
    new_w_s2 = (w_s2[0]+ord(s2[cnt]), w_s2[1]+vow)
    upd_new_s2 = new_s2 + s2[cnt]

    return check(w_s1, s2, w_s2, new_s2, cnt+1) or check(w_s1, s2, new_w_s2, upd_new_s2, cnt+1)

def wyraz(s1:str, s2:str)->bool:
    vow = 0
    asc = 0
    for i in s1:
        asc += ord(i)
        if i in vowels: vow += 1

    return check((asc, vow), s2, (0,0), "")

print(wyraz("ula", "xes"))