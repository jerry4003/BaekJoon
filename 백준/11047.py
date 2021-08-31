import sys
N,K=map(int,sys.stdin.readline().split())
coin=[]
for _ in range(N):
    coin.append(int(sys.stdin.readline()))
cnt=0
coin.reverse()
for i in coin:
    if(K==0):
        break
    if(i>K):
        continue
    cnt+=int(K/i)
    K=K%i
print(cnt)