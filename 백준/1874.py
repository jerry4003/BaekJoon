import sys
n=int(sys.stdin.readline())
number=[]
count=1
answer=[]
for _ in range(n):
    num=int(sys.stdin.readline())
    while count<=num:
        number.append(count)
        answer.append("+")
        count+=1
    if number[-1]==num:
        number.pop()
        answer.append("-")
if len(number)==0:
    for i in answer:
        print(i)
else:
    print("NO")