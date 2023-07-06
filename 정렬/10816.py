n = int(input())
card = list(map(int,input().split()))
m = int(input())
check = list(map(int, input().split()))

card.sort()
_dict = {card[0] : 1}
count = 1

for i in range(1, len(card)):
    if(card[i] == card[i-1]):
        count += 1
    else:
        count = 1
    _dict[card[i]] = count

for j in check:
    if j in _dict:
        print(_dict[j], end=' ')
    else:
        print(0, end=' ')