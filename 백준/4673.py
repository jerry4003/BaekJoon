def selfNum(n):
    N=n
    for i in range(4):
        a=N%10
        N=int(N/10)
        n+=a
    return n

Mylist=[]
Anslist=[]
for i in range(1,10001):
    Anslist.append(i)
for i in range(1,10001):
    Mylist.append(selfNum(i))
Anslist=sorted(set(Anslist)-set(Mylist))
for i in Anslist:
    print(i)