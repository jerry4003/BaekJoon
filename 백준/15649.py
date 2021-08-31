import sys

N,M=map(int,sys.stdin.readline().split())
number=[]

def f():
    for i in range(1,N+1):
        if i in number:
            continue
        number.append(i)
        if len(number)==M:
            for i in number:
                print(i,end=" ")
            print()
        f()
        number.pop()

f()        
