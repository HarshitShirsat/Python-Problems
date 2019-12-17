fn=input("Enter the file name - ")
f=open(fn,"r")
l=[]
no=0
for ln in f:
    total=0
    no+=1
    l=ln.split()
    for i in l:
        total+=int(i)
    print("Student ",no)
    print("Total marks - ",total)
    print("Average marks - ",total/6)
