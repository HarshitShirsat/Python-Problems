def indexofsmall(l):
    small=min(l)
    a=l.index(small)
    return a

n=int(input("Enter number of elements - "))
l=[]
for i in range(n):
    x=int(input("Enter element : "))
    l.append(x)
z=indexofsmall(l)
print("Index of smallest element - ",z)
