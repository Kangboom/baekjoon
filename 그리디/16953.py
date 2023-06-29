A, B = map(int, input().split())

count = 0
while(A != B):

    if ( A > B):
        count = -2
        break

    elif( B % 10 == 1):
        B = B // 10
        count += 1

    elif(B % 2 == 0):
        B //=2
        count += 1
    else:
        count = -2
        break

print(count+1)