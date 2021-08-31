import sys
N=int(sys.stdin.readline())
numberlist=[]
for _ in range(N):
    numberlist.append(list(map(int,sys.stdin.readline().split())))
k=2
for i in range(1,N):
    for j in range(k):
        if j==0:
            numberlist[i][j]+=numberlist[i-1][j]
        elif j==i:
            numberlist[i][j]+=numberlist[i-1][j-1]
        else:
            numberlist[i][j]+=max(numberlist[i-1][j-1],numberlist[i-1][j])
    k+=1
print(max(numberlist[N-1]))