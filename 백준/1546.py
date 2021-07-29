N=int(input())
score=list(map(float,input().split()))
cnt=0.0
Mscore=max(score)
for i in range(N):
    score[i]=score[i]/Mscore*100.0
    cnt+=score[i]
print(cnt/float(N))