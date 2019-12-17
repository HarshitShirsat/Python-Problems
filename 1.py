str1 = input("Enter string 1 -")
str2 = input("Enter string 2 -")
str=str1+" "+str2
res=""
for i in str:
    if i.isupper() == True:
        res+=i
print("Merged string is ",res)
