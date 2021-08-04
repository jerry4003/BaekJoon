N,M=map(int,input().split())
Garo=[]
wrong=[]
for _ in range(N):
   Garo.append(input())
for i in range(N-7):
    for j in range(M-7):
        wrongW=0
        wrongB=0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2==0:
                    if Garo[a][b]!="W":
                        wrongW+=1
                    if Garo[a][b]!="B":
                        wrongB+=1
                else:
                    if Garo[a][b]!="B":
                        wrongW+=1
                    if Garo[a][b]!="W":
                        wrongB+=1
        wrong.append(min(wrongW,wrongB))
print(min(wrong))
