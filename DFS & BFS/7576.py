def tomato(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]    
        if(nx<0 or nx>N-1 or ny<0 or ny>M-1):
            continue
        if(graph[nx][ny] == -1):
            continue
        if(graph[nx][ny] == 0 ):
            graph[nx][ny] = 1
            new.append((nx,ny))    

M, N = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# graph에서 1 인 좌표 찾기
temp = []
for i in range(N):
    for j in range(M):
        if(graph[i][j] == 1):
            temp.append((i,j))

day = 0
new = []
while(temp):
    for _ in range(len(temp)):
        x , y = temp.pop()
        tomato(x,y)
    if(new):
        day += 1
        temp = new.copy()
        new = []


for i in graph:
    if 0 in i:
        day = -1
print(day)

# new는 하루 지나면 익을 토마토를 담는 리스트
# temp는 현재 익어있는 토마토를 담는 리스트(익은토마토 중 옆에 안익은 토마토가 있는)
# while문 탈출 조건 즉 토마토가 다 익었을 때와, 익지않는 토마토가 있을 때 조건을 찾아야 됨
