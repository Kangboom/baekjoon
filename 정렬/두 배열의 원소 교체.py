N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    if(A[i] < B[i]):
        A[i], B[i] = B[i] , A[i]
    else: # A의 원소가 B의 원소보다 클 경우
        break

print(sum(A))