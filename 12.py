str=input("Enter the string - ")
count=0
for i in str:
    if i in ['a','e','i','o','u']:
        count=count+1
print("count - ",count)
