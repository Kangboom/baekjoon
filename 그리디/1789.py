N = int(input())

count = 0
sum = 0

for i in range(1,N+1):

    if( sum + i > N):
        break
    sum += i
    count += 1

print(count)

# 1부터 N까지 더해가면서 처음으로 N을 넘을 경우가 
# 서로다른 정수의 최대 갯수
# 만약 11 이라고 하면 1 + 2 + 3 + 4 에서 4만 5로 바꿔준다고 생각하면 되므로