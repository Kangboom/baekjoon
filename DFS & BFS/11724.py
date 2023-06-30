
def dfs(start):

    stack = []
    stack.append(start)
    visited[start] = True
    
    while stack:
        v = stack.pop()
        for i in graph[v]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
            
    return True    

import sys
input = sys.stdin.readline 

N , M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
result = 0

for i in range(1, N+1):
    if(visited[i]): continue
    dfs(i)
    result += 1

print(result)