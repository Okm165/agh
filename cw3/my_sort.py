lista = [120,12,22,4,6,32,55,23,12,6,7,8,6,5,34,23,12,1]

def my_sort(lista) -> list:
    n = 0
    while n < len(lista)-1:
        if lista[n] > lista[n+1]:
            lista[n], lista[n+1] = lista[n+1], lista[n]
            if n > 0: n -= 1
            else: n += 1
        else: n += 1 
    return lista

print(my_sort(lista))