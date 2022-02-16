T=int(input())
ans=[]
for i in range(T):
    a,b=map(int,input().split())
    ans.append(a+b)
for j in range(1,T+1):
    k=ans[j-1]
    print("Case #"+str(j)+":",k)