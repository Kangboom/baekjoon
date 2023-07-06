def get_selfnumber(x):
    l = len(str(x))
    start = 1

    if l == 1:
        start = 1
    elif l == 2:
        start = 1
    elif l == 3:
        start = x - 27
    else :
        start = x - 36

    for i in range(start,x):
        
        str_i = str(i)
        temp = 0
        for n in str_i:
            temp += int(n)
        if temp + i == x:
            return False
    return True

for i in range(1,10001):
    if get_selfnumber(i):
        print(i)