n = int(input())
plans = input().split()

x,y = 1, 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
move = ['R', 'L', 'U', 'D']

for plan in plans:
    
    for i in range(len(move)):
        if( plan == move[i]):
            nx = x + dx[i]
            ny = y + dy[i]
    if (nx <1 or ny < 1 or nx > 5 or nx > 5):
        continue

    x = nx
    y = ny 
    
print(x, y)