import sys
from collections import deque
dq=deque()
count=0
N,M=map(int,sys.stdin.readline().split())
for i in range(N):
    dq.append(i+1)
k=list(map(int,sys.stdin.readline().split()))
for i in k:
    while(True):
        if dq[0]==i:
            dq.popleft()
            break
        if dq.index(i)<((len(dq)//2)+1):
            while dq[0]!=i:
                dq.append(dq.popleft())
                count+=1
        else:
            while dq[0]!=i:
                dq.appendleft(dq.pop())
                count+=1

print(count)