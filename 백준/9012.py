import sys
T=int(sys.stdin.readline())
for _ in range(T):
    stack=[]
    flag=True
    string=list(sys.stdin.readline())
    for i in string:
        if i=="(":
            stack.append(i)
        elif i==")":
            if stack and stack[-1]=="(":
                stack.pop()
            else:
                flag=False
                break
    if flag==True and len(stack)==0:
        print("YES")
    else:
        print("NO")
