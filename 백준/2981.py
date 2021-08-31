from math import gcd
import sys
N=int(sys.stdin.readline())
number=[]
gcd_list=[]
for _ in range(N):
    number.append(int(sys.stdin.readline()))
number.sort()
gcd_num=number[1]-number[0]
if N>2:
    for i in range(2,N):
        gcd_num=gcd(gcd_num,number[i]-number[i-1])
for i in range(1,int(gcd_num**0.5)+1):
    if gcd_num%i==0:
        gcd_list.append(i)
        gcd_list.append(gcd_num//i)
gcd_list.remove(1)
gcd_list=list(set(gcd_list))
gcd_list.sort()
for i in gcd_list:
    print(i,end=" ")

