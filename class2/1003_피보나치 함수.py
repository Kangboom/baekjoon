import sys
input=sys.stdin.readline
n = int(input())
array = [int(input()) for _ in range(n)]

def fibo(n):
    result = [[1,0], [0,1]]
    if n == 0:
        print(*result[0])
    elif n == 1:
        print(*result[1])
    else:
        for _ in range(n-1):
            temp = [result[-2][0]+result[-1][0],result[-2][1]+result[-1][1]]
            result.append(temp)
        print(*result[-1])
            
for i in range(len(array)):
    fibo(array[i])