import sys

N=int(sys.stdin.readline())
K=list(map(int,sys.stdin.readline().split()))
list=[0]
def find(i):
    left=1
    right=len(list)-1
    while left<=right:
        mid=(left+right)//2
        if list[mid]>=i:
            right=mid-1
        else:
            left=mid+1
    return left
for i in K:
    if list[-1]<i:
        list.append(i)
    else:
        index=find(i)
        list[index]=i
print(len(list)-1)