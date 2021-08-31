import sys
N=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))
stack=[]
result=[-1 for _ in range(N)]
stack.append(0)
idx=1
for _ in range(N-1):
    while stack and nums[stack[-1]]<nums[idx]:
        result[stack[-1]]=nums[idx]
        stack.pop()
    stack.append(idx)
    idx+=1
for i in result:
    print(i,end=" ")