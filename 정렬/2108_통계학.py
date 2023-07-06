import sys
input=sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()

print(round((sum(num)/n)))
print(num[n//2])

hash = {}
for i in num:
    if i not in hash:
        hash[i] = 1
    else:
        hash[i] += 1

max_n = max(hash.values())
result = [ a for (a,b) in hash.items() if max_n == b]

if(len(result) == 1):
    print(result[0])
else:
    print(result[1])
print(num[n-1]-num[0]) # 범위

