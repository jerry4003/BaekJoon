import sys
N=int(input())
x=list(map(int,sys.stdin.readline().split()))
y=list(set(x))
y.sort()
dic={}
for i in range(len(y)):
    dic[y[i]]=i
for i in x:
    print(dic[i],end=" ")
