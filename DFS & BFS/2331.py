A , P = map(int, input().split())

result = [str(A)]

repeat_num = ""
i = 0  
while(True):
    sum = 0
    for num in result[i]:
        sum += int(num)**P
    
    if str(sum) in result:
        repeat_num = str(sum)
        break

    result.append(str(sum))
    i += 1

print(len(result[:result.index(repeat_num)]))
