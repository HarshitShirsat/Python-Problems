n=int(input("Enter the number of items - "))
n1,n2=0,1
print(n1,end=" ")
print(n2,end=" ")
for i in range(2,n):
    x=n1+n2
    n1=n2;
    n2=x;
    print(x, end=" ")
print("\n")
