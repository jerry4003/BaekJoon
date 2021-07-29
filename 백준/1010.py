a=int(input())
def factorial(k):
    sum=1
    for i in range(1,k+1):
        sum*=i
    return sum
        
for i in range(a):
    N,M=map(int,input().split())
    if N==M:
        cnt=1
    else:
        cnt=factorial(M)/(factorial(N)*factorial(M-N))
    print(int(cnt))