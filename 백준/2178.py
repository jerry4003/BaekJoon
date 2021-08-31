import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())
matrix=[]
mx=[-1,1,0,0]
my=[0,0,-1,1]
for _ in range(N):
    matrix.append(list(map(int,sys.stdin.readline().rstrip())))
que=deque()
que.append([0,0])
while que:
    a=que[0][0]
    b=que[0][1]
    del que[0]
    for i in range(4):
        nx=a+mx[i]
        ny=b+my[i]
        if 0<=nx<N and 0<=ny<M:
            if matrix[nx][ny]==1:
                que.append([nx,ny])
                matrix[nx][ny]=matrix[a][b]+1
print(matrix[N-1][M-1])