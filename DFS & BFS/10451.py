def dfs(start):
    stack = []
    stack.append(start)
    visited[start] = True

    while(stack):
        v = stack.pop()
        if not visited[num[v]]:
            visited[num[v]] = True
            stack.append(num[v])
        

T = int(input())
result = []
for i in range(T):
    N = int(input())
    order = [ i for i in range(0,N+1)]
    num = [0]
    num.extend(list(map(int, input().split())))
    visited = [False] * (N+1)    
    
    count = 0
    for i in range(1, N+1):
        if visited[i] == True :
            continue
        dfs(i)
        count += 1
    result.append(count)

for i in range(T):
    print(result[i])
