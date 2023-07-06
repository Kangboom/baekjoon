N = int(input())
N_card = list(map(int,input().split()))
M = int(input())
M_card = list(map(int, input().split()))

N_card.sort()

def num_sort(N_card, num, n):
    if(n//2 == 0):
        if N_card[n//2] == num :
            return 1
        else:
            return 0
    if(N_card[n//2] < num):
        return num_sort(N_card[n//2 +1:], num, n//2)
    elif N_card[n//2] == num:
        return 1
    elif N_card[n//2] >= num :
        return num_sort(N_card[0:n//2], num, n//2)

for num in M_card:
    print(num_sort(N_card, num, N), end=' ')            

