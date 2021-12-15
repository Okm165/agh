def eval_serie(n):
    counter = 0
    while n > 1:
        n = n%2*(3*n+1)+(1-n%2)*(n//2)
        counter+=1
    return counter


def find_longest():
    l_count = 0
    l_i = 0
    for i in range(2,10000+1):
        p = eval_serie(i)
        if(p > l_count):
            l_count = p
            l_i = i
    return (l_i, l_count)

print(find_longest())