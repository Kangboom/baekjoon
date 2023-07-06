n, c = map(int,input().split())
array = [ int(input()) for _ in range(n)]
array.sort()

start = min(array)
end = max(array)

while start <= end:

    mid = (start + end) // (c+1)
