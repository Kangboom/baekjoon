n = input()

s =[]
sum = 0

for i in n:
    if('A'<= i and i <= 'Z'):
        s.append(i)
    else:
        sum += int(i)

print((''.join(sorted(s)))+str(sum))
