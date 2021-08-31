import sys
import heapq
heap=[]
N=int(sys.stdin.readline())
for _ in range(N):
    num=int(sys.stdin.readline())
    if num==0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    elif num>0:
        heapq.heappush(heap,(num,num))
    else:
        heapq.heappush(heap,(-num,num))