fn=input("Enter the file name - ")
f=open(fn,"r")
line=0
word=0
char=0
list=[]
for ln in f:
    line+=1
    list=ln.split()
    for wd in list:
        word+=1
        for ch in wd:
            char+=1
print("Number of lines - ",line)
print("Number of words - ",word)
print("Number of characters - ",char)
