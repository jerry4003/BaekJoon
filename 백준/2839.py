import sys
N=int(sys.stdin.readline())
count=0
while N>=0:
    if N%5==0:
       count+=int(N//5)
       print(count)
       break
    else:
        N-=3
        count+=1
        if N<0:
           print(-1)
           break