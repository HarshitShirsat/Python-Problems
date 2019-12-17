class Rectangle():
    def __init__(self,w,h):
        self.width=w;
        self.height=h;
    def getArea(self):
        return self.width*self.height

n=int(input("Enter the number of objects - "))
rectobj=[]
for i in range(n):
    print("Rectangle ",str(i+1))
    w=int(input("Enter the width - "))
    h=int(input("Enter the height - "))
    obj=Rectangle(w,h)
    rectobj.append(obj)

areaobj=[]
for i in rectobj:
    x=i.getArea()
    areaobj.append(x)

minindex=areaobj.index(min(areaobj))
maxindex=areaobj.index(max(areaobj))

print("Rectangle with minimum area :")
print("Width = ",rectobj[minindex].width," Height = ",rectobj[minindex].height)
print("Rectangle with maximum area :")
print("Width = ",rectobj[maxindex].width," Height = ",rectobj[maxindex].height)
