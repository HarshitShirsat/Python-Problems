def isConsecutiveFour(l):
    for i in range(len(l)-3):
        if l[i]==l[i+1]==l[i+2]==l[i+3]:
            print("There")
            return
    print("Not there")

n=int(input("Enter number of elements - "))
l=[]
for i in range(n):
    x=int(input("Enter element : "))
    l.append(x)
isConsecutiveFour(l)
