N = int(input())
s = [list(map(int,input().split())) for _ in range(2)]

s[0].sort()
s[1].sort(reverse=True)

sum = 0
for i in range(N):
    sum += s[0][i] * s[1][i]

print(sum)