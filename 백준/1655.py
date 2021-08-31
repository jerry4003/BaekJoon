import sys
import heapq
N=int(sys.stdin.readline())
leftheap=[]
rightheap=[]
for i in range(N):
    num=int(sys.stdin.readline())
    if len(leftheap)==len(rightheap):
        heapq.heappush(leftheap,(-num,num))
    else:
        heapq.heappush(rightheap,(num,num))
    if rightheap and leftheap[0][1]>rightheap[0][1]:
        left_value=heapq.heappop(leftheap)[1]
        right_value=heapq.heappop(rightheap)[1]
        heapq.heappush(rightheap,(left_value,left_value))
        heapq.heappush(leftheap,(-right_value,right_value))
    print(leftheap[0][1])