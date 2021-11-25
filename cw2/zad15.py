def armstrong(N):
    decade = 10
    powers = [0,1,2,3,4,5,6,7,8,9]
    NUMS = []
    for i in range(N):
        if i == decade:
            decade *= 10
            for i in range(10):
                powers[i] *= i
        
        s = i
        sum = 0
        while s > 0:
            sum += powers[s%10]
            if sum > i: break
            s = s//10

        if sum == i: NUMS.append(i)
    return NUMS

print(armstrong(548834))