import sys
N=int(sys.stdin.readline())
ans=[[0]*10 for _ in range(N+1)]
mod=1000000000
for i in range(1,10):
    ans[1][i]=1
for i in range(2,N+1):
    for j in range(10):
        if j==0:
            ans[i][j]=ans[i-1][1]
        elif j==9:
            ans[i][j]=ans[i-1][8]
        else:
            ans[i][j]=ans[i-1][j-1]+ans[i-1][j+1]
print(sum(ans[N])%mod)