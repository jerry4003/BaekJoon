C=int(input())
for i in range(C):    
    score=list(map(float,input().split()))
    sum=0.0
    for j in range(1,int(score[0])+1):
        sum+=score[j]
    avr=float(sum/score[0])
    cnt=0
    for k in range(1,int(score[0])+1):
        if score[k]>avr:
            cnt+=1
    k=float(cnt/score[0])*100.0
    print(f'{k:.3f}%')
    