import sys
input = sys.stdin.readline 

N, M = map(int,input().split())

graph = [ [] for _ in range(N+1)]
not_root = []
for i in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
    not_root.append(a)

result = []

def haking(start):
    count = 0
    stack = []
    stack.append(start)
    visited[start] = True

    while stack:
        v = stack.pop()
        for node in graph[v]:
            if(visited[node] == False):
                count += 1
                stack.append(node)
                visited[node] = True

    return count

result = []
for i in range(1,N+1):
    if( i not in not_root):
        visited = [False] * (N+1)
        result.append(haking(i))

temp = max(result)
for i in range(len(result)):
    if temp == result[i]:
        print(i+1, end=' ')
