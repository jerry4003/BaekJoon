import sys
graph=[]
N=int(sys.stdin.readline())
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))
visit=[[0]*N for _ in range(N)]   
dx=[-1,1,0,0]
dy=[0,0,1,-1]
def dfs(i,j,dange):
    visit[i][j]=1
    global num
    if graph[i][j]==1:
        num+=1
        graph[i][j]=dange
    for k in range(4):
        ni=i+dx[k]
        nj=j+dy[k]
        if 0<=ni<N and 0<=nj<N:
            if graph[ni][nj]==1 and visit[ni][nj]==0:
                dfs(ni,nj,dange)

dange=1
num=0
numlist=[]
for i in range(N):
    for j in range(N):
        if graph[i][j]==1 and visit[i][j]==0:
            dfs(i,j,dange)
            numlist.append(num)
            num=0
            dange+=1
print(len(numlist))
numlist.sort()
for i in numlist:
    print(i)