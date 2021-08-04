N=int(input())
create=[]
for i in range(N):
    M=i
    for l in str(i):
        M+=int(l)
    create.append(M)
if N in create:
    print(create.index(N))
else:
    print(0)