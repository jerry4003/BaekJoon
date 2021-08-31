N=int(input())
cnt=0
K=N
while True:
    cnt+=1
    if K<10:
        K*=11
    else:
        M=int(K/10)+(K%10)
        K=M%10+10*(K%10)
    if N==K:
        break
print(cnt)