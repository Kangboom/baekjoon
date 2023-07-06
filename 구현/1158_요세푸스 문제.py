from collections import deque
n, k = map(int,input().split())

queue = deque()
for i in range(1,n+1):
    queue.append(i)

result = []

i = 1
while queue:
    if i % k != 0:
        queue.append(queue.popleft())
    else:
        result.append(queue.popleft())
    i += 1
print('<',end='')
print(*result,sep=', ',end='')
print('>')