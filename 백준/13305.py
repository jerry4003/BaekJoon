import sys
N=int(sys.stdin.readline())
distance=list(map(int,sys.stdin.readline().split()))
price=list(map(int,sys.stdin.readline().split()))
for i in range(len(price)-1):
    if i==0:
        continue
    if price[i]>price[i-1]:
        price[i]=price[i-1]
sum=0
for i in range(len(distance)):
    sum+=distance[i]*price[i]
print(sum)

