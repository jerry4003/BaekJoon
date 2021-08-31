from collections import deque
k=deque([])
print("[",end="")
for i in k:
    print(i,end="")
    if i!=k[len(k)-1]:
        print(",",end="")
print("]")

#같은수를 넣어봐 deque[1,2,3,4] 틀리게 나와 등신아