import sys
N=int(sys.stdin.readline())
answer=[]
window=[sys.stdin.readline().rstrip() for _ in range(N)]

def checking(x,y,N):
    color=window[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if window[i][j]!=color:
                answer.append("(")
                checking(x,y,N//2)
                checking(x,y+(N//2),N//2)
                checking(x+(N//2),y,N//2)
                checking(x+(N//2),y+(N//2),N//2)
                answer.append(")")
                return
    if color=="0":
        answer.append(0)
    else:
        answer.append(1)

checking(0,0,N)
for i in answer:
    print(i,end="")