def sieve(N):
    exclude = []
    for i in range(2,N):
        for ex in exclude:
            if i%ex == 0:
                break
        else:
            exclude.append(i)
            print(i)

sieve(1000)