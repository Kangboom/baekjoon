s = input()

count = 0
for i in range(len(s)-1):
    if(s[i] != s[i+1]):
        count +=1
if count % 2 == 0:
    print(count //2)
else :
    print(count //2 + 1)