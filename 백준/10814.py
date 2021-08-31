N=int(input())
member_list=[]
member_seq=1
for _ in range(N):
    age,name=map(str,input().split())
    age=int(age)
    member_list.append((age,member_seq,name))
    member_seq+=1
member_list.sort(key=lambda x:(x[0],x[1]))
for i in member_list:
    print(i[0],i[2])