import sys
N=int(sys.stdin.readline())
point_list=[]
for _ in range(N):
    x,y=map(int,sys.stdin.readline().split())
    point_list.append((x,y))
point_list.sort(key=lambda x:(x[1],x[0]))
for i in point_list:
    print(i[0],i[1])
