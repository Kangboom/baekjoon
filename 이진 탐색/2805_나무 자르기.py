n , m = map(int,input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in array:
        if i > mid :
            total += (i-mid)
    
    if total < m:
        end = mid-1
    else:
        start = mid+1

print(end)
    