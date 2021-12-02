def longest(N:list)->int:
    table = [0]*(2**4)
    for elem in N:
        char_int = 0
        while elem > 0:
            char_int |= (1 << elem%4)
            elem //= 4
        table[char_int] += 1
    return max(table)
