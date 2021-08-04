A,B,V=map(int,input().split())
if A==V:
    print(1)
else:
    I=A-B
    K=V-A
    if K%I>0:
        Z=int(K/I)+1
    else:
        Z=int(K/I)
    print(Z+1)