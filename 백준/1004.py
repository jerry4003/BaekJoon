a = int(input())

for i in range(a):
    cnt=0
    x1,y1,x2,y2=map(int,input().split())
    num=int(input())
    for i in range(num):
        cx,cy,r=map(int,input().split())
        d1=((cx-x1)**2+(cy-y1)**2)**0.5
        d2=((cx-x2)**2+(cy-y2)**2)**0.5
        if (d1>r and d2<r) or (d1<r and d2>r):
            cnt+=1
    print(cnt)
