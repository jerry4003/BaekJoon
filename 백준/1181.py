N=int(input())
word_list=[]
for _ in range(N):
    word=str(input())
    word_length=len(word)
    word_list.append((word_length,word))
word_list=list(set(word_list))
word_list.sort()
for i in word_list:
    print(i[1])