N = int(input())
max_w = [int(input()) for _ in range(N)]

max_w.sort()
result = max_w[0]*N

for i in range(1,N):
    temp = max_w[i]*(N-i)
    if(result < temp):
        result = temp

print(result)