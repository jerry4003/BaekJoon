import sys

N,M=map(int,sys.stdin.readline().split())
number=[]
def f():
    for i in range(1,N+1):
        if i in number:
            continue
        number.append(i)
        if len(number)==M:
            number2=sorted(number)           
            if number==number2:
                for j in number:
                    print(j,end=" ")
                print()
        f()
        number.pop()
f()