import sys
N,M,V=map(int,sys.stdin.readline().split())
graph=[[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a][b]=1
    graph[b][a]=1
visitdfs=[0 for _ in range(N+1)]
visitbfs=[0 for _ in range(N+1)]
dfslist=[]
bfslist=[]
def dfs(v):
    dfslist.append(v)
    visitdfs[v]=1
    for i in range(N+1):
        if graph[v][i]==1 and visitdfs[i]==0:
            dfs(i)
def bfs(v):
    queue=[]
    queue.append(v)
    visitbfs[v]=1
    while queue:
        bfslist.append(queue[0])
        for i in range(N+1):
            if graph[queue[0]][i]==1 and visitbfs[i]==0:
                queue.append(i)
                visitbfs[i]=1
        del queue[0]
dfs(V)
bfs(V)
for i in dfslist:
    print(i,end=" ")
print()
for i in bfslist:
    print(i,end=" ")