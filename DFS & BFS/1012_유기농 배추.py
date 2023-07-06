def dfs(x,y):

    if(graph[x][y] != 1):
        return False

    stack = []
    stack.append((x,y))
    graph[x][y] = 2

    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx<0 or nx >N-1 or ny<0 or ny>M-1):
                continue
            if (graph[nx][ny] != 1):
                continue
            stack.append((nx,ny))
            graph[nx][ny] = 2

    return True

result = []
T = int(input())
for _ in range(T):
    # M 가로, N 세로, K 배추개수
    M, N, K = map(int, input().split())

    graph = [ [0 for i in range(M)] for j in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if dfs(i,j):
                cnt += 1
        
    
    result.append(cnt)

for i in result:
    print(i)
