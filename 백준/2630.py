import sys
N=int(sys.stdin.readline())
paper=[]
result=[]
for _ in range(N):
    paper.append(list(map(int,sys.stdin.readline().split())))
def check(x,y,N):
    number=paper[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if paper[i][j]!=number:
                check(x,y,N//2)
                check(x+(N//2),y,N//2)
                check(x,y+(N//2),N//2)
                check(x+(N//2),y+(N//2),N//2)
                return
    if number==0:
        result.append(0)
    else:
        result.append(1)
check(0,0,N)
print(result.count(0))
print(result.count(1))