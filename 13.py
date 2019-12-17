str=input("ENter the string - ")
punc='''!@#$%^&*()_+-=`~{}|:"<>?[]\;,''./'''
newstr=""
for i in str:
    if i not in punc:
        newstr+=i
print(newstr)
