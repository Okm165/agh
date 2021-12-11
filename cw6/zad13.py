stack = []
def devide(val:int, bot:int, stack:list)->bool:
    if val < 0: return False

    elif val == 0: 
        print(stack)
        return True

    for i in range(bot, val+1):
        stack.append(i)
        if not devide(val-i, i, stack): break
        stack.pop()
    return True

devide(6, 1, stack)