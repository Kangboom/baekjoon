import sys
input=sys.stdin.readline

n, m = map(int,input().split())

hear = [ input().rstrip('\n') for _ in range(n)]
see = [ input().rstrip('\n') for _ in range(m)]

_dict = {}
result = []
for i in range(len(hear)):
    _dict[hear[i]] = 0
for i in range(len(see)):
    if see[i] in _dict:
        result.append(see[i])

print(len(result))
for i in sorted(result):
    print(i)
    
