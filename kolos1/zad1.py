import math

def is_prime(N:int)->bool:
    n = 2
    while n*n <= N:
        if not N % n: return False
        n += 1
    return True

def count(N:int)->int:
    prime_count = 0
    N_len = math.floor(math.log(N)/math.log(10))+1
    N_list = [0]*N_len
    for i in range(N_len):
        N_list[N_len-i-1] = N%10
        N //= 10
    for cut in range(N_len):
        mask = 1
        for m in range(N_len-cut-1):
            mask *= 2
            mask += 1
        for j in range(cut+1):
            mask_copy = mask
            val = 0
            val_list = [0]*10
            for N_elem in N_list:
                if mask_copy%2:
                    val *= 10
                    val += N_elem
                    val_list[N_elem] += 1
                mask_copy //= 2
            mask *= 2
            if max(val_list)<2 and is_prime(val): prime_count += 1
    return prime_count