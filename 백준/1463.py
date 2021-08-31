import sys
N=int(sys.stdin.readline())

ans=[0 for _ in range(1000001)]
ans[2]=1
ans[3]=1
for i in range(4,N+1):
    ans[i]=ans[i-1]+1
    if i%3==0:
        ans[i]=min(ans[(i//3)]+1,ans[i])
    if i%2==0:
        ans[i]=min(ans[(i//2)]+1,ans[i]) 
print(ans[N])   