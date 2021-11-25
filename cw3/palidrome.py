W = [23,23,145,4,5,2,2,3,3,2,2,5,4]

# find longest palindrome in list
def search_palin(N:list) -> int:
    i = 0
    longest = 0
    while i < len(N):
        m = i-2
        longest_local = 0
        while m >= 0 and i < len(N) and N[m] == N[i]:
            longest_local += 1
            i += 1
            m -= 1
        if(longest_local*2+1 > longest): longest = longest_local*2+1

        m = i-1
        longest_local = 0
        while m >= 0 and i < len(N) and N[m] == N[i]:
            longest_local += 1
            i += 1
            m -= 1
        if(longest_local*2 > longest): longest = longest_local*2
        
        i += 1
    
    return longest

print(search_palin(W))
        