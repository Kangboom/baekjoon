def dfs(h,w):

    stack = []
    if graph[h][w] != 1:
        return False

    stack.append((h,w))
    graph[h][w] = 2 # 방문하면 2

    while(stack):
        h, w = stack.pop()
        for i in range(8):
            nh = h + dh[i]
            nw = w + dw[i] 
            if(nh<0 or nh>x-1 or nw<0 or nw>y-1):
                continue 
            if(graph[nh][nw] == 0):
                continue
            if(graph[nh][nw] == 1):
                stack.append((nh,nw))
                graph[nh][nw] = 2 
    
    return True

result = []
while(True):
    y, x = map(int,input().split())
    if( y == 0 and x == 0):
        break
    graph = [list(map(int, input().split())) for _ in range(x)]
    #상,하,좌,우,위 대각선, 아래 대각선
    dh = [-1, 1, 0, 0, -1, -1, 1, 1]
    dw = [0, 0, -1, 1, -1, 1, -1, 1]

    count = 0
    for i in range(x):
        for j in range(y):
            if(dfs(i,j) == True):
                count += 1
    result.append(count)

for i in result:
    print(i)
