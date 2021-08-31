import sys
N,C=map(int,sys.stdin.readline().split())
house=[]
for _ in range(N):
    house.append(int(sys.stdin.readline()))
house.sort()
left=1
ans=0
right=house[-1]-house[0]
while left<=right:
    mid=(left+right)//2
    count=1
    before=house[0]
    for i in house:
        if i>=before+mid:
            count+=1
            before=i
    if count<C:
        right=mid-1
    else:
        left=mid+1
        ans=mid
print(ans)
