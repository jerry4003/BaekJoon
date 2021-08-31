from collections import Counter

N=int(input())
number=[]
for _ in range(N):
    number.append(int(input()))

def avr(a):
    return  round(sum(a)/len(a))
def mid(a):
    a.sort()
    return a[int(len(a)/2)]
def time(a):
    a.sort()
    modes=Counter(a).most_common()
    if len(a)>1:
        if modes[0][1]==modes[1][1]:
            return modes[1][0]
        else:
            return modes[0][0]
    else:
        return modes[0][0]
def scope(a):
    return max(a)-min(a)

print(avr(number))
print(mid(number))
print(time(number))
print(scope(number))
