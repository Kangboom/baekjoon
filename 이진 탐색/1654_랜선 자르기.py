k, n = map(int,input().split())
array = [ int(input()) for _ in range(k)]

start = 1
end = max(array)
h = 1 # 사실 h는 필요 없었음 어짜피 while문이 끝나면 mid값과 end 값은 같아지기 때문에 

while start <= end:
    mid = (start + end) // 2
    total = 0
    for l in array:
        total += (l // mid)

    if total >= n:
        h = mid
        start = mid +1
    else:
        end = mid-1    
print(h) # 그냥 end를 출력해도 똑같았음