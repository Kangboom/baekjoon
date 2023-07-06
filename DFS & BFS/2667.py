def dfs(x, y):

    if(graph[x][y] != 1):
        return False
    
    graph[x][y] = 2
    stack = []
    stack.append((x,y))
    count = 1

    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(nx<0 or nx>N-1 or ny<0 or ny > N-1):
                continue
            if(graph[nx][ny] == 0):
                continue
            if(graph[nx][ny] == 1):
                count += 1
                stack.append((nx,ny))
                graph[nx][ny] = 2
    
    result.append(count)
    return True


N = int(input())
graph = [ list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
result = []

for i in range(N):
    for j in range(N):
        if (dfs(i,j) == True):
            count += 1

print(count)
for i in sorted(result):
    print(i)