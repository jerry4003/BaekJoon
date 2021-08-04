word=input().upper()
alphabetlist=list(set(word))
cntlist=[]
for i in alphabetlist:
    cnt=word.count(i)
    cntlist.append(cnt)
if cntlist.count(max(cntlist))>1:
    print("?")
else:
    print(alphabetlist[cntlist.index(max(cntlist))])