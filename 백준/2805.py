import sys
N,M=map(int,sys.stdin.readline().split())
height=list(map(int,sys.stdin.readline().split()))
left=0
right=max(height)
ans=0
while left<=right:
    mid=(left+right)//2
    sum=0
    for i in height:
        if i>mid:
            sum+=(i-mid)
    if sum>=M:
        left=mid+1
    else:
        right=mid-1
print(right)

    
    