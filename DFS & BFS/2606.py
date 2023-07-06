def bfs(start):
    stack = []
    stack.append(start)
    visited[start] = True
    count = 0

    while stack:
        v = stack.pop()
        for computer in graph[v]:
            if not visited[computer]:
                stack.append(computer)
                visited[computer] = True
                count += 1
    return count

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a , b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
print(bfs(1))

# 10분