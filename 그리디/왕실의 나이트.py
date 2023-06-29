n = input()

dx = [2, 2, -2, -2 , 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

x, y = int(n[1]), ord(n[0])
count = 0

for i in range(len(dx)):
    
    if ( (0 < x + dx[i] and x + dx[i] < 9) and (96 < y + dy[i] and y + dy[i] < 104)):
        count += 1
        
print(count)