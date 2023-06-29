s = [ list(input().split()) for _ in range(20)]

scores = {'A+' : 4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F': 0.0}

sum = 0
count = 0
for i in range(20):
    temp = float(s[i][1])
    if (s[i][2] in scores):
        sum += temp * scores[s[i][2]]
        count += temp

print(round(sum/count,6))