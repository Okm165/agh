# Brian Kernighan’s Algorithm O(logn)
def num_of_ones(val:int)->int:
    cnt = 0
    while val > 0:
        val &= val-1
        cnt += 1
    return cnt

# można podzielić na 3 podzbiory puste i zad jest trywialne, 
# ale uznam że polecenie brzmi "podział zbioru N liczb na trzy NIEPUSTE podzbiory"
def search(table:list, cnt:int=0, a:int=0, b:int=0, c:int=0)->bool:
    if a == b == c and a and b and c: return True
    if cnt >= len(table): return False

    return (
        search(table, cnt+1, a+num_of_ones(table[cnt]), b, c) or
        search(table, cnt+1, a, b+num_of_ones(table[cnt]), c) or
        search(table, cnt+1, a, b, c+num_of_ones(table[cnt])) or
        search(table, cnt+1, a,b,c)
    )

print(search([5,7,15]))