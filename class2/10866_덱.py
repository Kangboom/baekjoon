from collections import deque

n = int(input())
cmds = [list(input().split()) for _ in range(n)]

mydeque = deque()
cmdset = ['push_front', 'push_back', 'pop_front', 'pop_back', 'size', 'empty',  'front', 'back']

for cmd in cmds:
    if cmd[0] == cmdset[0]:
        mydeque.appendleft(int(cmd[1]))
    elif cmd[0] == cmdset[1]:
        mydeque.append(int(cmd[1]))
    elif cmd[0] == cmdset[2]:
        if mydeque:
            print(mydeque.popleft())
        else:
            print(-1)
    elif cmd[0] == cmdset[3]:
        if mydeque:
            print(mydeque.pop())
        else:
            print(-1)
    elif cmd[0] == cmdset[4]:
            print(len(mydeque))
    elif cmd[0] == cmdset[5]:
        if mydeque:
            print(0)
        else:
            print(1)
    elif cmd[0] == cmdset[6]:
        if mydeque:
            print(mydeque[0])
        else:
            print(-1)
    else:
        if mydeque:
            print(mydeque[-1])
        else:
            print(-1)