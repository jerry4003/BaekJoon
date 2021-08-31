import sys
num=int(sys.stdin.readline())
K=int(sys.stdin.readline())
graph=[[0]*num for _ in range(num)]
for _ in range(K):
    a,b=map(int,sys.stdin.readline().split())
    graph[a-1][b-1]=1
    graph[b-1][a-1]=1

visit=[0 for _ in range(num)]
def dfs(v):
    visit[v]=1
    for i in range(num):
        if graph[v][i]==1 and visit[i]==0:
            dfs(i)
dfs(0)
print(sum(visit)-1)
