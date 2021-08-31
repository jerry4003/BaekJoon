import sys

N,M=map(int,sys.stdin.readline().split())
number=[]

def f():
    if len(number)==M:
            for j in number:
                print(j,end=" ")
            print()
            return
    for i in range(1,N+1):
        number.append(i)
        f()
        number.pop()

f()
    