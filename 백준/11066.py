import sys
T=int(sys.stdin.readline())
for _ in range(T):
    K=int(sys.stdin.readline())
    file=list(map(int,sys.stdin.readline().split()))
    dp=[[0*K] for _ in range(K)]
    for i in range(K-1):
        dp[i][i+1]=file[i]+file[i+1]
        for j in range(i+2,K):
            dp[i][j]=dp[i][j-1]+file[j]
    for d in range(2,K):