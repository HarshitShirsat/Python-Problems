str=input("Enter the string - ")
ans=""
count=0
for i in str:
    if i.isupper():
        count=count+1
        ans+=i
print("count = ",count)
print("capital = ",ans)
