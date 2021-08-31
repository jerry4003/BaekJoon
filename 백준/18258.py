import sys
from collections import deque
dq=deque()
N=int(sys.stdin.readline())
for _ in range(N):
    command=sys.stdin.readline().split()
    if command[0]=="push":
        dq.append(int(command[1]))
    elif command[0]=="pop":
        if len(dq)>0:
            k=dq.popleft()
            print(k)
        else:
            print(-1)
    elif command[0]=="size":
        print(len(dq))
    elif command[0]=="empty":
        if len(dq)>0:
            print(0)
        else:
            print(1)
    elif command[0]=="front":
        if len(dq)>0:
            print(dq[0])
        else:
            print(-1)
    elif command[0]=="back":
        if len(dq)>0:
            print(dq[len(dq)-1])
        else:
            print(-1)
