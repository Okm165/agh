def is_prime(N):
    if N < 2: return False
    n = 2
    while n*n <= N:
        if N%n == 0: return False
        n += 1
    return True

def cut_one(value:list, checked:list):
    for i in range(len(value)):
        cut_list = [0]*(len(value)-1)

        # cut one from list
        cnt = 0
        for j in range(len(value)):
            if j != i:
                cut_list[cnt] = value[j]
                cnt += 1
        
        # compose cut_value
        cut_value = 0
        for m in range(len(cut_list)):
            cut_value += cut_list[len(cut_list)-m-1]
            cut_value *= 10
        cut_value //= 10

        if cut_value not in checked:
            checked.append(cut_value)
            if is_prime(cut_value): print(cut_value)
            cut_one(cut_list, checked)

cut_one([3,2,6,3,7,9,6,3,1], [])