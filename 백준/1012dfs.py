import sys
sys.setrecursionlimit(10000)
T=int(sys.stdin.readline())
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for _ in range(T):
    M,N,K=map(int,sys.stdin.readline().split())
    cnt=0
    matrix=[[0]*M for _ in range(N)]
    visit=[[0]*M for _ in range(N)]
    for _ in range(K):
        x,y=map(int,sys.stdin.readline().split())
        matrix[y][x]=1
    def dfs(x,y):
        visit[x][y]=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if matrix[nx][ny]==1 and visit[nx][ny]==0:
                    dfs(nx,ny)
    for x in range(N):
        for y in range(M):
            if matrix[x][y]==1 and visit[x][y]==0:
                dfs(x,y)
                cnt+=1
    print(cnt)