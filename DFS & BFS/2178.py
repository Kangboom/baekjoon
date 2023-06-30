from collections import deque

def bfs(a, b):
    queue = deque()
    queue.append((a,b))

    while(queue):
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(nx<0 or nx>N-1 or ny<0 or ny>M-1):
                continue
            if(graph[nx][ny] == 0):
                continue

            if(graph[nx][ny] == 1):
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1

N, M = map(int, input().split())
graph = [ list(map(int,input())) for _ in range(N)]

# 상,하,좌,우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs(0,0)
print(graph[N-1][M-1])

