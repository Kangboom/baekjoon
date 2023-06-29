n = int(input())

sum = 0
count = 0

i = 1
while(sum < n):
    sum += i
    i += 1
    count += 1
if(count % 2 != 0):
    print(f'{sum-n+1}/{count-(sum-n)}')
else:
    print(f'{count-(sum-n)}/{sum-n+1}')
    