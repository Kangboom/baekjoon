import sys
input = sys.stdin.readline 

N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

result = [ 0 for _ in range(N+1)]

def find_root(root):
    stack = []
    stack.append(root)
    while stack:
        v = stack.pop()
        for n in tree[v]:
            if(n != result[v]):
                stack.append(n)
                result[n] = v
            

find_root(1)
for i in result[2:]:
    print(i)