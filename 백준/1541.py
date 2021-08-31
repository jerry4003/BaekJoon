import sys
a=sys.stdin.readline().split('-')
sum=0
for i in a[0].split('+'):
    sum+=int(i)
for i in range(1,len(a)):
    for j in a[i].split('+'):
        sum-=int(j)
print(sum)