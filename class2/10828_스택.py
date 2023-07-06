n = int(input())
cmds = [list(input().split()) for _ in range(n)]

stack = []
cmdset = ['push', 'top', 'size', 'empty', 'pop']

for cmd in cmds:
    if cmd[0] == cmdset[0]:
        stack.append(int(cmd[1]))
    elif cmd[0] == cmdset[1]:
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif cmd[0] == cmdset[2]:
        print(len(stack))
    elif cmd[0] == cmdset[3]:
        if not stack:
            print(1)
        else:
            print(0)
    else:
        if stack :
            print(stack.pop())
        else:
            print(-1)