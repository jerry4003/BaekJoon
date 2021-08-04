word=input()
CroAlpha=["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in CroAlpha:
    word=word.replace(i,"*")
print(len(word))