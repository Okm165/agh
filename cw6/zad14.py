# from-buffer-to
def hanoi(disks:int, one:list, two:list, three:list):
    if disks > 0:
        hanoi(disks-1, one, three, two)
        three.insert(0, one.pop(0))
        hanoi(disks-1, two, one, three)

one = [5,4,3,2,1]
two = []
three = []
hanoi(5, one, two, three)
print(one, two, three)