A,B,C=map(int,input().split())

if B<C:
    i=C-B
    print(int(A/i)+1)
else:
    print(-1)
