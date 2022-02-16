import sys
N=int(sys.stdin.readline())
count=0
for _ in range(N):
    word=sys.stdin.readline().rstrip()
    for i in range(0,len(word)-1):
        if word[i]!=word[i+1]:
            if word[i] in word[i+1:]:
                count+=1
                break
print(N-count)