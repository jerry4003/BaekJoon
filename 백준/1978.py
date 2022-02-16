import sys
N=int(sys.stdin.readline())
number=list(map(int,sys.stdin.readline().split()))
sum=0
for i in number:
    if i==1:
        continue
    elif i==2 or i==3:
        sum+=1
    else:
        k=0
        for j in range(2,(i//2)+1):
            if i%j==0:
                k+=1
                break
        if k==0:
            sum+=1        
print(sum)
    
        
    