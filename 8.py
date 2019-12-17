name=input("Enter your name - ")
x=len(name)
while x<=3 or x>=20:
    print("name not valid , enter again")
    name=input("Enter your name - ")
    x=len(name)
print(x)
