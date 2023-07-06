from collections import deque
import sys
input = sys.stdin.readline 

# BFS 사용
def haking(start):
    visited = [False] * (N+1)
    queue = deque()
    count = 1
    queue.append(start)
    visited[start] = True

    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if(not visited[node]):
                count += 1
                queue.append(node)
                visited[node] = True

    return count

N, M = map(int,input().split())

graph = [ [] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

result = []
for i in range(1,N+1): 
    result.append(haking(i))

temp = max(result)
for i in range(len(result)):
    if temp == result[i]:
        print(i+1, end=' ')

# 30분 .. 시간초과에서 헤맴
# 다른 BFS 문제랑 다를 건 없었음