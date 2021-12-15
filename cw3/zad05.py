# def sort(l):
#     ind = 0
#     while ind+1 < len(l):
#         if(l[ind] > l[ind+1]):
#             l[ind], l[ind+1] = l[ind+1], l[ind]
#             if ind > 0:
#                 ind -= 1
#             else: 
#                 ind += 1
#         else:
#             ind += 1


# # load
# values = []
# while True:
#     x = int(input("V:"))
#     if x == 0: break
#     values.append(x)

# sort(values)

# print(values[-9])


def place_into(lista:list, input_val:int) -> None:
    target_index = len(lista)
    for i in range(len(lista)):
        if input_val < lista[i]:
            target_index = i
            break
    
    for u in range(1,target_index):
        lista[u-1] = lista[u]
    
    lista[target_index-1] = input_val

lista = [0 for _ in range(10)]
while True:
    input_val = int(input(":"))
    if input_val == 0: break
    place_into(lista, input_val)
    print(lista)
print(lista[0])