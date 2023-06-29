N, M = map(int,input().split())
prices = [list(map(int,input().split())) for _ in range(M)]

result = prices[0][1] * N 

for price in prices:
    money = min((N // 6)*price[0] + (N % 6)*price[1],price[1]*N)
    
    if(result > money ):
        result = money
4
print(result) 