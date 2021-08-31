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
    if f+b>len(k):
        print("error")
    else:
        print(len(k))
#이거 k에 []라해도 len(k)=1이 나옴