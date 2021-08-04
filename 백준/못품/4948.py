import sys
def isPrime(A):
    if(A==1):
        return False
    else:
        for i in range(2,int(A**0.5)+1):
            if(A%i==0):
                return False
        return True    
prime=[]      
for i in range(1,2*123456+1):
    if isPrime(i):
        prime.append(i)  
while(1):
    n=int(sys.stdin.readline())
    if(n==0):
        break
    else:
        k=[]
        for i in range(n,2*n+1):
            if i in prime:
                k.append(i)
        print(len(k))

        