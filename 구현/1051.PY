N, M = map(int, input().split())
square = [ input() for _ in range(N)]

for line in range(min(N,M)-1,-1,-1):
    for i in range(N-line):
        for j in range(M-line):
            if(square[i][j] == square[i][j+line] and square[i+line][j] == square[i+line][j+line] and square[i][j] == square[i+line][j]):
                print((line+1)**2)
                exit()

# 큰 것부터 찾고 찾으면 exit()로 종료해서 실행시간을 줄일 수 있음