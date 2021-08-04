N,M=map(int,input().split())
card=list(map(int,input().split()))
sum=[]
for i in range(len(card)-2):
    for j in range(i+1,len(card)-1):
        for k in range(j+1,len(card)):
            sum.append(card[i]+card[j]+card[k])
ans=0
for score in sum:
    if score>ans and score<=M:
        ans=score
print(ans)