import sys
from collections import deque
Testcase=int(sys.stdin.readline())
for _ in range(Testcase):
    dq=deque()
    answer=list()
    N,M=map(int,sys.stdin.readline().split())
    important=deque(map(int,sys.stdin.readline().split()))
    for i in range(N):
        dq.append(i)
    while(True):
        if len(dq)==0:
            break
        if important[0]==max(important):
            important.popleft()
            answer.append(dq.popleft())
        else:
            dq.append(dq.popleft())
            important.append(important.popleft())
    print(1+answer.index(M))
