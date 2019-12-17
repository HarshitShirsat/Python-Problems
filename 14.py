l=[]
n=int(input("Enter the number of elements - "))
for i in range(0,n):
    a=int(input("Enter the element no %d- "%(i+1)))
    l.append(a)
l.sort()
print(l)
key=int(input("Enter key element - "))
low=0
high=n-1
while high>=low:
    mid=int((high+low)/2)
    if l[mid]==key:
        print("Element found at index ",mid)
        break
    elif l[mid]<key :
        low=mid+1
    else:
        high=mid-1
if high<low:
    print("element not found")
