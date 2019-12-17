marks={'John':86.5,'Jack':91.2,'Jill':84.5,'Harry':72.1,'Joe':80.5}
sl=sorted(marks,key=marks.get,reverse=True)

print("Top 3 marks are")
for i in sl[:3]:
    print(i," : ",marks[i])

sum=0
for i in sl:
    sum+=marks[i]
avg=sum/5
print("Average is - ",avg)
