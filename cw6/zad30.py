# poprawiona treść zadania
"""
Zadanie 30.
Punkt leżący na płaszczyźnie jest opisywany parą liczb typu float (x,y). 
Tablica T[N] zawiera współrzędne N punktów leżących na płaszczyźnie. 
Punkty posiadają jednostkową masę. Proszę napisać funkcję, 
która sprawdza czy istnieje niepusty podzbiór n punktów, 
gdzie n < k  oraz n jest wielokrotnością liczby 3, 
którego środek ciężkości leży w odległości mniejszej niż r od początku układu współrzędnych. 
Do funkcji należy przekazać dokładnie 3 parametry: tablicę t, promień r, oraz ograniczenie k, 
funkcja powinna zwrócić wartość typu bool.
"""

from math import sqrt

def dst(p1:tuple, p2:tuple)->float:
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def find(table:list, r:int, k:int, x:float=0, y:float=0, cnt:int = 0)->bool:
    if cnt >= k: return False
    if dst((x/cnt, y/cnt), (0,0)) < r: return True
    
    for i in range(len(table)):
        if table[i]:
            tmp_i = table[i]
            table[i] = False
            for j in range(i, len(table)):
                if table[j]:
                    tmp_j = table[j]
                    table[j] = False
                    for k in range(j, len(table)):
                        if table[k]:
                            tmp_k = table[k]
                            table[k] = False
                            if find(table, r, k, x+tmp_i[0]+tmp_j[0]+tmp_k[0], y+tmp_i[1]+tmp_j[1]+tmp_k[1], cnt+3): return True
                            table[k] = tmp_k
                    table[j] = tmp_j
            table[i] = tmp_i
    return False
