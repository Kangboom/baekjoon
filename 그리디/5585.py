N = int(input())

changes = [500, 100, 50, 10, 5, 1]
money = 1000 - N
result = 0

for change in changes:
    result += money // change 
    money %= change

print(result)