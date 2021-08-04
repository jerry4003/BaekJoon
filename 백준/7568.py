N=int(input())
people=[]
for i in range(N):
    x,y=map(int,input().split())
    people.append((x,y))
for i in people:
    rank=1
    for j in people:
        if j[0]>i[0] and j[1]>i[1]:
            rank+=1
    print(rank, end=" ")