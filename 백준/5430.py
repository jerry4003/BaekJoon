import sys
from collections import deque
T=int(sys.stdin.readline())
for _ in range(T):
    p=sys.stdin.readline().rstrip()
    p=p.replace("RR","")
    n=int(sys.stdin.readline())
    k=deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    r=0
    f=0
    b=0
    for i in p:
        if i=="R":
            r+=1
        elif i=="D":
            if r%2==0:
                f+=1
            else:
                b+=1
    if f+b>n:
        print("error")
    else:
        for i in range(f):
            k.popleft()
        for i in range(b):
            k.pop()
        if r%2==1:
            k.reverse()
        print("[", end='')
        for i in range(len(k)):
            if i == len(k)-1:
                print(k[i],end='')
            else:
                print(k[i],end=',')
        print("]")
        """print("[",end="")
        for i in k:
            print(i,end="")
            if i!=k[len(k)-1]:
                print(",",end=" ")
        print("]")"""