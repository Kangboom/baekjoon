n, m = map(int, input().split())
rice = list(map(int,input().split()))

h = max(rice)

while True:
    temp = 0
    for i in range(n):
        if rice[i] - h > 0:
            temp += (rice[i] - h) 
    if temp >= m:
        break
    else:
        h -= 1
print(h)