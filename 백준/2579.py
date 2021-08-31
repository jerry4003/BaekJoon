import sys
N=int(sys.stdin.readline())
score=[0 for i in range(301)]
sum_score=[0 for i in range(301)]
for i in range(N):
    score[i]=int(sys.stdin.readline())
sum_score[0]=score[0]
sum_score[1]=score[0]+score[1]
sum_score[2]=max(score[0],score[1])+score[2]
for i in range(3,N):
    sum_score[i]=max(sum_score[i-2],sum_score[i-3]+score[i-1])+score[i]
print(sum_score[N-1])