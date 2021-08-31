import sys
from collections import deque
T=int(sys.stdin.readline())
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for _ in range(T):
    M,N,K=map(int,sys.stdin.readline().split())
    cnt=0
    matrix=[[0]*M for _ in range(N)]
    visit=[[0]*M for _ in range(N)]
    def bfs(x,y):
        visit[x][y]=1
        queue=deque()
        queue.append((x,y))
        while queue:
            a=queue[0][0]
            b=queue[0][1]
            del queue[0]
            for i in range(4):
                nx=a+dx[i]
                ny=b+dy[i]
                if 0<=nx<N and 0<=ny<M:
                    if matrix[nx][ny]==1 and visit[nx][ny]==0:
                        visit[nx][ny]=1
                        queue.append((nx,ny))
    for _ in range(K):
        x,y=map(int,sys.stdin.readline().split())
        matrix[y][x]=1
    for x in range(N):
        for y in range(M):
            if matrix[x][y]==1 and visit[x][y]==0:
                bfs(x,y)
                cnt+=1
    print(cnt)