MAX_LENGTH = 30

def is_prime(N:int)->bool:
    if N < 2: return False
    n = 2
    while n*n <= N:
        if N % n == 0: return False
        n += 1
    return True

# convert byte list to value from sta_ind inclusive to end_ind NOT inclusive
def list_to_val(lista:list, sta_ind:int, end_ind:int)->int:
    diff = end_ind - sta_ind
    val = 0
    for i in range(diff):
        val += lista[sta_ind+i]
        val *= 2
    val //= 2
    return val

# main checking function
def primcut(lista:list, sta_ind:int, end_ind:int)->bool:
    for i in range(3, MAX_LENGTH+3):
        if sta_ind + i >= end_ind:
            if is_prime(list_to_val(lista, sta_ind, i)): return True
            return False
        if is_prime(list_to_val(lista, sta_ind, i)):
            if primcut(lista, i, end_ind): return True

T = [1,1,0,1,0,0]
print(primcut(T, 0, len(T)))