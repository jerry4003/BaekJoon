import sys
N=int(sys.stdin.readline())
k=int(sys.stdin.readline())
left=1
right=k
while left<=right:
    mid=(left+right)//2
    temp=0
    for i in range(1,N+1):
        temp+=min(N,mid//i)
    if temp>=k:
        right=mid-1
    else:
        left=mid+1
print(left)
