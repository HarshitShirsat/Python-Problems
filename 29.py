f1=open("keys.txt","r")
f2=open("marks.txt","r")

mlist=[]
klist=[]
totmark=[]
for line in f1:
    klist=line.split()
    klist.pop(0)
for line in f2:
    mlist=line.split()
    mlist.pop(0)
    count=0
    for i in range(0,10):
        if mlist[i]==klist[i]:
            count+=1
    totmark.append(count)

j=0
for i in totmark:
    print("Student ",j,"\t Mark - ",i)
    j+=1

index=totmark.index(max(totmark))
print("Highest Mark Obtained")
print("Student ",index,"\t Mark - ",totmark[index])
