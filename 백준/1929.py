def isPrime(A):
    if(A==1):
        return False
    else:
        for i in range(2,int(A**0.5)+1):
            if(A%i==0):
                return False
        return True

M,N= map(int,input().split())
for i in range(M,N+1):
    if isPrime(i):
        print(i)